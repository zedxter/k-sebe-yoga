# Spec: Resolve DESIGN.md hero image contract (Closes #83)

## Background

Issue #83: DESIGN.md asserts `cover.jpg` as the single hero source (approved 24.08),
but `index.html` serves `hero-wide.jpg` (≥721px) and `hero-mobile.jpg` (≤720px)
via `<picture>` + `<source>`.

Additionally, 6 legacy files sit unused: `cover.jpg`, `cover-v2.jpg`,
`cover-v2-mobile.jpg`, `cover-desktop.png`, `cover-mobile.png`, `cover-tablet.png`
(~4.8 MB total dead weight).

## Context

The `mobile-hero-full-frame` OpenSpec change (Aug 27–Sep 3, PR `spec/mobile-hero-full-frame`)
deliberately introduced the two-image responsive pattern:

- **hero-wide.jpg** (204 KB, horizontal) — desktop hero at ~72vh edge-to-edge
- **hero-mobile.jpg** (144 KB, vertical 9:16) — mobile full-height no-crop hero

This was a considered design decision: `cover.jpg` (horizontal) could not provide
the full-height mobile experience that Danil requested on 2026-08-29. The vertical
`hero-mobile.jpg` is essential for the mobile anti-pattern fix (cut-off figure,
text-on-image overflow).

The design spec `design/k-sebe-yoga-design.md` was already updated to describe
the two-image set, but the root **DESIGN.md** — which serves as the token source
of truth for pixel validation — still references `cover.jpg`.

## Decision: Option A — Update DESIGN.md, keep hero-*.jpg

**Rationale:**

1. **The two-image set is a considered design improvement**, not drift. The
   mobile-hero-full-frame change was deliberate: horizontal for desktop (hero-wide.jpg,
   figure-left + text-right column) + vertical for mobile (hero-mobile.jpg, text-on-top
   + full-height figure).

2. **Reverting to single cover.jpg would break the mobile fix.** `cover.jpg` is a
   horizontal image — it cannot provide the 9:16 full-height mobile experience
   (`object-fit: cover` would crop the figure). The cut-off figure anti-pattern
   would return.

3. **Responsive images are simpler** than a single image that must work across
   all sizes with awkward cropping. The `<picture>` + breakpoint pattern is
   standard, lightweight, and has zero JS/framework overhead.

4. **Smaller total payload:** hero-wide.jpg + hero-mobile.jpg = 348 KB vs
   cover.jpg alone is 114 KB (and at poor mobile quality). No PNG assets needed.

5. **The design spec already documents the two-image pattern** at
   `design/k-sebe-yoga-design.md` (sections 3 and "Требуемый образ обложки").

## Changes

### 1. DESIGN.md — update hero references

Replace all `cover.jpg` references with `hero-wide.jpg` / `hero-mobile.jpg`:

- Section `### Hero (критичный раздел)` line 152: `cover.jpg (24.08)` →
  `hero-wide.jpg (десктоп) + hero-mobile.jpg (мобильный)`
- Do/Don't lines 179, 186, 187, 210: update accordingly
- Keep the "один целостный кадр" principle — the hero-wide.jpg and
  hero-mobile.jpg are derived from the same coherent scene

### 2. README.md — update file listing

Tree listing shows `cover.jpg` as the hero image — update to `hero-wide.jpg`.

### 3. Delete unreferenced files

These files are not referenced in any active code and bloat the repo (~4.8 MB):

- `cover.jpg` — superseded by hero-wide.jpg
- `cover-v2.jpg` — intermediate generation
- `cover-v2-mobile.jpg` — intermediate generation
- `cover-desktop.png` — legacy PNG, never used
- `cover-mobile.png` — legacy PNG, never used
- `cover-tablet.png` — legacy PNG, never used

## Acceptance criteria

- [ ] DESIGN.md hero section references `hero-wide.jpg` + `hero-mobile.jpg`
- [ ] DESIGN.md Do/Don't list matches current hero image set
- [ ] DESIGN.md anti-pattern references updated to reflect current image names
- [ ] README.md file tree lists active hero images
- [ ] Dead image files deleted from repo
- [ ] `index.html` unchanged (it already serves the correct images)
- [ ] `validate.py` / `checks.json` unchanged (no hero-image validation there)
- [ ] PR created, references Closes #83

## References

- Issue #83: DESIGN.md hero image contract conflicts
- Issue #57: Unused image assets bloat repository
- OpenSpec change: `mobile-hero-full-frame`
- PR: (to be created)