#!/usr/bin/env python3
"""AI Security for Autonomous AI Agents — trainer slide deck (TGS-2025060473).

Component library adapted from the house COMPACT v2 reference
(.claude/skills/wsq-slides/reference/compact/build_slides.py).

House rules enforced here:
  · two trainer profile cards (general template + Dr Alfred Ang)
  · Download Course Material as a browser-mock visual, never a bare link
  · Assessment Flow diagram
  · Briefing BEFORE Assessment
  · TRAQOM digital attendance at the front AND the end
  · closing block: Assessment → Assessment Flow → Digital Attendance → Thank You
  · NO practice exam (non-certification course — its absence is correct)
  · NO step-by-step procedures (those live in the Learner Guide)
"""

import os, sys, json, math
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C
import deck_content as D

ASSETS = os.path.join(HERE, "assets")
OUTDIR = HERE

# ---------------- palette ----------------
BLUE = RGBColor(0x1F, 0x6F, 0xEB); TEAL = RGBColor(0x10, 0xB9, 0x81)
AMBER = RGBColor(0xF5, 0x9E, 0x0B); INK = RGBColor(0x16, 0x1B, 0x26)
GREY = RGBColor(0x5B, 0x63, 0x72); LIGHT = RGBColor(0xF5, 0xF8, 0xFC)
WHITE = RGBColor(0xFF, 0xFF, 0xFF); LINE = RGBColor(0xE2, 0xE8, 0xF0)
VIOLET = RGBColor(0x7C, 0x3A, 0xED); RED = RGBColor(0xDC, 0x26, 0x26)
NAVY = RGBColor(0x0B, 0x12, 0x20); CODEBLUE = RGBColor(0x9C, 0xDC, 0xFE)
PALETTE = [BLUE, TEAL, VIOLET, AMBER]
CMAP = {"BLUE": BLUE, "TEAL": TEAL, "VIOLET": VIOLET, "AMBER": AMBER, "RED": RED, "GREY": GREY}

prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]


def slide(): return prs.slides.add_slide(BLANK)


def rect(s, x, y, w, h, color, line=None):
    sp = s.shapes.add_shape(1, x, y, w, h); sp.fill.solid(); sp.fill.fore_color.rgb = color
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb = line; sp.line.width = Pt(1)
    sp.shadow.inherit = False; return sp


def oval(s, x, y, w, h, color):
    sp = s.shapes.add_shape(9, x, y, w, h); sp.fill.solid(); sp.fill.fore_color.rgb = color
    sp.line.fill.background(); sp.shadow.inherit = False; return sp


def txt(s, x, y, w, h, runs, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, space=4):
    tb = s.shapes.add_textbox(x, y, w, h); tf = tb.text_frame
    tf.word_wrap = True; tf.vertical_anchor = anchor
    for i, ln in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.space_after = Pt(space)
        for t, sz, col, bold in ln:
            r = p.add_run(); r.text = t; r.font.size = Pt(sz); r.font.bold = bold
            r.font.color.rgb = col; r.font.name = "Arial"
    return tb


def bullets(s, x, y, w, h, items, size=18, color=INK, gap=10, mcolor=BLUE):
    tb = s.shapes.add_textbox(x, y, w, h); tf = tb.text_frame; tf.word_wrap = True
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph(); p.space_after = Pt(gap)
        lvl = it[1] if isinstance(it, tuple) else 0
        text = it[0] if isinstance(it, tuple) else it
        r = p.add_run(); r.text = ("•  " if lvl == 0 else "–  ") + text
        r.font.size = Pt(size if lvl == 0 else size - 2)
        r.font.color.rgb = color if lvl == 0 else GREY
        r.font.name = "Arial"
        r.font.bold = (lvl == 0 and isinstance(it, tuple) and len(it) > 2 and it[2])
    return tb


PAGE = {"n": 0}; SLIDE_MAP = {}


def mark(key): SLIDE_MAP[key] = PAGE["n"] + 1


def footer(s):
    PAGE["n"] += 1
    txt(s, Inches(0.4), Inches(7.05), Inches(7.5), Inches(0.35),
        [[(f"{C.SHORT_TITLE}  ·  {C.COURSE_CODE}", 9, GREY, False)]])
    txt(s, Inches(5.0), Inches(7.05), Inches(3.3), Inches(0.35),
        [[("© 2026 Tertiary Infotech Pte Ltd", 9, GREY, False)]], align=PP_ALIGN.CENTER)
    txt(s, Inches(12.4), Inches(7.05), Inches(0.6), Inches(0.35),
        [[(str(PAGE["n"]), 9, GREY, False)]], align=PP_ALIGN.RIGHT)


def head(s, title, kicker=None, kcolor=BLUE):
    rect(s, 0, 0, SW, SH, WHITE); rect(s, 0, 0, Inches(0.28), Inches(1.55), kcolor)
    if kicker:
        txt(s, Inches(0.85), Inches(0.5), Inches(11.6), Inches(0.4), [[(kicker, 14, kcolor, True)]])
    txt(s, Inches(0.85), Inches(0.9), Inches(11.9), Inches(0.9), [[(title, 28, INK, True)]])
    rect(s, Inches(0.85), Inches(1.7), Inches(11.63), Inches(0.02), LINE)
    return s


def _asset(name):
    p = os.path.join(ASSETS, name)
    return p if os.path.exists(p) else None


def _fit(path, max_w_in, max_h_in):
    """Aspect-fit an image to a box, returning (w,h) in EMU. Never stretches."""
    with Image.open(path) as im:
        iw, ih = im.size
    ar = iw / ih
    w = max_w_in; h = w / ar
    if h > max_h_in:
        h = max_h_in; w = h * ar
    return Inches(w), Inches(h)


