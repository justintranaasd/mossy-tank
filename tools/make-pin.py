#!/usr/bin/env python3
"""
Pinterest pin maker for Mossy Tank.
Usage:
  python3 make-pin.py background.jpg "Your Headline Here"
  python3 make-pin.py background.jpg "Your Headline Here" "BADGE TEXT" output.png
"""

import sys
import os
from PIL import Image, ImageDraw, ImageFont

PIN_W, PIN_H  = 1000, 1500
FONT_HEADLINE = "/System/Library/Fonts/Supplemental/DIN Condensed Bold.ttf"
FONT_BADGE    = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_DOMAIN   = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

GREEN_DARK    = (20,  83, 45)    # --green-900
GREEN_BADGE   = (47, 158, 107)   # --accent (lighter green for the badge)
WHITE         = (255, 255, 255)


def scale_and_crop(img, w, h):
    ratio = max(w / img.width, h / img.height)
    nw, nh = int(img.width * ratio), int(img.height * ratio)
    img = img.resize((nw, nh), Image.LANCZOS)
    left, top = (nw - w) // 2, (nh - h) // 2
    return img.crop((left, top, left + w, top + h))


def draw_bottom_gradient(img, height=680):
    overlay = Image.new("RGBA", (PIN_W, height), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    for y in range(height):
        # Strong at bottom, fades to transparent at top
        t     = y / height           # 0 = top of gradient, 1 = bottom
        alpha = int(215 * (t ** 0.55))
        d.line([(0, y), (PIN_W, y)], fill=(0, 0, 0, alpha))
    img.paste(overlay, (0, PIN_H - height), overlay)


def draw_badge(draw, img, text, y):
    """Draw a small green pill badge. Returns the bottom y of the badge."""
    font    = ImageFont.truetype(FONT_BADGE, 26)
    bbox    = draw.textbbox((0, 0), text, font=font)
    tw      = bbox[2] - bbox[0]
    pad_x, pad_y = 18, 9
    pill_w  = tw + pad_x * 2
    pill_h  = bbox[3] - bbox[1] + pad_y * 2
    x       = 60  # left-aligned with margin

    # Pill background with rounded corners
    pill = Image.new("RGBA", (pill_w, pill_h), (0, 0, 0, 0))
    pill_draw = ImageDraw.Draw(pill)
    pill_draw.rounded_rectangle([(0, 0), (pill_w - 1, pill_h - 1)],
                                 radius=pill_h // 2,
                                 fill=(*GREEN_BADGE, 255))
    img.paste(pill, (x, y), pill)

    # Badge text
    draw.text((x + pad_x, y + pad_y - 1), text, font=font, fill=WHITE)
    return y + pill_h


def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines, current = [], []
    for word in words:
        test = " ".join(current + [word])
        w = draw.textbbox((0, 0), test, font=font)[2]
        if w > max_width and current:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return lines


def make_pin(bg_path, headline, badge="PLANTED TANKS", output_path=None):
    img = Image.open(bg_path).convert("RGBA")
    img = scale_and_crop(img, PIN_W, PIN_H)

    # Top-down gradient to bury any pre-baked text in source images
    top_cover = Image.new("RGBA", (PIN_W, PIN_H), (0, 0, 0, 0))
    tc_draw   = ImageDraw.Draw(top_cover)
    cover_h   = 300
    for y in range(cover_h):
        alpha = int(180 * (1 - y / cover_h) ** 0.5)
        tc_draw.line([(0, y), (PIN_W, y)], fill=(0, 0, 0, alpha))
    img.paste(top_cover, (0, 0), top_cover)

    # Strong bottom-up gradient for text contrast
    draw_bottom_gradient(img, height=700)

    draw = ImageDraw.Draw(img)

    # --- Measure text block to position everything from the bottom up ---
    margin   = 60
    max_tw   = PIN_W - margin * 2
    domain_y = PIN_H - 52   # domain sits 52px from bottom

    # Domain font
    dfont  = ImageFont.truetype(FONT_DOMAIN, 28)
    domain = "mossytank.com"
    dw     = draw.textbbox((0, 0), domain, font=dfont)[2]

    # Headline font — find largest size that wraps nicely
    font_size = 120
    while font_size >= 72:
        font  = ImageFont.truetype(FONT_HEADLINE, font_size)
        lines = wrap_text(headline, font, max_tw, draw)
        lh    = draw.textbbox((0, 0), "Ag", font=font)[3] + 10
        if len(lines) <= 4 and len(lines) * lh < 420:
            break
        font_size -= 6

    lines = wrap_text(headline, font, max_tw, draw)
    lh    = draw.textbbox((0, 0), "Ag", font=font)[3] + 10
    total_text_h = len(lines) * lh

    # Layout from bottom: domain → gap → headline → gap → badge
    headline_bottom = domain_y - 28
    headline_top    = headline_bottom - total_text_h
    badge_y         = headline_top - 48

    # Draw badge
    draw_badge(draw, img, badge, badge_y)

    # Draw headline lines
    y = headline_top
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        x    = margin   # left-aligned (feels more editorial than centered)
        # Shadow
        draw.text((x + 2, y + 2), line, font=font, fill=(0, 0, 0, 140))
        draw.text((x, y),         line, font=font, fill=WHITE)
        y += lh

    # Draw domain name
    draw.text(((PIN_W - dw) // 2, domain_y), domain, font=dfont,
              fill=(255, 255, 255, 190))

    # Thin green line above domain
    accent = Image.new("RGBA", (PIN_W, 3), (*GREEN_DARK, 255))
    img.paste(accent, (0, domain_y - 12), accent)

    # Output
    if output_path is None:
        base        = os.path.splitext(bg_path)[0]
        output_path = f"{base}_pin.png"

    img.convert("RGB").save(output_path, "PNG")
    print(f"Pin saved → {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python3 make-pin.py <image> "Headline" ["BADGE"] [output.png]')
        sys.exit(1)
    bg      = sys.argv[1]
    title   = sys.argv[2]
    badge   = sys.argv[3] if len(sys.argv) > 3 else "PLANTED TANKS"
    out     = sys.argv[4] if len(sys.argv) > 4 else None
    make_pin(bg, title, badge, out)
