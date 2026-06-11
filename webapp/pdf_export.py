import re
from io import BytesIO

import markdown2
from xhtml2pdf import pisa

# Severidad usa emojis de color que xhtml2pdf no sabe pintar y acaban
# solapados con el texto siguiente, así que se quitan antes de convertir.
_EMOJI_CHARS = "🔴🟠🟡🟢⚪✅❌⚠️⚠"
_EMOJI_TABLE = str.maketrans("", "", _EMOJI_CHARS)

# La tabla "Hallazgos correlacionados" tiene celdas largas sin espacios
# (p.ej. "unprotected_selfdestruct") que xhtml2pdf no parte solo, así que
# se fuerzan anchos de columna fijos junto con table-layout: fixed.
_FINDINGS_HEADER = re.compile(
    r"(<thead>(?:(?!</thead>).)*Tipo(?:(?!</thead>).)*Severidad(?:(?!</thead>).)*</thead>)",
    re.S,
)
_FINDINGS_COL_WIDTHS = ["4%", "11%", "9%", "24%", "10%", "13%", "29%"]

_PDF_STYLE = """
<style>
    body { font-family: Helvetica, sans-serif; font-size: 11px; }
    h1, h2, h3 { color: #1a1c2e; }
    table { border-collapse: collapse; width: 100%; margin-bottom: 1em; table-layout: fixed; }
    th, td {
        border: 1px solid #ccc; padding: 4px 8px; text-align: left;
        word-wrap: break-word; overflow-wrap: break-word; word-break: break-all;
    }
    th { background: #eef0fa; }
    code { background: #f4f4f4; padding: 1px 3px; }
</style>
"""


def _apply_findings_column_widths(html: str) -> str:
    def add_widths(match: re.Match) -> str:
        widths = iter(_FINDINGS_COL_WIDTHS)
        return re.sub(r"<th>", lambda _: f'<th style="width:{next(widths)}">', match.group(1))

    return _FINDINGS_HEADER.sub(add_widths, html, count=1)


def render_pdf(report_md: str) -> bytes:
    """Convierte el informe Markdown del reporter a un PDF descargable."""
    body_html = markdown2.markdown(
        report_md.translate(_EMOJI_TABLE),
        extras=["tables", "fenced-code-blocks"],
    )
    body_html = _apply_findings_column_widths(body_html)
    full_html = f"<html><head>{_PDF_STYLE}</head><body>{body_html}</body></html>"

    buffer = BytesIO()
    pisa.CreatePDF(full_html, dest=buffer)
    return buffer.getvalue()
