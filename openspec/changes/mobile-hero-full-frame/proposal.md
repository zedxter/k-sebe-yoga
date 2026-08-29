# Mobile hero — vertical cover in full height, text on top

## Why

On mobile (`max-width:720px`) the hero renders the **vertical** cover
`hero-mobile.jpg` (720×1280, aspect 9:16) inside a `390×337px` box via
`object-fit:cover` + `object-position:center top`. Because the box ratio
(~0.86) is far from the image ratio (~1.78), the browser **crops the image
almost in half** — the woman is cut. Measured on a 390px viewport:

- image natural ratio: 1280/720 = 1.78
- rendered ratio: 337/390 = 0.86  → `cover` aggressively cropped
- `hero-copy` sits centered at 67px from the top and overlaps the figure

Danil's requirement (2026-08-29): render the vertical image **in full height
(no crop)**, and place the text overlay **at the top of the image** so it does
not cover the woman.

## What

CSS/HTML-only change in `index.html` mobile media block — no image regen:

- On mobile, let `hero-mobile.jpg` flow at its natural aspect (full height):
  put `<img class="hero-img">` in document flow (`position:static` +
  `width:100%; height:auto`), so the hero box inherits the 9:16 ratio and the
  cover is never cropped.
- Move `.hero-copy` to be absolutely positioned at the **top** of the hero
  (`top` near top edge), centered horizontally, over a soft top-down gradient
  for legibility.
- Keep the woman visible (her figure spans ~35–80% of vertical height); text
  stays in the top band (~0–30% of hero height).

Design spec `design/k-sebe-yoga-design.md` updated first (source of truth).

## Acceptance criteria

- On every mobile viewport (320/360/390/414): `documentElement.scrollWidth -
  clientWidth === 0` (no horizontal overflow).
- The rendered `hero-img` box aspect ratio equals the natural 9:16 (no crop):
  `renderedHeight/renderedWidth ≈ naturalHeight/naturalWidth (1.78)`.
- `hero-copy` bottom edge stays above the figure: `copyBottom <= 30% of hero
  height` (figure begins ~35%).
- Desktop/tablet (`>=721px`) layout unchanged.
- `openspec validate --changes` passes; CI green.