# ================================================================ components
def cover():
    s = slide(); rect(s, 0, 0, SW, SH, WHITE)
    rect(s, 0, 0, SW, Inches(0.22), BLUE); rect(s, 0, Inches(7.28), SW, Inches(0.22), RED)
    org = _asset("tertiary-infotech-logo.png")
    if org: s.shapes.add_picture(org, Inches(0.85), Inches(0.7), height=Inches(1.05))
    rect(s, Inches(10.6), Inches(0.72), Inches(1.95), Inches(1.0), RED)
    txt(s, Inches(10.6), Inches(0.84), Inches(1.95), Inches(0.5),
        [[("WSQ", 22, WHITE, True)]], align=PP_ALIGN.CENTER)
    txt(s, Inches(10.6), Inches(1.32), Inches(1.95), Inches(0.4),
        [[("AI SECURITY", 8, WHITE, True)]], align=PP_ALIGN.CENTER)
    txt(s, Inches(0.9), Inches(2.3), Inches(12), Inches(0.6),
        [[("TRAINER SLIDES  ·  WSQ", 16, BLUE, True)]])
    txt(s, Inches(0.9), Inches(2.85), Inches(12.0), Inches(1.9), [[(C.TITLE, 38, INK, True)]])
    rect(s, Inches(0.92), Inches(4.45), Inches(2.4), Inches(0.06), RED)
    txt(s, Inches(0.9), Inches(4.8), Inches(12), Inches(1.5),
        [[(f"WSQ Course Code: {C.COURSE_CODE}  ·  {C.DURATION}", 16, GREY, False)],
         [(f"Skills Framework TSC: {C.TSC_TITLE} ({C.TSC_CODE})", 14, GREY, False)],
         [("Conducted by Tertiary Infotech Pte Ltd  ·  UEN 20120096W", 14, GREY, False)]], space=6)
    txt(s, Inches(0.9), Inches(6.45), Inches(12), Inches(0.4),
        [[(f"Version {C.VERSION}  ·  {C.VERSION_DATE}", 12, GREY, False)]])
    txt(s, Inches(0.9), Inches(6.85), Inches(12), Inches(0.34),
        [[("© 2026 Tertiary Infotech Pte Ltd. All Rights Reserved.  ·  www.tertiarycourses.com.sg",
           10, GREY, False)]])
    PAGE["n"] += 1


def section(kicker, title, n, sub=""):
    s = slide(); rect(s, 0, 0, SW, SH, WHITE); rect(s, 0, 0, Inches(0.28), SH, BLUE)
    rect(s, Inches(0.85), Inches(2.5), Inches(0.14), Inches(2.0), RED)
    txt(s, Inches(1.25), Inches(2.55), Inches(11), Inches(0.6), [[(kicker, 18, BLUE, True)]])
    txt(s, Inches(1.25), Inches(3.0), Inches(11.4), Inches(1.6), [[(title, 40, INK, True)]])
    if sub: txt(s, Inches(1.27), Inches(4.55), Inches(11), Inches(0.8), [[(sub, 16, GREY, False)]])
    txt(s, Inches(10.0), Inches(0.7), Inches(2.8), Inches(1.6),
        [[(n, 72, LINE, True)]], align=PP_ALIGN.RIGHT)
    footer(s)


def content(title, items, kicker=None, size=20, kcolor=BLUE):
    s = head(slide(), title, kicker, kcolor=kcolor)
    bullets(s, Inches(0.85), Inches(1.95), Inches(11.6), Inches(4.9), items, size=size)
    footer(s); return s


