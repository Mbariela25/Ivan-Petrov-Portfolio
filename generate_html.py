import base64, re, pathlib

md_text = pathlib.Path("Ivan_Petrov_Portfolio_Report.md").read_text(encoding="utf-8")

# Embed the chart image as base64
img_b64 = base64.b64encode(pathlib.Path("portfolio_allocation.png").read_bytes()).decode()
md_text = md_text.replace(
    "![Ivan Petrov Portfolio Allocation – April 2026](portfolio_allocation.png)",
    f'<img src="data:image/png;base64,{img_b64}" alt="Portfolio Allocation Chart" style="max-width:680px;width:100%;display:block;margin:24px auto;">'
)

def convert_md(text):
    lines = text.split("\n")
    html_lines = []
    in_table = False
    in_code = False
    table_rows = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # Code blocks
        if line.strip().startswith("```"):
            if not in_code:
                in_code = True
                html_lines.append('<pre><code>')
            else:
                in_code = False
                html_lines.append('</code></pre>')
            i += 1
            continue
        if in_code:
            html_lines.append(line.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;"))
            i += 1
            continue

        # Tables
        if line.startswith("|"):
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(line)
            i += 1
            continue
        else:
            if in_table:
                in_table = False
                html_lines.append(render_table(table_rows))
                table_rows = []

        # Already-converted img tags (pass through)
        if line.strip().startswith("<img "):
            html_lines.append(line)
            i += 1
            continue

        # Headings
        if line.startswith("######"): html_lines.append(f"<h6>{inline(line[6:].strip())}</h6>"); i+=1; continue
        if line.startswith("#####"):  html_lines.append(f"<h5>{inline(line[5:].strip())}</h5>"); i+=1; continue
        if line.startswith("####"):   html_lines.append(f"<h4>{inline(line[4:].strip())}</h4>"); i+=1; continue
        if line.startswith("###"):    html_lines.append(f"<h3>{inline(line[3:].strip())}</h3>"); i+=1; continue
        if line.startswith("##"):     html_lines.append(f"<h2>{inline(line[2:].strip())}</h2>"); i+=1; continue
        if line.startswith("#"):      html_lines.append(f"<h1>{inline(line[1:].strip())}</h1>"); i+=1; continue

        # Horizontal rule
        if re.match(r'^---+$', line.strip()):
            html_lines.append("<hr>"); i+=1; continue

        # Blockquote
        if line.startswith("> "):
            html_lines.append(f'<blockquote>{inline(line[2:])}</blockquote>'); i+=1; continue

        # Bullet list
        if re.match(r'^[\-\*] ', line):
            items = []
            while i < len(lines) and re.match(r'^[\-\*] ', lines[i]):
                items.append(f"<li>{inline(lines[i][2:])}</li>")
                i += 1
            html_lines.append("<ul>" + "".join(items) + "</ul>")
            continue

        # Numbered list
        if re.match(r'^\d+\. ', line):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                items.append(f"<li>{inline(re.sub(r'^\d+\. ', '', lines[i]))}</li>")
                i += 1
            html_lines.append("<ol>" + "".join(items) + "</ol>")
            continue

        # Empty line
        if line.strip() == "":
            html_lines.append("<br>"); i+=1; continue

        # Paragraph / italic line (e.g. *text*)
        html_lines.append(f"<p>{inline(line)}</p>")
        i += 1

    if in_table and table_rows:
        html_lines.append(render_table(table_rows))
    return "\n".join(html_lines)


def render_table(rows):
    # Filter separator rows (---|---)
    data_rows = [r for r in rows if not re.match(r'^\|[\s\|\-:]+\|$', r)]
    if not data_rows:
        return ""
    out = ['<table>']
    for idx, row in enumerate(data_rows):
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        tag = "th" if idx == 0 else "td"
        out.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells) + "</tr>")
    out.append("</table>")
    return "\n".join(out)


def inline(text):
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    return text


body = convert_md(md_text)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ivan Petrov Portfolio – Young Investor Hackathon 2026</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Source+Sans+3:wght@400;600&display=swap');

  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    font-family: 'EB Garamond', 'Times New Roman', Georgia, serif;
    font-size: 12.5pt;
    line-height: 1.75;
    color: #1a1a1a;
    background: #f4f1ec;
    padding: 0;
  }}

  .page {{
    max-width: 800px;
    margin: 40px auto 60px;
    background: #ffffff;
    padding: 72px 80px;
    box-shadow: 0 4px 32px rgba(0,0,0,0.12);
    border-top: 6px solid #1B3A6B;
  }}

  h1 {{
    font-size: 22pt;
    font-weight: 700;
    color: #1B3A6B;
    text-align: center;
    margin-bottom: 6px;
    letter-spacing: 0.02em;
  }}
  h2 {{
    font-size: 14pt;
    font-weight: 700;
    color: #1B3A6B;
    border-bottom: 2px solid #1B3A6B;
    padding-bottom: 4px;
    margin: 36px 0 14px;
    page-break-after: avoid;
  }}
  h3 {{
    font-size: 12pt;
    font-weight: 700;
    color: #2c4f7a;
    margin: 24px 0 10px;
  }}
  h4 {{
    font-size: 11.5pt;
    font-weight: 600;
    color: #333;
    margin: 18px 0 8px;
  }}

  p {{ margin-bottom: 10px; }}
  br {{ display: block; margin: 4px 0; }}

  strong {{ color: #1B3A6B; }}

  hr {{
    border: none;
    border-top: 1px solid #d0cac0;
    margin: 28px 0;
  }}

  blockquote {{
    border-left: 4px solid #C49A2C;
    background: #faf8f3;
    padding: 12px 20px;
    margin: 18px 0;
    font-style: italic;
    color: #444;
    border-radius: 0 4px 4px 0;
  }}

  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0 24px;
    font-size: 11pt;
    font-family: 'Source Sans 3', 'Arial', sans-serif;
  }}
  th {{
    background: #1B3A6B;
    color: #ffffff;
    font-weight: 600;
    padding: 8px 10px;
    text-align: left;
    font-size: 10.5pt;
  }}
  td {{
    padding: 7px 10px;
    border-bottom: 1px solid #e5e0d8;
    vertical-align: top;
  }}
  tr:nth-child(even) td {{ background: #f8f5f0; }}
  tr:hover td {{ background: #f0ebe0; }}

  ul, ol {{
    margin: 8px 0 14px 24px;
  }}
  li {{ margin-bottom: 5px; }}

  code {{
    background: #f0ece4;
    padding: 1px 5px;
    border-radius: 3px;
    font-size: 10.5pt;
    font-family: 'Courier New', monospace;
  }}

  .subtitle {{
    text-align: center;
    color: #666;
    font-style: italic;
    font-size: 10.5pt;
    margin-bottom: 32px;
  }}

  img {{ border-radius: 4px; }}

  @media print {{
    body {{ background: white; }}
    .page {{ box-shadow: none; margin: 0; padding: 48px 60px; border-top: none; }}
    h2 {{ page-break-before: auto; }}
  }}
</style>
</head>
<body>
<div class="page">
{body}
</div>
</body>
</html>"""

pathlib.Path("report.html").write_text(html, encoding="utf-8")
print("Saved: report.html")
print(f"File size: {pathlib.Path('report.html').stat().st_size // 1024} KB")
