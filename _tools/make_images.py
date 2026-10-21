#!/usr/bin/env python3
"""
Rebuild the two generated images of the site (B17):

  assets/img/profile-320.webp  320x320 Home hero photo, made from the profile photo
  assets/img/og-image.png      1200x630 link-preview image: round photo, name and tagline

Inputs come from the repository itself:
  - the photo named by "photo:" in _data/profile.yml (normally assets/img/profile.webp)
  - "name:" and "tagline:" in _data/profile.yml

Fonts: Plus Jakarta Sans (name) and Inter (tagline). If they are not already in
_tools/fonts/, the script downloads them from the google/fonts repository on GitHub.
If that fails, it uses a common system sans-serif font and says so.

Run it from the repository folder (Windows):
    py -m pip install pillow
    py _tools/make_images.py
"""
import os
import re
import sys
import urllib.request

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except ImportError:  # pragma: no cover
    sys.exit("Pillow is missing. Install it with:  py -m pip install pillow")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONT_DIR = os.path.join(HERE, "fonts")

FONTS = {
    "head": ("PlusJakartaSans[wght].ttf",
             "https://raw.githubusercontent.com/google/fonts/main/ofl/plusjakartasans/PlusJakartaSans%5Bwght%5D.ttf"),
    "body": ("Inter[opsz,wght].ttf",
             "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter%5Bopsz,wght%5D.ttf"),
}

FALLBACK_FONTS = [
    r"C:\Windows\Fonts\segoeuib.ttf",
    r"C:\Windows\Fonts\segoeui.ttf",
    r"C:\Windows\Fonts\arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/Library/Fonts/Arial.ttf",
]

# Palette (blueprint 8.1, light mode)
BG = (0xFF, 0xFC, 0xF8)
TEXT = (0x1F, 0x2A, 0x2E)
MUTED = (0x4B, 0x5A, 0x5E)
BRAND = (0x0F, 0x9D, 0x8A)
ACCENT = (0xFF, 0x6B, 0x4A)

OG_W, OG_H = 1200, 630
SAFE = 40  # nothing but background within 40 px of the edges


def read_profile():
    """Read top-level scalar keys from _data/profile.yml without needing PyYAML."""
    path = os.path.join(ROOT, "_data", "profile.yml")
    values = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r'^([A-Za-z_]+):\s*(.*)$', line.rstrip("\n"))
            if not m:
                continue
            key, raw = m.group(1), m.group(2).strip()
            if raw.startswith('"'):
                end = raw.find('"', 1)
                value = raw[1:end]
            elif raw.startswith("'"):
                end = raw.find("'", 1)
                value = raw[1:end]
            else:
                value = re.split(r"\s+#", raw, maxsplit=1)[0].strip()
            values[key] = value
    for key in ("name", "tagline", "photo"):
        if not values.get(key):
            sys.exit(f"_data/profile.yml has no '{key}:' value")
    return values


def font_file(kind):
    """Return a font path for 'head' or 'body', downloading it once if needed."""
    name, url = FONTS[kind]
    path = os.path.join(FONT_DIR, name)
    if os.path.exists(path) and os.path.getsize(path) > 10000:
        return path, True
    try:
        os.makedirs(FONT_DIR, exist_ok=True)
        print(f"Downloading {name} ...")
        with urllib.request.urlopen(url, timeout=60) as r:
            data = r.read()
        with open(path, "wb") as f:
            f.write(data)
        return path, True
    except Exception as e:  # network blocked or offline
        print(f"Could not download {name}: {e}")
        for fb in FALLBACK_FONTS:
            if os.path.exists(fb):
                print(f"Using fallback font {fb}")
                return fb, False
        sys.exit("No usable font found. Put the two font files in _tools/fonts/ and run again.")


def load_font(kind, size, weight, opsz=None):
    path, variable = font_file(kind)
    font = ImageFont.truetype(path, size)
    if variable:
        try:
            axes = font.get_variation_axes()
            values = []
            for ax in axes:
                n = ax["name"]
                n = n.decode() if isinstance(n, bytes) else n
                if n.lower().startswith("weight"):
                    values.append(weight)
                elif n.lower().startswith("optical") and opsz is not None:
                    values.append(max(ax["minimum"], min(ax["maximum"], opsz)))
                else:
                    values.append(ax["default"])
            font.set_variation_by_axes(values)
        except Exception as e:
            print(f"Note: could not set font weight ({e}); using the default weight.")
    return font


