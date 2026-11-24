#!/usr/bin/env python3
"""Draw the front page of THE WORLD TODAY for Tuesday 24 November 2026.

Every headline, deck and number comes from news first reported on
24 November 2026 (live searches, sources listed in README.md).
All artwork is hand-drawn with PIL ImageDraw: no photos, no web images.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
NAVY = (16, 30, 67)
GOLD = (217, 164, 65)
PAPER = (250, 247, 240)
INK = (24, 24, 24)
GREY = (92, 92, 92)
RED = (178, 34, 34)
TEAL = (13, 110, 110)
BLUE = (30, 90, 168)
GREEN = (34, 120, 60)
PURPLE = (104, 60, 150)
ORANGE = (200, 90, 20)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Wrap text to fit max_w pixels, returning a list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def chip(draw, x, y, label, color):
    f = font(SANS_B, 17)
    w = draw.textlength(label, font=f) + 18
    draw.rounded_rectangle([x, y, x + w, y + 26], radius=13, fill=color)
    draw.text((x + 9, y + 4), label, font=f, fill="white")
    return w


def pictogram(draw, kind, cx, cy, s, color):
    """Small hand-drawn pictogram centred at (cx, cy), size s."""
    d = draw
    if kind == "chip":
        d.rounded_rectangle([cx - s // 2, cy - s // 3, cx + s // 2, cy + s // 3],
                            radius=8, fill=color)
        for i in range(3):
            d.line([cx - s // 4 + i * s // 4, cy - s // 3 - 10,
                    cx - s // 4 + i * s // 4, cy - s // 3], fill=color, width=4)
            d.line([cx - s // 4 + i * s // 4, cy + s // 3,
                    cx - s // 4 + i * s // 4, cy + s // 3 + 10], fill=color, width=4)
        d.rectangle([cx - s // 6, cy - s // 6, cx + s // 6, cy + s // 6],
                    outline="white", width=3)
    elif kind == "ship":
        d.polygon([(cx - s // 2, cy), (cx + s // 2, cy),
                   (cx + s // 3, cy + s // 4), (cx - s // 3, cy + s // 4)],
                  fill=color)
        d.rectangle([cx - s // 6, cy - s // 3, cx + s // 6, cy], fill=color)
        d.line([cx, cy - s // 2, cx, cy - s // 3], fill=color, width=4)
        for i, yy in enumerate([cy + s // 3, cy + s // 3 + 8]):
            d.arc([cx - s // 2, yy - 6, cx + s // 2, yy + 6], 0, 180, fill=BLUE, width=3)
    elif kind == "flame":
        d.polygon([(cx - s // 4, cy + s // 4), (cx - s // 6, cy - s // 6),
                   (cx, cy - s // 2), (cx + s // 5, cy - s // 8),
                   (cx + s // 4, cy + s // 4)], fill=ORANGE)
        d.ellipse([cx - s // 6, cy - s // 8, cx + s // 6, cy + s // 4], fill=RED)
        d.rectangle([cx - s // 2, cy + s // 4, cx + s // 2, cy + s // 3], fill=GREY)
    elif kind == "scales":
        d.line([cx, cy - s // 2, cx, cy + s // 3], fill=color, width=4)
        d.line([cx - s // 2, cy - s // 3, cx + s // 2, cy - s // 3], fill=color, width=4)
        d.polygon([(cx - s // 2, cy - s // 3), (cx - s // 3, cy + s // 6),
                   (cx - 2 * s // 3, cy + s // 6)], outline=color, width=3)
        d.polygon([(cx + s // 2, cy - s // 3), (cx + s // 3, cy + s // 6),
                   (cx + 2 * s // 3, cy + s // 6)], outline=color, width=3)
        d.rectangle([cx - s // 3, cy + s // 3, cx + s // 3, cy + s // 3 + 6], fill=color)
    elif kind == "jet":
        d.polygon([(cx - s // 2, cy), (cx + s // 2, cy - s // 6),
                   (cx + s // 2, cy + s // 6)], fill=color)
        d.polygon([(cx, cy - s // 6), (cx + s // 6, cy - s // 2),
                   (cx + s // 4, cy - s // 6)], fill=color)
        d.polygon([(cx, cy + s // 6), (cx + s // 6, cy + s // 2),
                   (cx + s // 4, cy + s // 6)], fill=color)
    elif kind == "train":
        d.rounded_rectangle([cx - s // 3, cy - s // 3, cx + s // 3, cy + s // 3],
                            radius=10, fill=color)
        d.rectangle([cx - s // 4, cy - s // 5, cx + s // 4, cy], fill="white")
        d.ellipse([cx - s // 5, cy + s // 8, cx - s // 12, cy + s // 4], fill=GOLD)
        d.ellipse([cx + s // 12, cy + s // 8, cx + s // 5, cy + s // 4], fill=GOLD)
        d.line([cx - s // 2, cy + s // 3 + 6, cx + s // 2, cy + s // 3 + 6],
               fill=GREY, width=4)
    elif kind == "chess":
        for r in range(2):
            for c in range(2):
                if (r + c) % 2 == 0:
                    d.rectangle([cx - s // 2 + c * s // 2, cy - s // 2 + r * s // 2,
                                 cx - s // 2 + (c + 1) * s // 2,
                                 cy - s // 2 + (r + 1) * s // 2], fill=color)
        d.ellipse([cx - s // 6, cy - s // 6, cx + s // 6, cy + s // 6], fill=GOLD)
        d.ellipse([cx - s // 12, cy - s // 12, cx + s // 12, cy + s // 12], fill=NAVY)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    d.rectangle([0, 0, W, 112], fill=NAVY)
    title = font(SERIF_B, 62)
    d.text((W // 2, 14), "THE WORLD TODAY", font=title, fill="white", anchor="ma")
    date_f = font(SANS_B, 27)
    d.text((W // 2, 80), "TUESDAY  24  NOVEMBER  2026", font=date_f,
           fill=GOLD, anchor="ma")
    d.rectangle([0, 112, W, 117], fill=GOLD)

    # ---- Lead story ----
    lead_head = font(SERIF_B, 40)
    lead_deck = font(SANS, 21)
    lx, ly = 28, 132
    chip(d, lx, ly, "TECH  ·  MARKETS", RED)
    head_lines = wrap(d, "Huang back at Nvidia after Trump push",
                      lead_head, 700)
    y = ly + 38
    for line in head_lines:
        d.text((lx, y), line, font=lead_head, fill=INK)
        y += 46
    deck_lines = wrap(
        d,
        "Nvidia's board reinstated Jensen Huang as chief executive, "
        "11 days after he resigned, and shares jumped more than 30%.",
        lead_deck, 700)
    for line in deck_lines:
        d.text((lx, y), line, font=lead_deck, fill=GREY)
        y += 27
    pictogram(d, "chip", 880, 225, 130, NAVY)
    d.line([28, 316, W - 28, 316], fill=GOLD, width=3)

    # ---- Grid: 6 stories, 2 cols x 3 rows ----
    stories = [
        ("WAR  ·  EUROPE", RED, "ship",
         "Ukraine sinks Russian warship in Libya",
         "Kyiv said sea drones sank a Russian corvette in a Libyan "
         "port, days after a cargo ship was hit off Finland."),
        ("DISASTER  ·  ASIA", ORANGE, "flame",
         "24 killed in Indonesia factory fire",
         "A blaze at a candy factory in Banten killed at least 24 "
         "people. Rescuers still search for about 30 missing."),
        ("TECH  ·  LAW", PURPLE, "scales",
         "US states sue Musk firms over Grok images",
         "States sued over sexualised images made with the Grok "
         "chatbot, in a new test of AI firms' duties."),
        ("SECURITY  ·  ASIA", BLUE, "jet",
         "Russian jet sparks Korea alert",
         "South Korea briefly warned Ulleung island after a Russian "
         "aircraft entered its airspace on Tuesday."),
        ("DIPLOMACY  ·  ASIA", GREEN, "train",
         "India-Nepal launch new cross-border train",
         "Modi and Nepal PM Balendra Shah flagged off the "
         "Saryu-Kamala Express, with a Rs 15,000 crore package."),
        ("SPORT  ·  CHESS", TEAL, "chess",
         "Gukesh begins world title defence",
         "India's D Gukesh defends his world chess crown against "
         "Javokhir Sindarov in Geneva from today."),
    ]
    head_f = font(SERIF_B, 26)
    deck_f = font(SANS, 18)
    gx0, gy0 = 28, 330
    cw, ch = 476, 168
    for i, (cat, color, pic, head, deck) in enumerate(stories):
        x = gx0 + (i % 2) * (cw + 16)
        yy = gy0 + (i // 2) * ch
        pictogram(d, pic, x + 52, yy + 62, 78, color)
        tx = x + 112
        chip(d, tx, yy + 6, cat, color)
        hl = wrap(d, head, head_f, cw - 122)
        y2 = yy + 40
        for line in hl[:2]:
            d.text((tx, y2), line, font=head_f, fill=INK)
            y2 += 31
        dl = wrap(d, deck, deck_f, cw - 122)
        for line in dl[:3]:
            d.text((tx, y2), line, font=deck_f, fill=GREY)
            y2 += 23
        if i % 2 == 0:
            d.line([x + cw + 8, yy + 8, x + cw + 8, yy + ch - 14],
                   fill=(210, 205, 195), width=2)

    # ---- By the numbers ----
    ny = 852
    d.rectangle([28, ny, W - 28, ny + 92], outline=GOLD, width=3)
    d.text((W // 2, ny + 8), "BY THE NUMBERS", font=font(SANS_B, 20),
           fill=NAVY, anchor="ma")
    nums = [("11", "days Huang was out"),
            ("24", "killed in factory fire"),
            ("30", "still missing"),
            ("2", "Russian ships hit")]
    seg_w = (W - 56) // 4
    for i, (n, label) in enumerate(nums):
        cx = 28 + seg_w * i + seg_w // 2
        d.text((cx, ny + 34), n, font=font(SERIF_B, 30), fill=RED, anchor="ma")
        d.text((cx, ny + 68), label, font=font(SANS, 15), fill=GREY, anchor="ma")
        if i:
            d.line([28 + seg_w * i, ny + 36, 28 + seg_w * i, ny + 84],
                   fill=(210, 205, 195), width=2)

    # ---- Footer ----
    d.line([28, 962, W - 28, 962], fill=GOLD, width=2)
    d.text((W // 2, 972), "The news of Tuesday 24 November 2026",
           font=font(SERIF_B, 20), fill=NAVY, anchor="ma")
    d.text((W // 2, 998),
           "Sources: Al Jazeera, CNN, Reuters, The Manila Times, Times of India",
           font=font(SANS, 14), fill=GREY, anchor="ma")

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
