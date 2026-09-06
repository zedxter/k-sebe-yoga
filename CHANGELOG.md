# Changelog

All notable changes to k-sebe-yoga will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

- CI runner switch from self-hosted to ubuntu-latest
- Guard-branch workflow to prevent direct pushes to main

## [2026-09-05]

### Fixed
- Python pip --break-system-packages flag for Debian 12 runner compatibility
- Removed personal names and emails from public-facing pages

### Changed
- CI pipeline switched to self-hosted VPS runner

## [2026-09-04]

### Added
- MIT LICENSE file
- HTML5 validation, broken link check (lychee), and accessibility audit (pa11y-ci) to CI pipeline
- Canonical URL and JSON-LD structured data for SEO
- SVG favicon and .nojekyll file for GitHub Pages

### Changed
- PR template updated: Related Issue section moved to top, Closes # placeholder added
- validate.py now exits with code 1 on failures unconditionally

### Fixed
- DESIGN.md aligned with actual hero image set (hero-wide.jpg + hero-mobile.jpg)

## [2026-09-03]

### Added
- Privacy Notice page and footer link
- Deployment configuration: Caddyfile, systemd unit, deploy README
- Open Graph and Twitter Card meta tags for social previews
- :focus-visible keyboard accessibility styles
- Pixel validation CI with --strict mode
- QA scripts (contrast check, CSS var reference check) integrated into CI
- Agents.md rules for worktree/repo-clone discipline

### Changed
- CI pipeline with HTML/link/a11y checks added to workflow
- Multiple rounds of review-finding fixes across deployment, QA, and design

### Fixed
- Original Yulia copy restored 1:1 (only date changed to "По воскресеньям, в 7:00")
- Semantic HTML structure restored while preserving original copy text
- Location updated from ambiguous "напишу в личку" to specific landmark (Ruinenberg main entrance)
- WCAG 1.4.11 contrast ratio issues in :focus-visible styles
- Stale Google CDN font references removed from privacy.html and impressum.html
- Pixel validation checks updated to match flat HTML structure after copy restoration
- Personal names removed from repo documentation

## [2026-09-01]

### Added
- Open Graph meta tags (initial attempt, refined on 2026-09-03)

## [2026-08-31]

### Added
- Product standards document for the project
- First community meetup report (2026-08-30 trial session)

## [2026-08-23]

### Added
- Project initialized: landing page with hero cover, intro copy, and CTA
- Russian copy for the landing page
- Hero images (desktop + mobile)
- README with project overview
- Initial CSS design system