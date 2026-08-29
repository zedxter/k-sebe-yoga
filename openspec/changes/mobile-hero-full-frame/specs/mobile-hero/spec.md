# Mobile Hero — full-height vertical cover, text on top

## ADDED Requirements

### Requirement: Vertical cover renders in full height on mobile
On viewports ≤ 720px the hero image `hero-mobile.jpg` must display at its
natural 9:16 aspect ratio (full height), not be cropped.

#### Scenario: Mobile viewport shows the whole vertical cover
- GIVEN a viewport width of 390px
- WHEN the page loads
- THEN the rendered hero image box aspect ratio ≈ natural ratio (1.78),
  i.e. `renderedHeight / renderedWidth ≈ naturalHeight / naturalWidth`
- AND the hero box height ≈ `viewportWidth * 1.78`

#### Scenario: No horizontal overflow on any mobile width
- GIVEN viewport widths of 320, 360, 390 and 414px
- WHEN the page layout is computed
- THEN `documentElement.scrollWidth - clientWidth === 0`

### Requirement: Hero copy sits at the top, clear of the figure
On mobile the text overlay (h1, subtitle, CTA, trust line) must be positioned
at the top of the hero so it does not overlap the woman (whose figure spans
~35–80% of the vertical height).

#### Scenario: Copy block stays in the top band
- GIVEN a mobile viewport (e.g. 390px width)
- WHEN the layout is computed
- THEN the bottom edge of `.hero-copy` is within the top 30% of the hero
  height (above the figure start at ~35%)

### Requirement: Desktop and tablet hero unchanged
Viewports ≥ 721px continue to use the horizontal `hero-wide.jpg` with the
existing layout (figure left, text in right column) — no regression.

#### Scenario: Wide viewport keeps the desktop hero
- GIVEN a viewport width of 1024px
- WHEN the page renders
- THEN the hero uses `hero-wide.jpg` (horizontal cover)
- AND the hero copy remains in the right column (text-align:left)