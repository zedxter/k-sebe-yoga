# Product Standards — k-sebe-yoga

> Owner: Yennefer (PO) + Yulia (project owner). Version: 2026-08-31.
> Per-team rule (Danil, 25.08): every project documents its Product Standard at start.

## Mandatory core

| Axis | Value |
|------|-------|
| **monetization** | `nonprofit` (Danil's decision, 25.08) |
| **Success-axis / weights** | Top: **demand/response** (sign-ups, questions, feedback volume) + **path-to-action** (contact → attendance). Lower: **playbook** (role = community, not sandbox). Weights: demand 0.5, action 0.3, playbook 0.2 |
| **Unit economics** | N/A — free community offering, not a sandbox. Acquisition cost = Yulia's time + ads if any; metric = cost-per-lead. No revenue model |
| **North Star metric** | **participation/retention**: sign-ups → attendance → repeat attendance. "Came and came back." Threshold: ≥3 repeat attendances/month → "retained". TBD: numeric target after first session data |
| **Quality gate** | Full spec→PR→review→CI cycle (team canon). Design per Lutik's rules (full figure, text-free images). Security when payments/user data are introduced |

### Design gate (added 2026-09-02)

- **Source of truth:** DESIGN.md for visual design tokens, design.css for published stylesheet
- **DESIGN.md:** must be linted before merge — YAML valid, all 6 anti-patterns present
- **Stylesheet:** published at public URL, Content-Type `text/css`, CORS configured (`Access-Control-Allow-Origin: *`)
- **Eval scenarios:** ≥1 design-eval scenario must PASS before merge
- **ui-pixel-validation:** must pass on key pages (index.html, desktop + mobile 320px)
- **Design review:** required before merge (Lutik or owner approval)
| **Definition of Done** | Current stage (landing): landing is live, CTA collects sign-ups, CI is green. Full DoD when the service/product is live and had its first session |

### CD / auto-deploy

Static landing: GitHub Pages auto-builds from `main`. CI workflow: `.github/workflows/ci.yml` checks `index.html`, assets, and links. A project is not properly set up without CI.

## Project-specific

- **Audience**: Russian-speaking women, Potsdam/Berlin, 25–50
- **Format**: outdoor (park) yoga, free, 1–2×/week (weekend morning)
- **Content language**: Russian (landing + community comms)
- **Contact channel**: Telegram (Yulia: @Yulia_yoga_innere_balance)
- **Seasonality**: warm season (May–Sep). Winter: pause or indoor format

## Feedback loop

| Channel | Status | Where |
|---------|--------|-------|
| Telegram DM (Yulia) | ✅ active | @Yulia_yoga_innere_balance — primary contact |
| Landing feedback form | 🔜 add in development | "I want to come / question / suggestion" |
| Post-session verbal feedback | ✅ first session 30.08 | recorded in vault |

**Cadence:** light feedback after every session; monthly summary review.

## Standard owners

- Scope/metrics: Yennefer (PO)
- Content/landing: Misha (voice)
- Design: Lutik
- Quality: Geralt (CTO)
- Final approval: Danil

## Related

- `openspec/changes/add-product-standards/` — spec for this document
- `projects/projects.md` — registry
- `landing-copy-ru.md` — landing copy

## OpenSpec contour

This repo uses OpenSpec (spec-driven) for all changes. See `openspec/config.yaml`.