# Design — mobile hero full-height vertical cover

## Approach

Single-file CSS change in the existing `@media(max-width:720px)` block plus a
tiny `@media`-guarded style so the desktop absolute-cover hero is untouched.

Current mobile hero markup (unchanged):
```html
<div class="hero">
  <picture>
    <source media="(max-width:720px)" srcset="hero-mobile.jpg" />
    <source media="(min-width:721px)" srcset="hero-wide.jpg" />
    <img class="hero-img" src="hero-wide.jpg" alt="..." />
  </picture>
  <div class="hero-overlay"></div>
  <div class="hero-copy">h1 + sub + btn + trust</div>
  <div class="scroll-hint">⌄</div>
</div>
```

Base `.hero-img` is `position:absolute; inset:0; object-fit:cover` (for the
desktop full-bleed). That absolute + cover is what crops the portrait on
mobile.

## Mobile fix

In `@media(max-width:720px)`:

1. **Full height, no crop.** Repoint the image to document flow so it keeps its
   natural 9:16 aspect:
   ```css
   .hero-img{ position:relative; inset:auto; width:100%; height:auto;
              object-fit:fill; object-position:initial; display:block; }
   ```
   `.hero` already `position:relative`; on mobile drop its `aspect-ratio`
   (or leave auto) and let the in-flow image define the box → 390×~694px,
   ratio 1.78, no crop. `picture` set to `display:block`.

2. **Overlay/text pinned to the top.**
   ```css
   .hero-copy{ position:absolute; top:1.1rem; left:0; right:0; width:100%;
               max-width:none; margin:0; padding:0 1.4rem; text-align:center; }
   ```
   Keep h1/sub/btn/trust centered; tighten spacing so the whole copy block
   stays within the top ~30% of the hero (above the figure at ~35%).

3. **Soft top gradient** for text legibility, replacing the desktop right/bottom
   gradient on mobile:
   ```css
   .hero-overlay{ background: linear-gradient(to bottom,
       rgba(75,55,43,.55) 0%, rgba(75,55,43,0) 45%); }
   ```

Desktop `.hero`/`.hero-copy` untouched (min-width 721px uses `hero-wide.jpg`).

## Layout at 390px (expected)

```
┌────────────────────────┐ y=0
│  h1 / sub / btn / trust│ copy block (~0–30%)
│▁ gradient───────────── │
│                        │ figure head ~35%
│        🧘  woman       │
│                        │ figure extends to ~80%
└────────────────────────┘
```

## Risks / notes

- Purely presentational; no content change.
- Anchoring text to top is the well-understood "no overlap" mobile hero
  pattern; figure sits center (~35–80%) so top band stays clear.
- The scroll-hint (⌄) stays absolute bottom — still fine over the vertical
  cover.
- Wide/tablet layout and all images unchanged → reversible trivially.