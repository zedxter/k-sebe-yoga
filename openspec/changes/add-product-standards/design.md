# Design — Add Product Standards (k-sebe-yoga)

## Approach

Add a single root-level `product-standards.md` following the team template
`projects/product-standards.template.md`. Content reflects the k-sebe-yoga entry already
present in the team's `projects/product-standards.md` — kept in sync.

Introduce the OpenSpec workflow contour to the repo (spec-driven cycle, `openspec/`),
so future changes follow the team canon.

## Layout

```
product-standards.md      # canonical per-project standard (English)
openspec/
  config.yaml             # schema spec-driven
  changes/                # OpenSpec changes
  specs/                  # specs
```

## Language

English, per the GitHub-content rule. Team's vault copy stays Russian.

## Risks / notes

- Documentation-only change, no behavior change.
- The OpenSpec contour init added `openspec/` and `.hermes/skills`; ensure the config
  is committed intentionally (project uses team spec pipeline).