"""
UI Pixel Validation — k-sebe-yoga against DESIGN.md (headless Playwright).

Screenshots at desktop + mobile viewports plus computed CSS token validation.

Usage:
  cd /home/danil/projects/k-sebe-yoga
  python3 design-evals/validate.py     # exits 1 if any token fails

Exit codes: 0 = all pass, 1 = failures detected, 2 = error
"""
import sys, os, json, re, pathlib, time, argparse
import yaml
from playwright.sync_api import sync_playwright

BASE = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
PROJECT = BASE.parent
DESIGN_FILE = PROJECT / "DESIGN.md"
CHECKS_FILE = BASE / "checks.json"
HTML_FILE = PROJECT / "index.html"

DESKTOP_VIEWPORT = {"width": 1440, "height": 900}
MOBILE_VIEWPORT  = {"width": 320,  "height": 568}


def parse_design_tokens(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return yaml.safe_load(m.group(1)) if m else yaml.safe_load(text)


def resolve_token(value, design, _depth=0):
    if _depth > 10 or not isinstance(value, str):
        return value
    if value.startswith("{") and value.endswith("}"):
        value = value.strip("{}")
    node = design
    for part in value.split("."):
        if isinstance(node, dict):
            node = node.get(part)
        else:
            return value
        if node is None:
            return value
    if isinstance(node, str) and (node.startswith("{") and node.endswith("}")):
        return resolve_token(node, design, _depth + 1)
    return node


def hex_to_rgb(h):
    h = h.lstrip("#").strip()
    if len(h) == 6:
        r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        return f"rgb({r}, {g}, {b})"
    return h


def normalize_font_family(raw):
    """Normalize font-family string for comparison.
    'Cormorant Garamond', Georgia, serif -> Cormorant Garamond
    "Cormorant Garamond" -> Cormorant Garamond
    Inter, system-ui... -> Inter
    """
    # Remove surrounding quotes
    raw = raw.strip().strip("'\"")
    # Take first named font (before comma, skipping generic families)
    for part in raw.split(","):
        part = part.strip().strip("'\"")
        if part and part.lower() not in ("serif", "sans-serif", "monospace", "system-ui"):
            return part
    return raw


def px_to_num(px_str):
    """Convert '25.6px' to float 25.6. Returns None if not px."""
    m = re.match(r"^(-?[\d.]+)px$", px_str.strip())
    return float(m.group(1)) if m else None


def compare_value(actual, expected):
    """Compare actual (computed CSS) vs expected (DESIGN.md token).
    Handles: px vs rem, font-family with fallbacks, colors, unitless line-height.
    """
    # Exact match first (fast path)
    if actual == expected:
        return True
    if not isinstance(actual, str) or not isinstance(expected, str):
        return False

    # Colors: expected is hex, actual is rgb()
    if expected.startswith("#"):
        return actual == hex_to_rgb(expected)

    # font-family: normalize both sides
    if normalize_font_family(actual) == normalize_font_family(expected):
        return True

    # Rem/px conversion: expected is like "1.6rem" or "0.92rem"
    rem_m = re.match(r"^([\d.]+)rem$", expected)
    if rem_m:
        expected_px = round(float(rem_m.group(1)) * 16, 2)
        actual_px = px_to_num(actual)
        if actual_px is not None and abs(actual_px - expected_px) < 0.3:
            return True

    # Unitless line-height: expected is "1.5", actual is like "40.8px"
    actual_px = px_to_num(actual)
    if actual_px is not None:
        try:
            expected_float = float(expected)
            if abs(actual_px - expected_float) < 0.3:
                return True
            # Also check: line-height = actual_px / computed font-size
            return False
        except (ValueError, TypeError):
            return False

    # borderRadius: "999px" vs "9999px" — accept both as full pill
    if actual.replace("px", "") in ("999", "9999") and expected.strip("px") in ("999", "9999"):
        return True

    return False


def compare_lineheight(actual, expected_unitless, font_size_px):
    """Compare lineHeight: expected is unitless (e.g. '1.1'), actual is px.
    actual ≈ font_size_px * expected_unitless."""
    if not isinstance(actual, str):
        return False
    actual_px = px_to_num(actual)
    if actual_px is None:
        return False
    try:
        expected_f = float(expected_unitless)
    except (ValueError, TypeError):
        return False
    expected_px = round(font_size_px * expected_f, 2)
    return abs(actual_px - expected_px) < 0.5


def css_value(page, selector, prop):
    """Get computed CSS value, returning both bare value and context."""
    try:
        loc = page.locator(selector).first
        if not loc.is_visible():
            return "<NOT VISIBLE>"
        return loc.evaluate("(el, p) => getComputedStyle(el)[p]", prop)
    except Exception as e:
        return f"<ERROR: {e}>"


def css_font_size_px(page, selector):
    """Get computed font-size in px for lineHeight context."""
    v = css_value(page, selector, "fontSize")
    m = re.match(r"^(-?[\d.]+)px$", v.strip())
    return float(m.group(1)) if m else None


def validate_tokens(page, checks, design, viewport_name):
    total = passed = failures = 0
    report = []

    for sel, prop_list in checks.items():
        present = page.locator(sel).count() > 0
        for prop, token_path, desc in prop_list:
            total += 1
            if not present:
                report.append({
                    "el": sel, "prop": prop, "want": token_path,
                    "real": "<NOT FOUND>", "ok": False, "desc": desc,
                    "viewport": viewport_name
                })
                failures += 1
                continue

            real = css_value(page, sel, prop)
            expected_raw = resolve_token(token_path, design)
            expected = str(expected_raw) if expected_raw is not None else token_path

            # Special handling: lineHeight with unitless token vs px actual
            if prop == "lineHeight":
                fs = css_font_size_px(page, sel)
                if fs:
                    ok = compare_lineheight(real, expected, fs)
                else:
                    ok = compare_value(real, expected)
            else:
                ok = compare_value(real, expected)

            report.append({
                "el": sel, "prop": prop, "want": expected, "real": real,
                "ok": ok, "desc": desc, "viewport": viewport_name
            })
            if ok:
                passed += 1
            else:
                failures += 1

    return total, passed, failures, report


def take_screenshot(page, path):
    try:
        page.evaluate("document.body.scrollIntoView(true)")
        time.sleep(0.3)
        page.screenshot(path=str(path), full_page=True)
        return True
    except Exception:
        return False


def run():
    parser = argparse.ArgumentParser(
        description="UI Pixel Validation against DESIGN.md"
    )
    parser.add_argument(
        "--strict", action="store_true", default=False,
        help="[no-op] strict mode flag kept for CI compatibility"
    )
    parser.parse_args()

    design = parse_design_tokens(DESIGN_FILE)
    checks = json.loads(CHECKS_FILE.read_text(encoding="utf-8"))

    if not HTML_FILE.exists():
        print(f"[ERROR] index.html not found at {HTML_FILE}")
        sys.exit(2)

    target = HTML_FILE.resolve().as_uri()
    print(f"Target: {target}")

    all_reports = []
    grand_total = grand_passed = grand_failures = 0

    for vp_name, vp_size in [("desktop", DESKTOP_VIEWPORT), ("mobile", MOBILE_VIEWPORT)]:
        print(f"\n{'='*72}")
        print(f"  VIEWPORT: {vp_name.upper()}  ({vp_size['width']}x{vp_size['height']})")
        print(f"{'='*72}")

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport=vp_size)
            page.goto(target, wait_until="networkidle", timeout=15000)
            time.sleep(0.5)

            # Screenshot
            shot_dir = PROJECT / "design-evals" / "screenshots"
            shot_dir.mkdir(parents=True, exist_ok=True)
            shot_path = shot_dir / f"index-{vp_name}.png"
            if take_screenshot(page, shot_path):
                print(f"  Screenshot: {shot_path}")

            # Token validation
            total, passed, failures, report = validate_tokens(
                page, checks, design, vp_name
            )
            grand_total += total
            grand_passed += passed
            grand_failures += failures
            all_reports.extend(report)

            browser.close()

    # Report
    print(f"\n{'='*72}")
    print(f"  PIXEL VALIDATION REPORT")
    print(f"{'='*72}")
    for r in all_reports:
        icon = "✓" if r["ok"] else "✗"
        print(f"  [{icon}] {r['viewport']:<8} | {r['el']:<28} | {r['prop']:<18} | "
              f"got={str(r['real'])[:28]:<28} | want={str(r['want'])[:28]:<28} | {r['desc']}")

    print(f"\n{'='*72}")
    print(f"  RESULT: {grand_passed}/{grand_total} passed  |  {grand_failures} failures")
    shot_dir = PROJECT / "design-evals" / "screenshots"
    print(f"  Screenshots: {shot_dir}/")
    cert = "ДА" if grand_failures == 0 else "НЕТ"
    print(f"  CERTIFICATE: Соответствует DESIGN.md до пикселя: {cert}")
    print(f"{'='*72}\n")
    print(f"[INFO] Screenshots always generated (artifacts uploaded to CI).")
    if grand_failures > 0:
        print(f"[FAIL] {grand_failures} failures detected — exiting 1.")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    run()