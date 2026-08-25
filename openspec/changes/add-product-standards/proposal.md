# Add Product Standards — k-sebe-yoga

## Why

k-sebe-yoga is an active development-phase project (design-led landing). It needs product
standards documented in the repo so that future phases (moving to a live product, pricing,
metrics) follow a fixed baseline. This aligns with the team rule (Danil, 25.08): every project
documents its Product Standard at start.

This change also introduces the OpenSpec workflow contour to the repo (spec-driven cycle),
since the project runs the full team development cycle.

## What

Add `product-standards.md` at the repo root (English, per GitHub-language rule), capturing
the four mandatory axes:

- **Unit economics:** TBD / deferred — to define when the project moves to a live/product
  phase (service→product direction: bookings/subscription).
- **North Star:** TBD / deferred — likely conversion into bookings/enquiries when live.
- **Quality gate:** full spec→review cycle (team canon, "no lite" for GitHub repos);
  design per Lutik's rules (text-free images, full figure visible); security when payments
  integrate (if any).
- **Definition of Done:** for the current stage — deliver to mockup/next phase per spec,
  passed review; full DoD when the product is live.

## Acceptance criteria

- `product-standards.md` exists at repo root, English, covers the 4 mandatory axes.
- OpenSpec contour is in place (`openspec/` with config, changes, specs) so future changes
  follow the team spec→code cycle.
- `openspec validate --changes` passes.