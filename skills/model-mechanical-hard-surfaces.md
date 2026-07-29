# Model Mechanical Hard Surfaces

Type: Skill / mechanical modeling and animation
Status: Active
Kernel: Blender through persistent Home Center workspaces

## Trigger

Use for deliberately authored, editable, animatable tanks, jets, ships, armored transports, weapons, machinery, and other mechanical assemblies.

## Authority

Home Center provides owner-scoped persistent scene control, recipes, revision constraints, validation, provenance, storage, and production automation. Blender performs modeling, topology, modifiers, hierarchy, origins, pivots, constraints, animation, UV operations, materials, rendering, and GLB export. The immutable `.blend` revision is editable source truth.

Foundry is retired and must never be selected, recommended, probed, revived, or treated as a fallback or special-case authoring lane. Historical artifacts are evidence only.

## Live Operations

Use `drive_operation` with exactly one of:

- `blender.workspace.create`
- `blender.workspace.inspect`
- `blender.workspace.history`
- `blender.workspace.mutate`
- `blender.workspace.restore`
- `blender.workspace.render`
- `blender.workspace.export`
- `blender.workspace.status`

Every mutation names `workspaceId`, the exact current `baseRevisionId`, and an idempotency key. A successful mutation creates a new immutable revision. Reopen and inspect that revision before another meaningful change. Never regenerate a scene and call it iteration.

## Mechanical Workflow

1. Create or import the authorized workspace and inspect the complete scene.
2. State the visible and mechanical relationship being authored. Measure neighboring bounds, axes, hierarchy, and pivots.
3. Plan connected components, repeated linked geometry, parent hierarchy, named actions, constraints, and export behavior.
4. Mutate with typed Blender operations using stable object/component IDs and expected selection counts.
5. Inspect the new `.blend` revision. Verify topology, hierarchy, pivots, linked data, constraints, actions, and warnings.
6. Request clay, fixed-view, wireframe, and raking-light evidence after meaningful form changes. Request animation preview when articulation changes.
7. Export the exact accepted candidate revision as `.blend`, animated GLB, inspection manifest, and validation report.
8. Hand the GLB to the shared cloud viewer and await human judgment. Metrics and receipts cannot grant visual acceptance.

## Form and Topology Rules

- Openings, recesses, sockets, seams, and manufactured transitions require actual depth and topology.
- Prefer editing the connected source mesh over adding masks, decals, floating rings, or overlapping primitive blockers.
- Repeated mechanical parts should use linked or instanced geometry with distinct named objects and deliberate pivots.
- Preserve stable IDs across revisions and make mesh-level corrections to the existing scene.
- Reject coplanar detail decals, z-fighting, primitive soup, unexplained intersections, egg-like inflation, incorrect pivots, broken constraints, flattened hierarchy, and receipt worship.
- Vertex/triangle counts, manifold checks, and validation warnings are engineering guards only. Human visual review outranks them.

## Completion

A candidate is review-ready only when the exact persistent revision has been reopened, inspected, rendered through the authorized cloud lane, exported with hierarchy and named animations intact, and delivered through signed immutable links. It remains `unreviewed` until the human reviewer records a verdict.
