# Tasks

## 1. Update design spec (source of truth)
- [ ] `design/k-sebe-yoga-design.md`: mobile hero = vertical cover full height
      (aspect 9/16, no cover-crop); text overlay at top of image over figure.
- [ ] Confirm text-at-top + figure ~35–80% is documented.

## 2. Implement CSS/HTML fix in `index.html`
- [ ] In `@media(max-width:720px)`: let `.hero-img` flow full-height
      (`position:relative; width:100%; height:auto; object-fit:fill; display:block`)
      so the vertical cover is not cropped.
- [ ] Pin `.hero-copy` to the top (`position:absolute; top:1.1rem`, centered).
- [ ] Mobile `.hero-overlay` → soft top-down gradient for text legibility.
- [ ] Leave desktop/tablet (≥721px) hero untouched.

## 3. Verify headless at 320 / 360 / 390 / 414 / 1024
- [ ] `scrollWidth - clientWidth === 0` at every width.
- [ ] `hero-img` box ratio ≈ 1.78 on mobile (no crop).
- [ ] `.hero-copy` bottom ≤ 30% of hero height on mobile.
- [ ] 1024px still shows wide hero + right column copy (no regression).

## 4. Validate & ship
- [ ] `openspec validate --changes` passes.
- [ ] CI green on the PR.
- [ ] Report to Danil for eyes-on sign-off before merge.