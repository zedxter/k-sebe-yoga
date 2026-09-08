# k-sebe-yoga

**"To yourself."** A single-page landing that invites women to join shared outdoor yoga practice in Potsdam / Berlin — for the Russian-speaking community.

> Practice: "return to yourself" — women's energy, intuition, wishes, unfolding talents. It is not fitness; it is soft, inner-potential work in the open air.

## Status
- **Active** since 2026-08-23. Registry row: `projects/projects.md` (vault).
- Iteration 1: hero cover header + intro text (text came from Daniil 23.08). Structure being locked.

## Contact / CTA
- Questions / sign-up: [write in Telegram](https://t.me/Yulia_yoga_innere_balance)
- CTA on the page: **«По всем вопросам пишите в Telegram»** → link to that t.me.

## Stack
Single-page static site: plain HTML + CSS, no backend.

## Structure
```
k-sebe-yoga/
├── index.html      ← the landing (hero + Russian copy + t.me CTA)
├── hero-wide.jpg   ← hero cover (desktop, ≥721px)
├── hero-mobile.jpg ← hero cover (mobile, ≤720px)
└── README.md       ← this file
```

## What it should feel like
Warm, from the heart, not a corporate fitness page. First screen: cover image + a short invitation to come breathe together, outside, in Potsdam.

## Security

Security headers are enforced at two levels:

1. **Caddy HTTP headers** (production server `k-sebe-yoga.com`):
   - `Strict-Transport-Security`: 1 year, include subdomains, preload
   - `Content-Security-Policy`: restricts resources to self, no scripts
   - `X-Frame-Options: DENY`: prevents clickjacking
   - `X-Content-Type-Options: nosniff`: prevents MIME sniffing
   - `Referrer-Policy: strict-origin-when-cross-origin`
   - `Permissions-Policy`: disables camera, microphone, geolocation
   - See `deploy/Caddyfile` for the full configuration

2. **CSP meta tag**: Added to both `index.html` and `impressum.html` as defense-in-depth, so Content-Security-Policy applies even when the page is served without custom HTTP headers (e.g., via GitHub Pages).

HSTS cannot be set via a meta tag — it is enforced exclusively via the Caddy HTTP header.

## Links
- GitHub: https://github.com/zedxter/k-sebe-yoga