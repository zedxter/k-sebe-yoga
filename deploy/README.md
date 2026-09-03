# Deployment Configuration — k-sebe-yoga

This directory contains deployment configuration files for serving the
k-sebe-yoga landing page via **Caddy** behind **systemd**.

## Files

| File | Purpose |
|------|---------|
| `Caddyfile` | Caddy v2 configuration — TLS, headers, static file serving |
| `k-sebe-yoga.service` | systemd unit for running Caddy as a managed service |

## Prerequisites

- A server (VPS or dedicated) with **Caddy v2** installed
- DNS records pointing `k-sebe-yoga.com` and `www.k-sebe-yoga.com` to the server IP
- Site content deployed to `/var/www/k-sebe-yoga/`

## Quick Start

```bash
# 1. Deploy site content
rsync -avz --delete ./ root@your-server:/var/www/k-sebe-yoga/

# 2. Install Caddy config
sudo mkdir -p /etc/caddy/sites/k-sebe-yoga
sudo cp deploy/Caddyfile /etc/caddy/sites/k-sebe-yoga/

# 3. Install systemd unit
sudo cp deploy/k-sebe-yoga.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now k-sebe-yoga

# 4. Verify
sudo systemctl status k-sebe-yoga
curl -I https://k-sebe-yoga.com
```

## Rollback

```bash
# 1. Revert to previous content
rsync -avz --delete ./root@your-server:/var/www/k-sebe-yoga/

# 2. If Caddy config changed, restore previous version
sudo cp deploy/Caddyfile.bak /etc/caddy/sites/k-sebe-yoga/Caddyfile
sudo systemctl reload k-sebe-yoga

# 3. If systemd unit changed
sudo cp deploy/k-sebe-yoga.service.bak /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl restart k-sebe-yoga
```

## Logs

```bash
journalctl -u k-sebe-yoga -f          # systemd logs
tail -f /var/log/caddy/k-sebe-yoga.log  # Caddy access logs
```

## Notes

- TLS is handled automatically by Caddy (Let's Encrypt via ACME)
- The `Caddyfile` assumes Caddy v2. If using v1, adjust the syntax
- Custom domain setup requires DNS A/AAAA records pointing to the server
- CORS header `Access-Control-Allow-Origin: *` is set on all assets, as required by `product-standards.md` for `design.css`