#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

SAFETY_TERMS: dict[str, list[str]] = {
    "medical": ["medication", "medicine", "doctor", "lexapro", "latuda", "cymbalta", "blood pressure", "heartburn", "supplement", "magnesium", "coq10"],
    "alcohol": ["alcohol", "sober", "sobriety", "aa", "abv", "ferment", "fermentation", "kilju", "kvass", "wine", "beer", "liquor"],
    "nicotine": ["nicotine", "snus", "vape", "vaping", "tobacco", "pouch", "cigar", "fum"],
    "inhalation": ["vape", "vaping", "inhal", "smoke", "liquid smoke", "essential oil", "diffuser", "mct oil"],
}


@dataclass(frozen=True)
class MessagePart:
    role: str
    text: str
    create_time: float


@dataclass(frozen=True)
class ConversationHit:
    shard: str
    shard_index: int
    conversation_id: str
    title: str
    date: str
    matched_terms: list[str]
    safety_tags: list[str]
    snippets: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Mine a local ChatGPT export into a bounded derivative markdown source index."
    )
    parser.add_argument("--root", required=True, help="Path containing conversations-*.json shards.")
    parser.add_argument(
        "--terms",
        required=True,
        help="Comma-separated search terms. Terms are matched case-insensitively as literals.",
    )
    parser.add_argument("--out", required=True, help="Markdown output path.")
    parser.add_argument("--title", default="Chat Export Source Index", help="Markdown title.")
    parser.add_argument("--max-conversations", type=int, default=40)
    parser.add_argument("--max-snippets", type=int, default=3)
    parser.add_argument("--max-snippet-chars", type=int, default=420)
    parser.add_argument(
        "--context-chars",
        type=int,
        default=180,
        help="Characters of context to keep on either side of a match before bounding.",
    )
    return parser.parse_args()


def normalize_terms(raw: str) -> list[str]:
    terms: list[str] = []
    for item in raw.split(","):
        term = " ".join(item.strip().split())
        if term and term.lower() not in {t.lower() for t in terms}:
            terms.append(term)
    if not terms:
        raise SystemExit("--terms must contain at least one non-empty term")
    return terms


def bounded_positive(name: str, value: int, minimum: int, maximum: int) -> int:
    if value < minimum or value > maximum:
        raise SystemExit(f"{name} must be between {minimum} and {maximum}; got {value}")
    return value


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"failed to parse JSON {path}: {exc}") from exc


def iter_conversations(path: Path) -> Iterable[tuple[int, dict[str, Any]]]:
    data = load_json(path)
    if isinstance(data, list):
        for index, item in enumerate(data):
            if isinstance(item, dict):
                yield index, item
    elif isinstance(data, dict):
        conversations = data.get("conversations")
        if isinstance(conversations, list):
            for index, item in enumerate(conversations):
                if isinstance(item, dict):
                    yield index, item
        else:
            yield 0, data


def extract_parts(conversation: dict[str, Any]) -> list[MessagePart]:
    parts: list[MessagePart] = []
    mapping = conversation.get("mapping")
    if not isinstance(mapping, dict):
        return parts
    for node in mapping.values():
        if not isinstance(node, dict):
            continue
        message = node.get("message")
        if not isinstance(message, dict):
            continue
        author = message.get("author") if isinstance(message.get("author"), dict) else {}
        role = str(author.get("role") or "unknown")
        create_time = message.get("create_time") or 0.0
        content = message.get("content") if isinstance(message.get("content"), dict) else {}
        raw_parts = content.get("parts")
        if not isinstance(raw_parts, list):
            continue
        for raw_part in raw_parts:
            if isinstance(raw_part, str) and raw_part.strip():
                parts.append(MessagePart(role=role, text=raw_part, create_time=float(create_time or 0.0)))
    parts.sort(key=lambda item: item.create_time)
    return parts


def compile_terms(terms: list[str]) -> re.Pattern[str]:
    ordered = sorted(terms, key=len, reverse=True)
    return re.compile("|".join(re.escape(term) for term in ordered), re.IGNORECASE)


def compact(text: str) -> str:
    return " ".join(text.split())


