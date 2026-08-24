#!/usr/bin/env python3
"""Build same-folder PDFs for every activity Markdown file plus one full-pack PDF.

The activity Markdown remains the editable source. This builder intentionally uses only
ReportLab so the PDFs can be regenerated without browser or Pandoc dependencies.
"""

from __future__ import annotations

import html
import os
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

import course_data as C


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
ACTIVITIES = ROOT / "activities"
BLUE = colors.HexColor("#1F6FEB")
NAVY = colors.HexColor("#111827")
GREY = colors.HexColor("#5B6372")
LIGHT = colors.HexColor("#F5F8FC")
LINE = colors.HexColor("#DCE3EC")
RED = colors.HexColor("#DC2626")


def ascii_safe(text: str) -> str:
    replacements = {
        "\u2014": " - ", "\u2013": " - ", "\u2011": "-", "\u2010": "-",
        "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
        "\u2026": "...", "\u2022": "-", "\u2192": "->", "\u00d7": "x",
        "\u00f7": "/", "\u2248": "about ", "\u00b7": " | ", "\u00a0": " ",
        "\u2713": "PASS", "\u2717": "FAIL",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def inline(text: str) -> str:
    text = ascii_safe(text.strip())
    text = html.escape(text, quote=False)
    text = re.sub(r"!\[([^]]*)\]\([^)]+\)", r"[Image: \1]", text)
    text = re.sub(r"\[([^]]+)\]\((https?://[^)]+)\)", r'<link href="\2" color="#1F6FEB">\1</link>', text)
    text = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    return text


styles = getSampleStyleSheet()
BODY = ParagraphStyle("Body", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.0,
                      leading=11.6, textColor=NAVY, spaceAfter=3.5)
H1 = ParagraphStyle("H1", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=18,
                    leading=22, textColor=NAVY, spaceBefore=10, spaceAfter=8)
H2 = ParagraphStyle("H2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=14,
                    leading=17, textColor=BLUE, spaceBefore=8, spaceAfter=5)
H3 = ParagraphStyle("H3", parent=styles["Heading3"], fontName="Helvetica-Bold", fontSize=11.3,
                    leading=13.5, textColor=NAVY, spaceBefore=6, spaceAfter=3)
BULLET = ParagraphStyle("Bullet", parent=BODY, leftIndent=13, firstLineIndent=-8, bulletIndent=4)
QUOTE = ParagraphStyle("Quote", parent=BODY, leftIndent=12, rightIndent=8, borderColor=BLUE,
                       borderWidth=1, borderPadding=7, backColor=LIGHT, textColor=NAVY)
CODE = ParagraphStyle("Code", parent=BODY, fontName="Courier", fontSize=7.8, leading=10,
                      leftIndent=6, rightIndent=6, borderColor=LINE, borderWidth=0.5,
                      borderPadding=6, backColor=colors.HexColor("#0B1220"),
                      textColor=colors.HexColor("#E5F2FF"))
SMALL = ParagraphStyle("Small", parent=BODY, fontSize=7.4, leading=9.2)


def table_flow(lines: list[str], width: float):
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells):
            continue
        rows.append(cells)
    if not rows:
        return []
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    pdata = [[Paragraph(inline(c), SMALL) for c in row] for row in rows]
    weights = []
    for j in range(ncol):
        longest = max(8, min(45, max(len(ascii_safe(r[j])) for r in rows)))
        weights.append(longest)
    total = sum(weights)
    col_widths = [width * w / total for w in weights]
    t = Table(pdata, colWidths=col_widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return [t, Spacer(1, 5)]


def markdown_flow(text: str, width: float):
    lines = text.splitlines()
    story = []
    paragraph = []
    in_code = False
    code_lines = []
    i = 0

    def flush_paragraph():
        if paragraph:
            story.append(Paragraph(inline(" ".join(x.strip() for x in paragraph)), BODY))
            paragraph.clear()

    while i < len(lines):
        raw = lines[i].rstrip()
        stripped = raw.strip()
        if stripped.startswith("```"):
            flush_paragraph()
            if in_code:
                story.append(Preformatted(ascii_safe("\n".join(code_lines)), CODE))
                code_lines = []
                in_code = False
            else:
                in_code = True
            i += 1
            continue
        if in_code:
            code_lines.append(raw)
            i += 1
            continue
        if stripped.startswith("|") and i + 1 < len(lines) and lines[i + 1].strip().startswith("|"):
            flush_paragraph()
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i])
                i += 1
            story.extend(table_flow(block, width))
            continue
        if not stripped:
            flush_paragraph()
        elif stripped == "---":
            flush_paragraph()
            story.append(Spacer(1, 5))
        elif stripped.startswith("### "):
            flush_paragraph(); story.append(Paragraph(inline(stripped[4:]), H3))
        elif stripped.startswith("## "):
            flush_paragraph(); story.append(Paragraph(inline(stripped[3:]), H2))
        elif stripped.startswith("# "):
            flush_paragraph(); story.append(Paragraph(inline(stripped[2:]), H1))
        elif stripped.startswith("> "):
            flush_paragraph(); story.append(Paragraph(inline(stripped[2:]), QUOTE))
        elif re.match(r"^[-*] ", stripped):
            flush_paragraph()
            item = re.sub(r"^[-*] ", "", stripped)
            story.append(Paragraph(inline(item), BULLET, bulletText="-"))
        elif re.match(r"^\d+\. ", stripped):
            flush_paragraph()
            m = re.match(r"^(\d+)\.\s+(.*)", stripped)
            story.append(Paragraph(inline(m.group(2)), BULLET, bulletText=m.group(1) + "."))
        else:
            paragraph.append(raw)
        i += 1
    flush_paragraph()
    if in_code and code_lines:
        story.append(Preformatted(ascii_safe("\n".join(code_lines)), CODE))
    return story


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.line(18 * mm, 14 * mm, 192 * mm, 14 * mm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(18 * mm, 9 * mm, f"{C.SHORT_TITLE} | {C.COURSE_CODE} | Version {C.VERSION}")
    canvas.drawRightString(192 * mm, 9 * mm, f"Page {doc.page}")
    canvas.restoreState()


def cover_story(activity_title: str, subtitle: str):
    return [
        Spacer(1, 30 * mm),
        Paragraph("ACTIVITY PACK", ParagraphStyle("K", parent=H2, alignment=TA_CENTER, textColor=RED)),
        Spacer(1, 8 * mm),
        Paragraph(inline(activity_title), ParagraphStyle("Cover", parent=H1, alignment=TA_CENTER,
                  fontSize=25, leading=30, textColor=NAVY)),
        Spacer(1, 8 * mm),
        Paragraph(inline(subtitle), ParagraphStyle("Sub", parent=BODY, alignment=TA_CENTER,
                  fontSize=12, leading=16, textColor=GREY)),
        Spacer(1, 18 * mm),
        Table([
            [Paragraph("Course", SMALL), Paragraph(inline(C.TITLE), SMALL)],
            [Paragraph("Course code", SMALL), Paragraph(C.COURSE_CODE, SMALL)],
            [Paragraph("Version", SMALL), Paragraph(f"{C.VERSION} | {C.VERSION_DATE}", SMALL)],
        ], colWidths=[35 * mm, 105 * mm], style=TableStyle([
            ("BACKGROUND", (0, 0), (0, -1), BLUE),
            ("TEXTCOLOR", (0, 0), (0, -1), colors.white),
            ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.5, LINE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ])),
        Spacer(1, 28 * mm),
        Paragraph("Tertiary Infotech Pte Ltd | UEN 201200696W",
                  ParagraphStyle("Org", parent=BODY, alignment=TA_CENTER, textColor=GREY)),
    ]


def build_pdf(output: Path, title: str, subtitle: str, sources: list[Path]):
    doc = SimpleDocTemplate(str(output), pagesize=A4, rightMargin=18 * mm, leftMargin=18 * mm,
                            topMargin=18 * mm, bottomMargin=18 * mm,
                            title=title, author="Tertiary Infotech Pte Ltd")
    width = A4[0] - 36 * mm
    story = cover_story(title, subtitle)
    for src in sources:
        story.append(PageBreak())
        story.append(Paragraph(inline(src.stem.replace("-", " ").title()), H2))
        story.extend(markdown_flow(src.read_text(encoding="utf-8"), width))
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def activity_number(folder: Path) -> str:
    return re.search(r"activity-(\d+)", folder.name).group(1)


def main():
    for folder in sorted(p for p in ACTIVITIES.iterdir() if p.is_dir() and p.name.startswith("activity-")):
        md_files = sorted(folder.glob("*.md"))
        if not md_files:
            continue
        num = activity_number(folder)
        readme = folder / "README.md"
        first_heading = next((line[2:].strip() for line in readme.read_text(encoding="utf-8").splitlines()
                              if line.startswith("# ")), folder.name)

        for src in md_files:
            build_pdf(src.with_suffix(".pdf"), f"Activity {num}: {src.stem.replace('-', ' ').title()}",
                      first_heading, [src])

        existing = sorted(folder.glob(f"Activity-{num}-*.pdf"))
        slug = folder.name.split("-", 2)[2]
        full_output = existing[0] if existing else folder / f"Activity-{num}-{slug}.pdf"
        preferred = ["README.md", "SCENARIO.md", "DISCUSSION-QUESTIONS.md",
                     "PROMPT-INJECTION-PRACTICE.md", "SKILL-PLUGIN-RISK-REVIEW.md",
                     "SECURITY-CHECKLIST.md"]
        ordered = [folder / name for name in preferred if (folder / name).exists()]
        build_pdf(full_output, first_heading, "Complete learner scenario, practice and security checklist", ordered)
        print(f"Built {full_output}")


if __name__ == "__main__":
    main()