def two_col(title, left, right, kicker=None, lhead="", rhead="",
            lcolor=BLUE, rcolor=TEAL, note=None):
    s = head(slide(), title, kicker)
    bh = Inches(4.7) if not note else Inches(4.15)
    rect(s, Inches(0.85), Inches(1.95), Inches(5.7), bh, LIGHT)
    rect(s, Inches(6.95), Inches(1.95), Inches(5.55), bh, LIGHT)
    rect(s, Inches(0.85), Inches(1.95), Inches(5.7), Inches(0.1), lcolor)
    rect(s, Inches(6.95), Inches(1.95), Inches(5.55), Inches(0.1), rcolor)
    if lhead: txt(s, Inches(1.1), Inches(2.15), Inches(5.2), Inches(0.4), [[(lhead, 16, lcolor, True)]])
    if rhead: txt(s, Inches(7.2), Inches(2.15), Inches(5.0), Inches(0.4), [[(rhead, 16, rcolor, True)]])
    bullets(s, Inches(1.1), Inches(2.7), Inches(5.2), bh - Inches(0.9), left, size=15)
    bullets(s, Inches(7.2), Inches(2.7), Inches(5.05), bh - Inches(0.9), right, size=15, mcolor=rcolor)
    if note:
        txt(s, Inches(0.85), Inches(6.25), Inches(11.7), Inches(0.6), [[(note, 13, GREY, False)]],
            align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s


def cards3(title, cards, kicker, kcolor=BLUE):
    s = head(slide(), title, kicker, kcolor=kcolor); xs = [Inches(0.85), Inches(5.0), Inches(9.15)]
    for i, c in enumerate(cards[:3]):
        x = xs[i]; col = c[0]
        rect(s, x, Inches(1.95), Inches(3.65), Inches(4.7), LIGHT)
        rect(s, x, Inches(1.95), Inches(3.65), Inches(0.12), col)
        txt(s, x + Inches(0.25), Inches(2.2), Inches(3.2), Inches(0.6), [[(c[1], 19, col, True)]])
        bullets(s, x + Inches(0.25), Inches(2.95), Inches(3.2), Inches(3.4), c[2],
                size=14, mcolor=col, gap=9)
    footer(s); return s


def big_statement(line1, line2, kicker, color=BLUE):
    s = slide(); rect(s, 0, 0, SW, SH, WHITE); rect(s, 0, 0, Inches(0.28), SH, color)
    txt(s, Inches(1.1), Inches(2.2), Inches(11), Inches(0.5), [[(kicker, 16, color, True)]])
    txt(s, Inches(1.1), Inches(2.8), Inches(11.3), Inches(2.4), [[(line1, 38, INK, True)]])
    if line2: txt(s, Inches(1.12), Inches(4.9), Inches(11), Inches(1.2), [[(line2, 20, GREY, False)]])
    footer(s); return s


def tile_grid(title, items, kicker=None, cols=2, size=15, accent=BLUE):
    s = head(slide(), title, kicker, kcolor=accent)
    n = len(items); rows = math.ceil(n / cols)
    X0 = Inches(0.85); Y0 = Inches(1.95); TOTW = Inches(11.63); AREAH = Inches(4.78)
    gx = Inches(0.25); gy = Inches(0.22)
    cw = int((TOTW - gx * (cols - 1)) / cols); ch = int((AREAH - gy * (rows - 1)) / rows)
    for i, it in enumerate(items):
        r, c = divmod(i, cols)
        x = int(X0 + (cw + gx) * c); y = int(Y0 + (ch + gy) * r)
        col = PALETTE[i % len(PALETTE)] if accent is None else accent
        col = PALETTE[i % len(PALETTE)]
        rect(s, x, y, cw, ch, LIGHT); rect(s, x, y, Inches(0.09), ch, col)
        if isinstance(it, tuple):
            txt(s, x + Inches(0.3), y + Inches(0.16), cw - Inches(0.55), ch - Inches(0.3),
                [[(it[0], size, col, True)], [(it[1], size - 3, INK, False)]], space=3)
        else:
            txt(s, x + Inches(0.3), y, cw - Inches(0.55), ch,
                [[(it, size, INK, False)]], anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s


def flow_h(title, steps, kicker=None, color=BLUE, note=None):
    s = head(slide(), title, kicker, kcolor=color)
    n = len(steps); X0 = Inches(0.85); TOTW = Inches(11.63); gap = Inches(0.34)
    cw = int((TOTW - gap * (n - 1)) / n); y = Inches(2.45); ch = Inches(3.15); bd = Inches(0.82)
    for i, st in enumerate(steps):
        x = int(X0 + (cw + gap) * i)
        rect(s, x, y, cw, ch, LIGHT); rect(s, x, y, cw, Inches(0.1), color)
        oval(s, int(x + cw / 2 - bd / 2), int(y + Inches(0.42)), bd, bd, color)
        txt(s, int(x + cw / 2 - bd / 2), int(y + Inches(0.42)), bd, bd,
            [[(str(i + 1), 30, WHITE, True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        txt(s, x + Inches(0.16), int(y + Inches(1.55)), cw - Inches(0.32), int(ch - Inches(1.7)),
            [[(st, 13, INK, False)]], align=PP_ALIGN.CENTER)
        if i < n - 1:
            txt(s, int(x + cw - Inches(0.04)), int(y + ch / 2 - Inches(0.3)),
                int(gap + Inches(0.08)), Inches(0.6),
                [[("▶", 15, color, True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    if note:
        txt(s, Inches(0.85), Inches(5.95), Inches(11.7), Inches(0.7), [[(note, 14, GREY, False)]],
            align=PP_ALIGN.CENTER)
    footer(s); return s


def trainer_slide(kicker, name, role, rows, initials, accent=BLUE):
    s = head(slide(), "About the Trainer", kicker, kcolor=accent)
    lx = Inches(0.85); lw = Inches(3.65)
    rect(s, lx, Inches(1.95), lw, Inches(4.7), LIGHT); rect(s, lx, Inches(1.95), lw, Inches(0.12), accent)
    bd = Inches(1.7); ax = int(lx + (lw - bd) / 2)
    oval(s, ax, Inches(2.5), bd, bd, accent)
    txt(s, ax, Inches(2.5), bd, bd, [[(initials, 44, WHITE, True)]],
        align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    txt(s, lx + Inches(0.15), Inches(4.55), lw - Inches(0.3), Inches(0.6),
        [[(name, 21, INK, True)]], align=PP_ALIGN.CENTER)
    txt(s, lx + Inches(0.15), Inches(5.2), lw - Inches(0.3), Inches(1.2),
        [[(role, 13, GREY, False)]], align=PP_ALIGN.CENTER)
    rx = Inches(4.9); rw = Inches(7.6); ry = Inches(1.95); rh = Inches(4.7)
    n = len(rows); gy = Inches(0.2); th = int((rh - gy * (n - 1)) / n)
    for i, (label, val) in enumerate(rows):
        y = int(ry + (th + gy) * i); col = PALETTE[i % len(PALETTE)]
        rect(s, rx, y, rw, th, LIGHT); rect(s, rx, y, Inches(0.1), th, col)
        vruns = [(val, 14, INK, False)] if val else \
                [("____________________________________________", 13, LINE, False)]
        txt(s, rx + Inches(0.32), y, rw - Inches(0.6), th,
            [[(label.upper(), 11, col, True)], vruns], anchor=MSO_ANCHOR.MIDDLE, space=3)
    footer(s); return s


def brk(kind, dur, color=AMBER):
    s = slide(); rect(s, 0, 0, SW, SH, WHITE)
    rect(s, 0, 0, SW, Inches(0.22), color)
    rect(s, Inches(5.4), Inches(2.35), Inches(2.53), Inches(0.1), color)
    txt(s, 0, Inches(2.75), SW, Inches(1.2), [[(kind, 48, INK, True)]], align=PP_ALIGN.CENTER)
    txt(s, 0, Inches(4.05), SW, Inches(0.8), [[(dur, 22, color, True)]], align=PP_ALIGN.CENTER)
    # Break slides carry the same footer as every other slide (house rule: every slide).
    footer(s)
    return s


def img_points(title, image, points, kicker=None, accent=BLUE, img_w=7.0, note=None):
    s = head(slide(), title, kicker, kcolor=accent)
    p = _asset(image)
    if p:
        w, h = _fit(p, img_w, 4.75)
        s.shapes.add_picture(p, Inches(0.85), Inches(2.05), width=w, height=h)
    rx = Inches(0.85) + Inches(img_w) + Inches(0.3); rw = Inches(12.48) - rx
    n = len(points); gy = Inches(0.2); th = int((Inches(4.75) - gy * (n - 1)) / n)
    for i, (t1, t2) in enumerate(points):
        y = int(Inches(2.05) + (th + gy) * i); col = PALETTE[i % len(PALETTE)]
        rect(s, rx, y, rw, th, LIGHT); rect(s, rx, y, Inches(0.09), th, col)
        txt(s, rx + Inches(0.28), y, rw - Inches(0.5), th,
            [[(t1, 14, col, True)], [(t2, 12, INK, False)]], anchor=MSO_ANCHOR.MIDDLE, space=3)
    if note:
        txt(s, Inches(0.85), Inches(6.9), Inches(11.7), Inches(0.4), [[(note, 12.5, GREY, False)]],
            align=PP_ALIGN.CENTER)
    footer(s); return s


def img_full(title, image, kicker=None, accent=BLUE, caption=None):
    s = head(slide(), title, kicker, kcolor=accent)
    p = _asset(image)
    maxh = 4.35 if caption else 4.85
    if p:
        w, h = _fit(p, 11.6, maxh)
        x = int(Inches(0.85) + (Inches(11.63) - w) / 2)
        s.shapes.add_picture(p, x, Inches(1.95), width=w, height=h)
    if caption:
        rect(s, Inches(0.85), Inches(6.45), Inches(11.63), Inches(0.62), LIGHT)
        txt(s, Inches(1.1), Inches(6.45), Inches(11.1), Inches(0.62), [[(caption, 14, INK, False)]],
            anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    footer(s); return s


def table_slide(title, headers, rows, kicker=None, accent=BLUE, widths=None, note=None, fsize=13):
    s = head(slide(), title, kicker, kcolor=accent)
    ncol = len(headers); X0 = Inches(0.85); TOTW = Inches(11.63)
    ws = [int(TOTW * w) for w in widths] if widths else [int(TOTW / ncol)] * ncol
    area_h = Inches(4.65) if note else Inches(4.85)
    nrow = len(rows) + 1; rh = int(area_h / nrow); y = Inches(1.95); x = X0
    for j, htxt in enumerate(headers):
        rect(s, x, y, ws[j], rh, accent)
        txt(s, x + Inches(0.14), y, ws[j] - Inches(0.24), rh, [[(htxt, fsize, WHITE, True)]],
            anchor=MSO_ANCHOR.MIDDLE)
        x += ws[j]
    for i, row in enumerate(rows):
        y = int(Inches(1.95) + rh * (i + 1)); x = X0
        fill = LIGHT if i % 2 == 0 else WHITE
        for j, cell in enumerate(row):
            rect(s, x, y, ws[j], rh, fill, line=LINE)
            txt(s, x + Inches(0.14), y, ws[j] - Inches(0.24), rh,
                [[(cell, fsize - 1, INK, j == 0)]], anchor=MSO_ANCHOR.MIDDLE)
            x += ws[j]
    if note:
        txt(s, Inches(0.85), Inches(6.62), Inches(11.7), Inches(0.4), [[(note, 13, GREY, False)]],
            align=PP_ALIGN.CENTER)
    footer(s); return s


def formula_slide(title, panels, kicker=None, accent=BLUE, note=None):
    s = head(slide(), title, kicker, kcolor=accent)
    n = len(panels); X0 = Inches(0.85); TOTW = Inches(11.63); gap = Inches(0.3)
    cw = int((TOTW - gap * (n - 1)) / n); y = Inches(2.1); ch = Inches(3.9)
    for i, (hd, formula, cap) in enumerate(panels):
        x = int(X0 + (cw + gap) * i); col = PALETTE[i % len(PALETTE)]
        rect(s, x, y, cw, ch, LIGHT); rect(s, x, y, cw, Inches(0.1), col)
        txt(s, x + Inches(0.22), y + Inches(0.28), cw - Inches(0.44), Inches(0.5),
            [[(hd, 16, col, True)]])
        rect(s, x + Inches(0.22), y + Inches(0.95), cw - Inches(0.44), Inches(1.35), NAVY)
        txt(s, x + Inches(0.32), y + Inches(0.95), cw - Inches(0.64), Inches(1.35),
            [[(ln, 15, CODEBLUE, True)] for ln in formula.split("\n")],
            anchor=MSO_ANCHOR.MIDDLE, space=3)
        txt(s, x + Inches(0.22), y + Inches(2.5), cw - Inches(0.44), ch - Inches(2.6),
            [[(cap, 12.5, GREY, False)]])
    if note:
        txt(s, Inches(0.85), Inches(6.25), Inches(11.7), Inches(0.6), [[(note, 14, GREY, False)]],
            align=PP_ALIGN.CENTER)
    footer(s); return s


def ncards(title, cards, kicker=None, accent=BLUE, cols=4, note=None, ch_in=None):
    """Outlined numbered concept cards — the reference's signature 4-across move.

    The title sits to the right of the badge and may wrap to two lines; the body
    starts BELOW whichever is taller, so a long title can never overlap the body.
    """
    s = head(slide(), title, kicker, kcolor=accent)
    n = len(cards); X0 = Inches(0.72); TOTW = Inches(11.85)
    gx = Inches(0.28) if cols > 2 else Inches(0.15)
    cw = int((TOTW - gx * (cols - 1)) / cols)
    rows = math.ceil(n / cols)
    areah = Inches(4.4) if note else Inches(4.75)
    gy = Inches(0.25)
    ch = Inches(ch_in) if ch_in else int((areah - gy * (rows - 1)) / rows)
    # card title column width, in characters, drives the wrap estimate
    title_w_in = (cw - Inches(1.0)) / 914400
    for i, (t1, t2) in enumerate(cards):
        r, c = divmod(i, cols)
        x = int(X0 + (cw + gx) * c); y = int(Inches(1.95) + (ch + gy) * r)
        col = PALETTE[i % len(PALETTE)]
        rect(s, x, y, cw, ch, LIGHT); rect(s, x, y, Inches(0.09), ch, col)
        bd = Inches(0.46)
        oval(s, x + Inches(0.24), y + Inches(0.20), bd, bd, col)
        txt(s, x + Inches(0.24), y + Inches(0.20), bd, bd, [[(str(i + 1), 15, WHITE, True)]],
            align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # ~ 9.5 chars per inch at 14pt Arial bold
        est_lines = max(1, math.ceil(len(t1) / max(6, title_w_in * 9.5)))
        thh = Inches(0.30) * est_lines
        txt(s, x + Inches(0.82), y + Inches(0.16), cw - Inches(1.0), thh,
            [[(t1, 14, col, True)]])
        body_y = y + Inches(0.16) + max(thh, Inches(0.50)) + Inches(0.16)
        txt(s, x + Inches(0.28), body_y, cw - Inches(0.54),
            y + ch - body_y - Inches(0.14), [[(t2, 11.5, INK, False)]])
    if note:
        rect(s, Inches(0.72), Inches(6.42), Inches(11.85), Inches(0.62), LIGHT)
        txt(s, Inches(1.0), Inches(6.42), Inches(11.3), Inches(0.62), [[(note, 13, INK, False)]],
            anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s


def takeaway(s, text, color=BLUE, y=6.35):
    """One bolded boxed rule to remember — closes a concept slide."""
    rect(s, Inches(0.85), Inches(y), Inches(11.63), Inches(0.62), LIGHT)
    rect(s, Inches(0.85), Inches(y), Inches(0.09), Inches(0.62), color)
    txt(s, Inches(1.15), Inches(y), Inches(11.2), Inches(0.62), [[(text, 13.5, INK, True)]],
        anchor=MSO_ANCHOR.MIDDLE)


def activity_slide(a):
    col = CMAP[a["accent"]]
    s = head(slide(), a["title"], f"ACTIVITY {a['n']} · CASE STUDY", kcolor=col)
    rect(s, Inches(10.35), Inches(0.5), Inches(2.13), Inches(0.62), col)
    txt(s, Inches(10.35), Inches(0.5), Inches(2.13), Inches(0.62),
        [[(f"ACTIVITY {a['n']} · {a['minutes']} MIN", 11, WHITE, True)]],
        align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # org + scenario
    rect(s, Inches(0.85), Inches(1.95), Inches(11.63), Inches(1.32), LIGHT)
    rect(s, Inches(0.85), Inches(1.95), Inches(0.09), Inches(1.32), col)
    txt(s, Inches(1.15), Inches(2.06), Inches(11.2), Inches(0.4), [[(a["org"], 13, col, True)]])
    txt(s, Inches(1.15), Inches(2.44), Inches(11.2), Inches(0.8),
        [[(a["scenario"], 13.5, INK, False)]])
    # 5 chips
    n = len(a["flow"]); X0 = Inches(0.85); TOTW = Inches(11.63); gap = Inches(0.22)
    cw = int((TOTW - gap * (n - 1)) / n); y = Inches(3.5); ch = Inches(1.25); bd = Inches(0.56)
    for i, st in enumerate(a["flow"]):
        x = int(X0 + (cw + gap) * i)
        rect(s, x, y, cw, ch, WHITE, line=LINE)
        oval(s, int(x + cw / 2 - bd / 2), y + Inches(0.14), bd, bd, col)
        txt(s, int(x + cw / 2 - bd / 2), y + Inches(0.14), bd, bd, [[(str(i + 1), 15, WHITE, True)]],
            align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        txt(s, x + Inches(0.1), y + Inches(0.76), cw - Inches(0.2), Inches(0.45),
            [[(st, 10.5, INK, False)]], align=PP_ALIGN.CENTER)
        if i < n - 1:
            txt(s, int(x + cw), int(y + ch / 2 - Inches(0.22)), int(gap), Inches(0.44),
                [[("▶", 12, col, True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # discussion questions
    rect(s, Inches(0.85), Inches(4.95), Inches(7.6), Inches(1.42), WHITE, line=LINE)
    txt(s, Inches(1.1), Inches(5.02), Inches(7.2), Inches(0.32),
        [[("DISCUSSION QUESTIONS", 10.5, col, True)]])
    bullets(s, Inches(1.1), Inches(5.32), Inches(7.15), Inches(1.0), a["questions"],
            size=10.5, gap=3)
    # produce band
    rect(s, Inches(8.65), Inches(4.95), Inches(3.83), Inches(1.42), LIGHT)
    rect(s, Inches(8.65), Inches(4.95), Inches(0.09), Inches(1.42), TEAL)
    txt(s, Inches(8.92), Inches(5.02), Inches(3.4), Inches(0.32),
        [[("YOU'LL PRODUCE", 10.5, TEAL, True)]])
    txt(s, Inches(8.92), Inches(5.32), Inches(3.45), Inches(1.0), [[(a["produce"], 11.5, INK, False)]])
    # meta
    txt(s, Inches(0.85), Inches(6.5), Inches(11.63), Inches(0.4),
        [[(f"Assesses {a['ka']}  ·  Activity pack: activities/activity-{a['n']}/  "
           f"·  Full step-by-step facilitation detail: Learner Guide", 11.5, GREY, False)]])
    footer(s); return s


def lms_slide():
    s = head(slide(), "Download Course Material", kicker="COURSE PORTAL · LMS/TMS", kcolor=BLUE)
    bx, by, bw, bh = Inches(0.85), Inches(2.0), Inches(6.1), Inches(4.55)
    rect(s, bx, by, bw, bh, WHITE, line=LINE)
    rect(s, bx, by, bw, Inches(0.52), RGBColor(0xEE, 0xF2, 0xF8))
    for i, c in enumerate([RED, AMBER, TEAL]):
        oval(s, int(bx + Inches(0.18) + Inches(0.28) * i), int(by + Inches(0.17)),
             Inches(0.18), Inches(0.18), c)
    rect(s, int(bx + Inches(1.2)), int(by + Inches(0.1)), int(bw - Inches(1.5)), Inches(0.34),
         WHITE, line=LINE)
    txt(s, int(bx + Inches(1.35)), int(by + Inches(0.1)), int(bw - Inches(1.8)), Inches(0.34),
        [[("https://lms-tms.tertiaryinfotech.com", 13, BLUE, True)]], anchor=MSO_ANCHOR.MIDDLE)
    shot = _asset("lms-tms-login.png")
    if shot:
        w, h = _fit(shot, 5.6, 3.55)
        x = int(bx + (bw - w) / 2)
        s.shapes.add_picture(shot, x, int(by + Inches(0.72)), width=w, height=h)
    steps = [("Sign in", "lms-tms.tertiaryinfotech.com — log in with your registered email (OTP or password)."),
             ("Open your course", f"Select '{C.TITLE}' under My Courses."),
             ("Download materials", "Trainer slides and the Learner Guide — your open-book references."),
             ("Submit & survey", "Upload your assessment answers and complete the TRAQOM survey.")]
    rx = Inches(7.3); rw = Inches(5.2); gy = Inches(0.2); th = int((Inches(4.55) - gy * 3) / 4)
    for i, (t1, t2) in enumerate(steps):
        y = int(Inches(2.0) + (th + gy) * i); col = PALETTE[i % 4]
        rect(s, rx, y, rw, th, LIGHT); rect(s, rx, y, Inches(0.09), th, col)
        bd = Inches(0.5)
        oval(s, rx + Inches(0.2), int(y + th / 2 - bd / 2), bd, bd, col)
        txt(s, rx + Inches(0.2), int(y + th / 2 - bd / 2), bd, bd, [[(str(i + 1), 16, WHITE, True)]],
            align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        txt(s, rx + Inches(0.9), y, rw - Inches(1.1), th,
            [[(t1, 14, col, True)], [(t2, 11.5, INK, False)]], anchor=MSO_ANCHOR.MIDDLE, space=2)
    txt(s, Inches(0.85), Inches(6.6), Inches(11.7), Inches(0.4),
        [[("All course material is downloaded from the LMS/TMS portal — keep it handy: "
           "the final assessment is open book.", 13, GREY, False)]], align=PP_ALIGN.CENTER)
    footer(s); return s


def attendance_slide(kicker="TRAQOM · SSG DIGITAL ATTENDANCE"):
    return content("Digital Attendance (Mandatory)", [
        "It is mandatory to take the AM, PM and Assessment digital attendance for WSQ-funded courses.",
        "The trainer or administrator displays the digital attendance QR code from the SSG portal.",
        "Scan the QR code with your mobile phone camera and submit your attendance.",
        "A minimum of 75% attendance is required to be eligible for assessment and funding.",
        "Complete the TRAQOM survey at the end of the course — it is required for funding.",
    ], kicker=kicker)


# ================================================================ BUILD
cover()

# ---------------- ADMIN (front) ----------------
mark("admin")
section("COURSE ADMINISTRATION", "Welcome & Housekeeping", "00")
attendance_slide()
trainer_slide("YOUR TRAINER · GENERAL", "Your Trainer",
              "General Trainer template —\nto be completed by the trainer",
              [("Name", ""), ("Title / Designation", ""), ("Qualifications", ""),
               ("Areas of expertise", ""), ("Training & industry experience", ""), ("Contact", "")],
              initials="?", accent=GREY)
trainer_slide("YOUR TRAINER", C.TRAINER, "Principal Trainer\nTertiary Infotech Pte Ltd",
              [("Role", "Principal Trainer, Tertiary Infotech Pte Ltd"),
               ("Background", "PhD — 20+ years across AI, cybersecurity, data science and enterprise IT."),
               ("Delivers", "WSQ courses on generative AI, AI security, AI governance and data analytics."),
               ("Founder", "Founder and lead instructor at Tertiary Infotech / Tertiary Courses.")],
              initials="AA", accent=BLUE)
content("Let's Know Each Other", [
    "Your name, organisation and role.",
    "Any generative AI or AI agent systems already live in your organisation.",
    "One AI security question you want answered by the end of Day 2.",
], kicker="ICE-BREAKER")
tile_grid("Ground Rules", [
    "Set your mobile phone to silent mode.",
    "Participate actively — no question is too small.",
    "Mutual respect: agree to disagree.",
    "One conversation at a time.",
    "Be punctual; return from breaks on time.",
    "75% attendance is required for funding.",
], kicker="HOUSEKEEPING", cols=2, size=15)
lms_slide()

table_slide("Skills Framework Alignment",
            ["TSC element", "Detail"],
            [["TSC Title", C.TSC_TITLE],
             ["TSC Code", C.TSC_CODE],
             ["Proficiency Level", C.PROFICIENCY],
             ["Knowledge statements", "K1–K5 — assessed by the Written Assessment"],
             ["Ability statements", "A1–A5 — assessed by the Case Study"]],
            kicker="WSQ ALIGNMENT", widths=[0.28, 0.72], fsize=14,
            note="This course delivers the accredited TSC through an AI security lens.")

table_slide("Learning Outcomes",
            ["LO", "Learning Outcome", "Assessed by"],
            [["LO1", C.LEARNING_OUTCOMES[0][1], "WA · Case Study"],
             ["LO2", C.LEARNING_OUTCOMES[1][1], "WA · Case Study"],
             ["LO3", C.LEARNING_OUTCOMES[2][1], "WA · Case Study"]],
            kicker="WHAT YOU WILL ACHIEVE", widths=[0.08, 0.68, 0.24], fsize=13)

table_slide("Knowledge Statements (K)",
            ["Code", "Knowledge statement"],
            [[c, d] for c, d in C.TSC_KNOWLEDGE],
            kicker="ASSESSED BY THE WRITTEN ASSESSMENT", widths=[0.09, 0.91], fsize=13,
            note="One written assessment question per knowledge statement.")

table_slide("Ability Statements (A)",
            ["Code", "Ability statement"],
            [[c, d] for c, d in C.TSC_ABILITIES],
            kicker="ASSESSED BY THE CASE STUDY", widths=[0.09, 0.91], fsize=13,
            accent=VIOLET,
            note="The case study covers every ability statement across three questions.")

two_col("Lesson Plan — Day 1", [
    ("Morning (AM attendance)", 0, True),
    ("Welcome, introductions, learning outcomes", 1),
    ("LU1 T1: The AI security threat landscape", 1),
    ("LU1 T2: Generative vs discriminative — the guardrail pattern", 1),
    ("Tea break", 1),
    ("LU1 T3: Application modes as attack surfaces", 1),
    ("Activity 1: Threat Modelling a GenAI Concierge (45 min)", 1),
    ("Lunch break 12:30–1:30pm", 1)],
    [("Afternoon (PM attendance)", 0, True),
     ("LU2 T1: Data quality, poisoning and supply chain integrity", 1),
     ("LU2 T2: Prompt injection — direct, indirect, cross-modal", 1),
     ("Tea break", 1),
     ("Activity 2: Prompt Injection & the PDPA Leak (60 min)", 1),
     ("Day 1 recap and Q&A", 1)],
    kicker="SCHEDULE · DAY 1", lhead="Morning — foundations", rhead="Afternoon — the prompt layer",
    note="8 instructional hours · 9:30am–6:30pm · 1-hour lunch · tea breaks counted within.")

two_col("Lesson Plan — Day 2", [
    ("Morning (AM attendance)", 0, True),
    ("LU2 T3: Security frameworks for GenAI and agents", 1),
    ("LU2 T4: Measuring guardrails — adversarial testing", 1),
    ("Tea break", 1),
    ("Activity 3: Selecting a Security Framework (60 min)", 1),
    ("Lunch break 12:45–1:45pm", 1)],
    [("Afternoon (PM attendance)", 0, True),
     ("LU3 T1: Agent anatomy, excessive agency, destructive execution", 1),
     ("Activity 4: Rogue Agent Post-Incident Review (60 min)", 1),
     ("LU3 T2: PDPA, PDPC and IMDA agentic governance", 1),
     ("LU3 T3: Misinformation, bias and limitations", 1),
     ("Activity 5: Agent Governance & Deployment Gate (25 min)", 1),
     ("Briefing for Assessment · WA + Case Study · TRAQOM", 1)],
    kicker="SCHEDULE · DAY 2", lhead="Morning — frameworks & measurement",
    rhead="Afternoon — agents, governance, assessment",
    note="8 instructional hours · 9:30am–6:30pm · assessment held at the end of Day 2.")

# ---------------- DAY 1 ----------------
mark("day1")
section("DAY 1 · LEARNING UNIT 1", "Foundations of AI Security", "01",
        "Why generative AI breaks the security assumptions you already rely on")

img_points("The governance gap", "diagram-incident-landscape.png",
           [("Deployed faster than governed",
             "57% of organisations run self-hosted agents; most have no inventory of them."),
            ("Prompt injection dominates",
             "The single largest source of reported GenAI and agent incidents."),
            ("Excessive agency is rising",
             "Mainstream agent deployment moved LLM03 up three places in 2026."),
            ("Monitoring is the biggest gap",
             "71% have no runtime monitoring of what their agents actually do.")],
           kicker="LU1 · T1 · WHERE WE ARE", accent=RED, img_w=6.9)

s = ncards("Why GenAI breaks classical security", D.LU1_WHY_DIFFERENT,
           kicker="LU1 · T1 · K2", accent=RED, cols=4,
           note="Classical AppSec assumes code and data are separable. A language model is the "
                "counter-example: its data IS its instructions.")

big_statement(D.BIG_STATEMENTS[0]["l1"], D.BIG_STATEMENTS[0]["l2"],
              D.BIG_STATEMENTS[0]["kicker"], color=RED)

img_full("The context window has no trust boundary", "diagram-trust-boundary.png",
         kicker="LU1 · T1 · K2", accent=RED,
         caption="Every source becomes one flat token sequence. The model cannot tell an "
                 "instruction from data — which is why LLM01 has no complete fix.")

two_col("Generative vs discriminative models",
        D.LU1_GEN_VS_DISC["left"], D.LU1_GEN_VS_DISC["right"],
        kicker="LU1 · T2 · K3", lhead="Generative — what we secure",
        rhead="Discriminative — what does the policing",
        lcolor=RED, rcolor=BLUE, note=D.LU1_GEN_VS_DISC["note"])

s = table_slide("Application modes are attack surfaces",
                D.LU1_APP_SURFACES[0], D.LU1_APP_SURFACES[1:],
                kicker="LU1 · T3 · A4", accent=VIOLET, widths=[0.17, 0.28, 0.38, 0.17],
                note="Every capability you add is a capability an attacker can aim at.")

img_full("OWASP Top 10 for LLM Applications — 2026", "diagram-owasp-llm-top10.png",
         kicker="LU1 · T3 · THE REFERENCE TAXONOMY", accent=BLUE,
         caption="Released August 2026. Ranking now weights 7,714 real incidents — "
                 "evidence, not only practitioner opinion.")

activity_slide(D.ACTIVITIES[0])
brk("Lunch Break", "12:30pm – 1:30pm")

# LU2 — prompt layer
mark("lu2")
section("DAY 1 · LEARNING UNIT 2", "Attacking and Defending the Prompt Layer", "02",
        "Injection, poisoning and the limits of prompt-based defence")

ncards("Three kinds of prompt injection",
       [(t, d.replace("\n", " ") + "\n\n→ " + n) for t, d, n, _ in D.LU2_INJECTION_TYPES],
       kicker="LU2 · T2 · K4", accent=RED, cols=3, ch_in=3.3,
       note="Indirect injection is the one that matters in production: the attacker never "
            "touches your interface, only the content your system chooses to read.")

ncards("Why prompt-based defences fail", D.LU2_WHY_PROMPTS_FAIL,
       kicker="LU2 · T2 · K4", accent=RED, cols=4,
       note="Defensive prompting raises the attacker's cost. It never closes the hole. "
            "Treat it as friction, never as a boundary.")

table_slide("Poisoning — five vectors, one idea",
            D.LU2_POISONING[0], D.LU2_POISONING[1:],
            kicker="LU2 · T1 · K1", accent=AMBER, widths=[0.18, 0.28, 0.36, 0.18],
            note="Data quality is a security property. Whoever can write to your corpus "
                 "can write to your model's behaviour.")

activity_slide(D.ACTIVITIES[1])
content("Day 1 Recap", [
    "Prompt injection is architectural — the context window has no trust boundary.",
    "Guardrail classifiers are discriminative models policing a generative one: useful, fallible.",
    "Every application mode — summarise, infer, transform, augment — is an attack surface.",
    "Data quality is a security property: poisoning reaches training, RAG, memory and artifacts.",
    "Tomorrow: the system stops answering and starts acting.",
], kicker="DAY 1 · CLOSE", size=18)

# ---------------- DAY 2 ----------------
mark("day2")
section("DAY 2 · LEARNING UNIT 2 (cont.)", "Frameworks and Measurement", "03",
        "Choosing the right instrument, and proving the control works")

img_full("No single framework is sufficient", "diagram-framework-stack.png",
         kicker="LU2 · T3 · A3", accent=TEAL,
         caption="Each framework answers a different question. Combine them deliberately — "
                 "a threat taxonomy is not a process, and a process is not a legal obligation.")

table_slide("What each framework is — and is not",
            D.FRAMEWORK_ROLES[0], D.FRAMEWORK_ROLES[1:],
            kicker="LU2 · T3 · A3", accent=TEAL, widths=[0.30, 0.44, 0.26], fsize=12.5)

img_full("OWASP Top 10 for Agentic Applications — 2026", "diagram-owasp-asi-top10.png",
         kicker="LU2 · T3 · THE AGENT TAXONOMY", accent=VIOLET,
         caption="The agent-specific companion to the LLM list. Where the LLM list asks what the "
                 "model says, the ASI list asks what the agent does.")

formula_slide("Measuring whether a guardrail works", D.MEASUREMENT_PANELS,
              kicker="LU2 · T4 · A5", accent=BLUE,
              note="Report all three together. Any one of them alone can be gamed.")

ncards("Reading red-team results honestly", [
    ("Never read the average",
     "An aggregate attack-success rate hides the one attack family that succeeds every "
     "single time. Report per family."),
    ("Refusal rate needs a partner",
     "A falling refusal rate is not progress if the false-positive rate fell with it. "
     "You may have simply loosened the guardrail."),
    ("Vary the phrasing",
     "Test the same attack across prompt variants. A defence that holds against one "
     "phrasing is not a defence — it is a coincidence."),
    ("Re-test after every update",
     "The vendor can change model behaviour overnight. Your last red-team result "
     "expires when the model does."),
], kicker="LU2 · T4 · A5", accent=BLUE, cols=4,
   note="Publish the residual risk. A go-live gate with no stated risk tolerance is not a gate.")

activity_slide(D.ACTIVITIES[2])
brk("Lunch Break", "12:45pm – 1:45pm")

# LU3 — agents
mark("lu3")
section("DAY 2 · LEARNING UNIT 3", "Agent Autonomy, Governance and Compliance", "04",
        "When the system stops answering and starts acting")

big_statement(D.BIG_STATEMENTS[1]["l1"], D.BIG_STATEMENTS[1]["l2"],
              D.BIG_STATEMENTS[1]["kicker"], color=VIOLET)

img_full("An agent is a model plus a loop plus tools", "diagram-agent-anatomy.png",
         kicker="LU3 · T1 · K5", accent=VIOLET,
         caption="Each component adds a distinct attack surface. Autonomy is not a feature "
                 "of the model — it is a property of the architecture around it.")

table_slide("Agent capabilities and their risks",
            D.AGENT_CAPABILITY_RISK[0], D.AGENT_CAPABILITY_RISK[1:],
            kicker="LU3 · T1 · K5", accent=VIOLET, widths=[0.18, 0.28, 0.32, 0.22])

img_full("Agent kill chain — a real 2026 incident", "diagram-kill-chain.png",
         kicker="LU3 · T1 · K5 · CASE STUDY", accent=RED,
         caption="OpenAI → Hugging Face, July 2026. No malware, no known CVE. "
                 "The chain was assembled entirely from individually legitimate actions.")

content("What the 2026 incidents actually proved", [
    "Agents pursue goals across obstacles: a permission denial is read as a failed method, not a stop sign.",
    "Agents target other AI systems — prompt injection hidden in an HTML comment for a coding assistant.",
    "Anthropic's evaluations: a model published malicious code to PyPI that ran on 15 real systems.",
    "One model scanned ~9,000 targets and stopped only when it recognised the target was real.",
    "Replit: an agent deleted the production customer database — ASI10, in one irreversible step.",
], kicker="LU3 · T1 · K5", size=16, kcolor=RED)

img_full("Defence in depth — four layers", "diagram-defence-layers.png",
         kicker="LU3 · T1 · MICROSOFT'S MODEL", accent=TEAL,
         caption="Each layer fails differently — that is precisely why you need all four. "
                 "The application layer is the one you fully control.")

ncards("Four design patterns for safe agents", D.MS_DESIGN_PATTERNS,
       kicker="LU3 · T1 · CONTROLS", accent=TEAL, cols=4,
       note="Notice what none of these are: a better prompt. Every one is an architectural decision.")

ncards("The four-layer control stack",
       [(t, d) for t, d, _ in D.CONTROL_STACK],
       kicker="LU3 · T1 · CONTROLS", accent=BLUE, cols=4,
       note="Identity first. You cannot apply least privilege to an agent that has no distinct identity.")

activity_slide(D.ACTIVITIES[3])

# governance & compliance
big_statement(D.BIG_STATEMENTS[2]["l1"], D.BIG_STATEMENTS[2]["l2"],
              D.BIG_STATEMENTS[2]["kicker"], color=TEAL)

img_full("Calibrating autonomy — the deterministic gate", "diagram-autonomy-gate.png",
         kicker="LU3 · T2 · A2", accent=TEAL,
         caption="IMDA: structural safeguards are preferred over prompt-based controls, and "
                 "approval checkpoints are required for irreversible actions.")

ncards("IMDA Model AI Governance for Agentic AI", D.IMDA_DIMENSIONS,
       kicker="LU3 · T2 · A2 · SINGAPORE", accent=TEAL, cols=4,
       note="Published January 2026 — the world's first governance framework written "
            "specifically for agentic AI. Some use cases are unsuitable for agents entirely.")

img_full("PDPA accountability in the AI value chain", "diagram-pdpa-roles.png",
         kicker="LU3 · T2 · A2 · SINGAPORE", accent=RED,
         caption="PDPC GenAI Guidelines, July 2026. The system deployer carries primary "
                 "responsibility — you cannot contract it away to the model vendor.")

table_slide("PDPA obligations for an AI deployment",
            D.PDPA_DUTIES[0], D.PDPA_DUTIES[1:],
            kicker="LU3 · T2 · A2", accent=RED, widths=[0.26, 0.74], fsize=12.5)

ncards("Bias, limits and misinformation", D.BIAS_LIMITS,
       kicker="LU3 · T3 · A1", accent=AMBER, cols=4,
       note="LLM07 rose in 2026 because a confident wrong answer that drives a tool call "
            "is no longer a quality problem — it is a security failure.")

activity_slide(D.ACTIVITIES[4])

# ---------------- CLOSE ----------------
mark("close")
section("COURSE CLOSE", "Synthesis and Assessment", "05")

ncards("Four principles to take back to work", D.CLOSING_PRINCIPLES,
       kicker="SYNTHESIS", accent=BLUE, cols=4,
       note="If you remember one thing: security for AI systems is an architecture problem "
            "wearing a prompt-engineering costume.")

content("Summary & Q&A", [
    "LU1: Generative AI breaks classical assumptions — input is executable, output drives action.",
    "LU2: Prompt injection and poisoning are architectural; defensive prompting is friction, not a boundary.",
    "LU2: Frameworks are instruments — OWASP, NIST, ATLAS, IMDA and the PDPA each answer a different question.",
    "LU3: An agent is a model plus a loop plus tools; autonomy multiplies every earlier risk.",
    "LU3: Accountability is Singapore law — the system deployer answers for what the agent does.",
], kicker="WHAT WE COVERED", size=17)

# Briefing BEFORE assessment (house rule)
content("Briefing for Assessment", [
    "Two instruments: a Written Assessment (SAQ) and a Case Study.",
    "Written Assessment: 5 short-answer questions — one for each knowledge statement K1–K5.",
    "Case Study: 3 questions — one per Learning Outcome, covering ability statements A1–A5.",
    "Format: open book. You may use the slides, the Learner Guide and your activity notes.",
    "Grading: Competent / Not Yet Competent. Re-assessment is available if you are NYC.",
    "Answer in your own words — reproducing slide text verbatim does not evidence competence.",
], kicker="BEFORE YOU BEGIN", size=17, kcolor=AMBER)

table_slide("Assessment",
            ["Instrument", "Covers", "Detail"],
            [["Written Assessment (SAQ)", "K1 – K5", C.ASSESSMENT["wa"]],
             ["Case Study", "A1 – A5 via LO1–LO3", C.ASSESSMENT["cs"]],
             ["Format", "—", C.ASSESSMENT["format"]],
             ["Grading", "—", C.ASSESSMENT["grading"]]],
            kicker="ASSESSMENT OVERVIEW", widths=[0.24, 0.20, 0.56], fsize=13)

img_full("Assessment Flow", "diagram-assessment-flow.png",
         kicker="HOW YOU WILL BE ASSESSED", accent=BLUE,
         caption="Both instruments must be completed. Your assessor confirms the outcome "
                 "with you and both parties sign off.")

content("Support", [
    "Email: enquiry@tertiaryinfotech.com",
    "Tel: +65 6318 4588",
    "Website: www.tertiarycourses.com.sg",
    "LMS/TMS: https://lms-tms.tertiaryinfotech.com",
], kicker="AFTER THE COURSE", size=18)

attendance_slide(kicker="TRAQOM · DIGITAL ATTENDANCE · END OF COURSE")


# Thank You
s = slide(); rect(s, 0, 0, SW, SH, WHITE)
rect(s, 0, 0, SW, Inches(0.22), BLUE); rect(s, 0, Inches(7.28), SW, Inches(0.22), RED)
txt(s, 0, Inches(2.9), SW, Inches(1.3), [[("Thank You!", 54, INK, True)]], align=PP_ALIGN.CENTER)
rect(s, Inches(5.4), Inches(4.35), Inches(2.53), Inches(0.08), RED)
txt(s, 0, Inches(4.7), SW, Inches(0.8),
    [[(C.TITLE, 20, GREY, False)]], align=PP_ALIGN.CENTER)
txt(s, 0, Inches(5.25), SW, Inches(0.6),
    [[(f"{C.COURSE_CODE}  ·  Tertiary Infotech Pte Ltd  ·  UEN 20120096W", 13, GREY, False)]],
    align=PP_ALIGN.CENTER)
PAGE["n"] += 1

# ---------------- save ----------------
out = os.path.join(OUTDIR, f"WSQ - Master Trainer Slides - {C.COURSE_CODE} - {C.TITLE}-v{C.VERSION.replace('.','')}.pptx")
prs.save(out)
with open(os.path.join(OUTDIR, "slide_map.json"), "w") as f:
    json.dump(SLIDE_MAP, f, indent=2)
print(f"Saved: {out}")
print(f"Slides: {PAGE['n']}")
print("Slide map:", SLIDE_MAP)