def bound_snippet(text: str, match: re.Match[str], context_chars: int, max_chars: int) -> str:
    start = max(0, match.start() - context_chars)
    end = min(len(text), match.end() + context_chars)
    snippet = compact(text[start:end])
    if len(snippet) <= max_chars:
        return snippet
    half = max(40, (max_chars - 5) // 2)
    needle = compact(match.group(0))
    center = snippet.lower().find(needle.lower())
    if center == -1:
        return snippet[: max_chars - 4].rstrip() + " ..."
    left = max(0, center - half)
    right = min(len(snippet), center + len(needle) + half)
    prefix = "... " if left > 0 else ""
    suffix = " ..." if right < len(snippet) else ""
    return prefix + snippet[left:right].strip() + suffix


def date_from_timestamp(value: Any) -> str:
    try:
        if value:
            return datetime.fromtimestamp(float(value), tz=timezone.utc).date().isoformat()
    except (TypeError, ValueError, OSError):
        pass
    return "unknown-date"


def safety_tags_for(text: str) -> list[str]:
    lower = text.lower()
    tags = []
    for tag, terms in SAFETY_TERMS.items():
        if any(term in lower for term in terms):
            tags.append(tag)
    return tags


def score_hit(matched_terms: list[str], snippets: list[str], safety_tags: list[str]) -> tuple[int, int, int]:
    specific = sum(1 for term in matched_terms if len(term) >= 8 or " " in term)
    return (specific, len(matched_terms), len(snippets) - len(safety_tags))


def mine(root: Path, terms: list[str], max_conversations: int, max_snippets: int, max_snippet_chars: int, context_chars: int) -> list[ConversationHit]:
    pattern = compile_terms(terms)
    hits: list[ConversationHit] = []
    shards = sorted(root.glob("conversations-*.json"))
    if not shards:
        raise SystemExit(f"no conversations-*.json shards found under {root}")
    for shard in shards:
        for shard_index, conversation in iter_conversations(shard):
            parts = extract_parts(conversation)
            if not parts:
                continue
            full_text = "\n".join(part.text for part in parts)
            if not pattern.search(full_text):
                continue
            matched_terms = sorted({match.group(0).lower() for match in pattern.finditer(full_text)})
            snippets: list[str] = []
            seen_snippets: set[str] = set()
            for part in parts:
                for match in pattern.finditer(part.text):
                    snippet = f"{part.role}: {bound_snippet(part.text, match, context_chars, max_snippet_chars)}"
                    if snippet not in seen_snippets:
                        snippets.append(snippet)
                        seen_snippets.add(snippet)
                    if len(snippets) >= max_snippets:
                        break
                if len(snippets) >= max_snippets:
                    break
            if not snippets:
                continue
            hit = ConversationHit(
                shard=shard.name,
                shard_index=shard_index,
                conversation_id=str(conversation.get("conversation_id") or conversation.get("id") or "unknown"),
                title=str(conversation.get("title") or "Untitled"),
                date=date_from_timestamp(conversation.get("create_time") or conversation.get("update_time")),
                matched_terms=matched_terms,
                safety_tags=safety_tags_for(full_text),
                snippets=snippets,
            )
            hits.append(hit)
    hits.sort(key=lambda hit: (score_hit(hit.matched_terms, hit.snippets, hit.safety_tags), hit.date), reverse=True)
    return hits[:max_conversations]


def markdown_escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(path: Path, title: str, root: Path, terms: list[str], hits: list[ConversationHit]) -> None:
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    lines: list[str] = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append("Status: derivative source index")
    lines.append(f"Generated: {now}")
    lines.append(f"Source root: `{root}`")
    lines.append("")
    lines.append("## Corpus Policy")
    lines.append("")
    lines.append("This file is a bounded derivative index. It must not contain full raw conversations, raw JSON dumps, rendered `chat.html`, or attachment contents.")
    lines.append("")
    lines.append("## Query")
    lines.append("")
    lines.append("Terms: " + ", ".join(f"`{term}`" for term in terms))
    lines.append(f"Hits emitted: {len(hits)}")
    lines.append("")
    lines.append("## Source Index")
    lines.append("")
    lines.append("| Shard | Index | Date | Title | Matched terms | Safety tags | Conversation id |")
    lines.append("|---|---:|---|---|---|---|---|")
    for hit in hits:
        lines.append(
            "| "
            + " | ".join(
                [
                    markdown_escape_cell(hit.shard),
                    str(hit.shard_index),
                    markdown_escape_cell(hit.date),
                    markdown_escape_cell(hit.title),
                    markdown_escape_cell(", ".join(hit.matched_terms)),
                    markdown_escape_cell(", ".join(hit.safety_tags) if hit.safety_tags else "none"),
                    markdown_escape_cell(hit.conversation_id),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## Bounded Snippets")
    lines.append("")
    for hit in hits:
        lines.append(f"### `{hit.shard}` #{hit.shard_index} - {hit.date} - {hit.title}")
        lines.append("")
        lines.append(f"Conversation id: `{hit.conversation_id}`")
        lines.append("")
        if hit.safety_tags:
            lines.append("Safety tags: " + ", ".join(f"`{tag}`" for tag in hit.safety_tags))
            lines.append("")
        for snippet in hit.snippets:
            lines.append(f"- {snippet}")
        lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"--root must be an existing directory: {root}")
    max_conversations = bounded_positive("--max-conversations", args.max_conversations, 1, 500)
    max_snippets = bounded_positive("--max-snippets", args.max_snippets, 1, 10)
    max_snippet_chars = bounded_positive("--max-snippet-chars", args.max_snippet_chars, 80, 1000)
    context_chars = bounded_positive("--context-chars", args.context_chars, 20, 500)
    terms = normalize_terms(args.terms)
    hits = mine(root, terms, max_conversations, max_snippets, max_snippet_chars, context_chars)
    write_markdown(Path(args.out), args.title, root, terms, hits)
    print(f"wrote {args.out} with {len(hits)} hits")


if __name__ == "__main__":
    main()