def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def circle_photo(photo, d):
    """Square-crop the photo and return it as an RGBA circle of diameter d (4x supersampled edge)."""
    sq = ImageOps.fit(photo, (d, d), method=Image.LANCZOS)
    big = d * 4
    mask = Image.new("L", (big, big), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, big - 1, big - 1), fill=255)
    mask = mask.resize((d, d), Image.LANCZOS)
    out = sq.convert("RGBA")
    out.putalpha(mask)
    return out


def smooth_circle(size, color):
    """Anti-aliased filled circle of diameter size, as RGBA."""
    big = size * 4
    mask = Image.new("L", (big, big), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, big - 1, big - 1), fill=255)
    mask = mask.resize((size, size), Image.LANCZOS)
    layer = Image.new("RGBA", (size, size), color + (255,))
    layer.putalpha(mask)
    return layer


def make_profile_320(photo, out_path):
    img = ImageOps.fit(photo, (320, 320), method=Image.LANCZOS)
    img.save(out_path, "WEBP", quality=82, method=6)
    print(f"Wrote {os.path.relpath(out_path, ROOT)} (320x320)")


def make_og(photo, name, tagline, out_path):
    img = Image.new("RGB", (OG_W, OG_H), BG)
    draw = ImageDraw.Draw(img)

    # Round photo with a teal ring (outer radius 175 px, centred vertically).
    d = 330
    cx, cy = 70 + 175, OG_H // 2
    ring = smooth_circle(2 * 175, BRAND)
    img.paste(ring, (cx - 175, cy - 175), ring)
    gap = smooth_circle(2 * 169, BG)
    img.paste(gap, (cx - 169, cy - 169), gap)
    face = circle_photo(photo, d)
    img.paste(face, (cx - d // 2, cy - d // 2), face)

    # Text block to the right of the photo.
    x0 = 480
    max_w = OG_W - 64 - x0

    name_size = 84
    name_font = load_font("head", name_size, 700)
    while draw.textlength(name, font=name_font) > max_w and name_size > 40:
        name_size -= 2
        name_font = load_font("head", name_size, 700)

    tag_size = 38
    tag_font = load_font("body", tag_size, 500, opsz=28)
    lines = wrap(draw, tagline, tag_font, max_w)
    while len(lines) > 3 and tag_size > 24:
        tag_size -= 2
        tag_font = load_font("body", tag_size, 500, opsz=28)
        lines = wrap(draw, tagline, tag_font, max_w)

    name_box = draw.textbbox((0, 0), name, font=name_font, anchor="ls")
    name_h = -name_box[1]
    line_gap = int(tag_size * 1.42)
    bar_gap_top, bar_h, bar_gap_bottom = 26, 7, 34
    block_h = name_h + bar_gap_top + bar_h + bar_gap_bottom + line_gap * (len(lines) - 1) + int(tag_size * 0.78)
    top = cy - block_h // 2

    baseline = top + name_h
    draw.text((x0, baseline), name, font=name_font, fill=TEXT, anchor="ls")

    bar_y = baseline + bar_gap_top
    draw.rounded_rectangle((x0, bar_y, x0 + 76, bar_y + bar_h), radius=3, fill=ACCENT)

    y = bar_y + bar_h + bar_gap_bottom + int(tag_size * 0.78)
    for line in lines:
        draw.text((x0, y), line, font=tag_font, fill=MUTED, anchor="ls")
        y += line_gap

    img.save(out_path, "PNG", optimize=True)
    print(f"Wrote {os.path.relpath(out_path, ROOT)} ({OG_W}x{OG_H})")
    return img


def check_margins(img):
    """Every non-background pixel must lie at least SAFE px inside the edges."""
    px = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if x < SAFE or y < SAFE or x >= w - SAFE or y >= h - SAFE:
                if px[x, y] != BG:
                    return False, (x, y)
    return True, None


def main():
    prof = read_profile()
    photo_path = os.path.join(ROOT, prof["photo"].lstrip("/").replace("/", os.sep))
    if not os.path.exists(photo_path):
        sys.exit(f"Photo not found: {photo_path}")
    photo = Image.open(photo_path).convert("RGB")
    out_dir = os.path.dirname(photo_path)
    base, _ = os.path.splitext(os.path.basename(photo_path))
    make_profile_320(photo, os.path.join(out_dir, base + "-320.webp"))
    og = make_og(photo, prof["name"], prof["tagline"], os.path.join(ROOT, "assets", "img", "og-image.png"))
    ok, where = check_margins(og)
    if ok:
        print(f"Check passed: everything is at least {SAFE} px inside the edges.")
    else:
        print(f"Warning: a pixel at {where} is closer than {SAFE} px to the edge.")


if __name__ == "__main__":
    main()
