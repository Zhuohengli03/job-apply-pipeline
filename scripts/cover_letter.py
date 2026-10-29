#!/usr/bin/env python3
"""生成一页 cover letter PDF。

用法：python3 cover_letter.py spec.json
spec.json：
{
  "name": "San (Tom) Zhang",
  "contact": "Jersey City, NJ | you@email.com | +1 (000) 000-0000 | linkedin.com/in/xxx",
  "company": "Acme",
  "team": "Acme Hiring Team",        # 可选，默认 "{company} Hiring Team"
  "date": "October 29, 2026",          # 可选，默认今天
  "paras": ["第一段……", "第二段……", "第三段……"],
  "out": "/mnt/user-data/outputs/CoverLetter_SanZhang_Acme.pdf"
}
段落里可用 <b>…</b>、<i>…</i>；& 要写成 &amp;。
"""
import datetime
import json
import os
import sys

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

REG, BOLD = "Helvetica", "Helvetica-Bold"
for reg, bold in [("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
                   "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"),
                  ("/Library/Fonts/Arial.ttf", "/Library/Fonts/Arial Bold.ttf")]:
    if os.path.exists(reg) and os.path.exists(bold):
        pdfmetrics.registerFont(TTFont("CLReg", reg))
        pdfmetrics.registerFont(TTFont("CLBold", bold))
        REG, BOLD = "CLReg", "CLBold"
        break

spec = json.load(open(sys.argv[1], encoding="utf-8"))
date = spec.get("date") or datetime.date.today().strftime("%B %-d, %Y")
doc = SimpleDocTemplate(spec["out"], pagesize=letter, leftMargin=72, rightMargin=72, topMargin=60, bottomMargin=60,
                        title=f"Cover Letter - {spec['name']} - {spec['company']}", author=spec["name"])
name_st = ParagraphStyle("n", fontName=BOLD, fontSize=16, leading=20)
hdr_st = ParagraphStyle("h", fontName=REG, fontSize=9.5, leading=13)
body = ParagraphStyle("b", fontName=REG, fontSize=10.5, leading=14.5, spaceAfter=9)
story = [Paragraph(spec["name"], name_st), Paragraph(spec["contact"], hdr_st), Spacer(1, 18),
         Paragraph(date, body), Paragraph(f"Dear {spec.get('team', spec['company'] + ' Hiring Team')},", body)]
story += [Paragraph(p, body) for p in spec["paras"]]
story.append(Paragraph(f"Best regards,<br/>{spec['name']}", body))
doc.build(story)
print(spec["out"])
