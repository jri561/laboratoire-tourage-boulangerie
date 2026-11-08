# -*- coding: utf-8 -*-
import re
import subprocess
import sys
from pathlib import Path
import pypdf

from recipe_data import RECIPES

OUTPUT_DIR = Path("Cahier_Recettes_Atelier")
SOURCES_DIR = OUTPUT_DIR / "_sources_html"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
SOURCES_DIR.mkdir(parents=True, exist_ok=True)

FAMILY_THEMES = {
    "viennoiserie": {
        "accent": "#d97706",          # Ambre / Cuivre
        "badge_bg": "#b45309",
        "total_bg": "#ffedd5",
        "subtotal_bg": "#fff7ed",
        "soft_bg": "#fffbeb",
        "soft_border": "#fde68a",
    },
    "patisserie": {
        "accent": "#be185d",          # Bordeaux / Cacao prune
        "badge_bg": "#9d174d",
        "total_bg": "#fce7f3",
        "subtotal_bg": "#fdf2f8",
        "soft_bg": "#fdf2f8",
        "soft_border": "#fbcfe8",
    },
    "traiteur": {
        "accent": "#059669",          # Vert Émeraude
        "badge_bg": "#047857",
        "total_bg": "#d1fae5",
        "subtotal_bg": "#ecfdf5",
        "soft_bg": "#ecfdf5",
        "soft_border": "#a7f3d0",
    },
    "referentiel": {
        "accent": "#0284c7",          # Bleu Ardoise
        "badge_bg": "#0369a1",
        "total_bg": "#e0f2fe",
        "subtotal_bg": "#f0f9ff",
        "soft_bg": "#f0f9ff",
        "soft_border": "#bae6fd",
    },
}

HTML_DOUBLE_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>{title} — {code}</title>
<style>
@page {{
  size: A4 portrait;
  margin: 7mm 8mm;
}}
* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}}
body {{
  color: #0f172a;
  background: #ffffff;
  letter-spacing: 0.15px;
}}

.sheet-page {{
  width: 100%;
  height: 282mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  page-break-after: always;
  break-after: page;
}}
.sheet-page:last-child {{
  page-break-after: auto;
  break-after: auto;
}}

/* EN-TÊTE ÉPURÉ HAUTE LISIBILITÉ */
.header-banner {{
  background: #f8fafc;
  border: 1.5px solid #cbd5e1;
  border-left: 8px solid {accent};
  border-radius: 7px;
  padding: 10px 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: {gap_head};
}}
.header-titles h1 {{
  font-size: {h1_size};
  font-weight: 900;
  color: #0f172a;
  letter-spacing: -0.2px;
  line-height: 1.15;
}}
.header-titles .subtitle {{
  font-size: {sub_size};
  font-weight: 700;
  color: #475569;
  margin-top: 3px;
  line-height: 1.25;
}}
.header-right {{
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 3px;
}}
.header-badge {{
  background: {badge_bg};
  color: #ffffff;
  padding: 6px 12px;
  border-radius: 5px;
  font-weight: 900;
  font-size: 12.5px;
  letter-spacing: 0.5px;
  white-space: nowrap;
}}
.page-indicator {{
  font-size: 10px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.6px;
  color: {accent};
}}

/* BANDEAU FLASH GÉANT */
.flash-row {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 9px;
  margin-bottom: {gap_flash_bot};
}}
.flash-card {{
  background: #f8fafc;
  border: 1.5px solid #cbd5e1;
  border-left: 5.5px solid #0284c7;
  padding: {flash_pad};
  border-radius: 6px;
}}
.flash-card.alert {{
  border-left-color: #dc2626;
  background: #fff5f5;
  border-color: #fecaca;
}}
.flash-card.amber {{
  border-left-color: #d97706;
  background: #fffbeb;
  border-color: #fde68a;
}}
.flash-card.green {{
  border-left-color: #059669;
  background: #f0fdf4;
  border-color: #bbf7d0;
}}
.flash-card .lbl {{
  font-size: {flash_lbl_size};
  font-weight: 800;
  color: #475569;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  margin-bottom: 3px;
}}
.flash-card .val {{
  font-size: {flash_val_size};
  font-weight: 900;
  color: #0f172a;
  line-height: 1.15;
}}

/* TABLEAUX DES PESÉES GRAND CONFORT (PAGE GAUCHE) */
.tables-container {{
  display: flex;
  flex-direction: column;
  gap: {gap_tables};
  flex-grow: 1;
  justify-content: flex-start;
}}
table.giant-table {{
  width: 100%;
  border-collapse: collapse;
  border: 1.5px solid #94a3b8;
  border-radius: 6px;
  overflow: hidden;
}}
table.giant-table th {{
  background: #f1f5f9;
  color: #0f172a;
  padding: {th_pad};
  font-size: {th_size};
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  border-bottom: 2.2px solid #0f172a;
  border-right: 1px solid #cbd5e1;
}}
table.giant-table th:last-child {{ border-right: none; }}
table.giant-table th.left, table.giant-table td.left {{ text-align: left; }}
table.giant-table th.right, table.giant-table td.right {{ text-align: right; }}
table.giant-table th.center, table.giant-table td.center {{ text-align: center; }}

table.giant-table td {{
  padding: {td_pad};
  border-bottom: 1px solid #cbd5e1;
  border-right: 1px solid #e2e8f0;
  font-size: {td_size};
  font-weight: 700;
  color: #1e293b;
}}
table.giant-table td:last-child {{ border-right: none; }}
table.giant-table tr:nth-child(even) td {{
  background-color: #f8fafc;
}}

/* Indicateur couleur gauche selon l'étape */
table.giant-table tr.step-row-1 td:first-child {{ border-left: 5.5px solid #0284c7; }}
table.giant-table tr.step-row-2 td:first-child {{ border-left: 5.5px solid #d97706; }}
table.giant-table tr.step-row-3 td:first-child {{ border-left: 5.5px solid #059669; }}
table.giant-table tr.step-row-4 td:first-child {{ border-left: 5.5px solid #7c3aed; }}

table.giant-table td.ing-name {{
  font-size: {td_name_size};
  font-weight: 800;
  color: #0f172a;
}}
.ing-note {{
  font-weight: 600;
  color: #475569;
  font-size: 0.88em;
}}

/* Pastilles d'étapes numérotées */
.step-pill {{
  display: inline-block;
  padding: 1.5px 7px;
  border-radius: 4px;
  font-weight: 900;
  font-size: 0.86em;
  color: #ffffff;
  margin-right: 6px;
  vertical-align: baseline;
  letter-spacing: 0.25px;
}}
.step-pill.s1 {{ background: #0284c7; }}
.step-pill.s2 {{ background: #d97706; }}
.step-pill.s3 {{ background: #059669; }}
.step-pill.s4 {{ background: #7c3aed; }}

table.giant-table td.weight-cell {{
  font-size: {td_weight_size};
  font-weight: 900;
  color: #000000;
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.35px;
}}
table.giant-table tr.subtotal td {{
  background: {subtotal_bg};
  font-size: {subtotal_size};
  font-weight: 900;
  color: #0f172a;
  border-top: 1.8px solid #475569;
  border-bottom: 1.8px solid #475569;
}}
table.giant-table tr.total-final td {{
  background: {total_bg};
  font-size: {total_size};
  font-weight: 900;
  color: #000000;
  border-top: 2.2px solid #0f172a;
  border-bottom: 2.2px solid #0f172a;
}}

/* PAGE DE DROITE : PROTOCOLE PLEINE LARGEUR EN GROS CARACTÈRES */
.right-content {{
  display: flex;
  flex-direction: column;
  gap: 14px;
  flex-grow: 1;
  justify-content: flex-start;
}}
.proto-block {{
  background: #ffffff;
  border: 1.5px solid #cbd5e1;
  border-left: 7px solid #0284c7;
  border-radius: 7px;
  padding: {proto_pad};
}}
.proto-block.b2 {{
  border-left-color: #d97706;
}}
.proto-block h2 {{
  font-size: {proto_title_size};
  font-weight: 900;
  color: #0f172a;
  text-transform: uppercase;
  border-bottom: 1.5px solid #e2e8f0;
  padding-bottom: 6px;
  margin-bottom: 10px;
  letter-spacing: 0.25px;
}}
.proto-list {{
  list-style: none;
  font-size: {proto_step_size};
  line-height: {proto_lh};
  color: #1e293b;
}}
.proto-list li {{
  margin-bottom: {proto_step_margin};
  padding-left: 14px;
  position: relative;
}}
.proto-list li::before {{
  content: "▪";
  position: absolute;
  left: 0;
  color: {accent};
  font-weight: 900;
}}
.proto-list strong {{
  color: #000000;
  font-weight: 900;
}}

/* Encadré Récapitulatif de Sécurité & Contrôle (Bas de Page Droite) */
.summary-box {{
  background: {soft_bg};
  border: 1.5px solid {soft_border};
  border-left: 7px solid {accent};
  border-radius: 7px;
  padding: 12px 16px;
}}
.summary-box h3 {{
  font-size: 13px;
  font-weight: 900;
  text-transform: uppercase;
  color: #0f172a;
  margin-bottom: 8px;
  letter-spacing: 0.3px;
}}
.summary-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px 16px;
  font-size: 13px;
  line-height: 1.35;
}}
.summary-item strong {{
  color: #000000;
  font-weight: 900;
}}

/* PIED DE PAGE */
.footer {{
  border-top: 1.8px solid #cbd5e1;
  padding-top: 5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 10px;
  color: #334155;
  font-weight: 800;
}}
.legend-inline {{
  display: flex;
  gap: 10px;
  align-items: center;
}}
.legend-dot {{
  display: inline-block;
  width: 9px;
  height: 9px;
  border-radius: 2px;
  margin-right: 4px;
}}
</style>
</head>
<body>

  <!-- ===================================================================== -->
  <!-- PAGE 1 (GAUCHE) : POSTE DE PESÉE & TABLEAUX EN GROS CARACTÈRES        -->
  <!-- ===================================================================== -->
  <div class="sheet-page">
    <div>
      <div class="header-banner">
        <div class="header-titles">
          <h1>{title}</h1>
          <div class="subtitle">{subtitle}</div>
        </div>
        <div class="header-right">
          <div class="header-badge">{code} • GAUCHE</div>
          <div class="page-indicator">PAGE 1/2 • POSTE DE PESÉE</div>
        </div>
      </div>

      <div class="flash-row">
        {flash_html}
      </div>

      <div class="tables-container">
        {tables_left_html}
      </div>
    </div>

    <div class="footer">
      <span>{code} • {family_label}</span>
      <span class="legend-inline">
        <span><i class="legend-dot" style="background:#0284c7;"></i>1. Base / Frasage</span>
        <span><i class="legend-dot" style="background:#d97706;"></i>2. Incorp. / Liquides</span>
        <span><i class="legend-dot" style="background:#059669;"></i>3. Poudres / Tourage</span>
        <span><i class="legend-dot" style="background:#7c3aed;"></i>4. Inclusions / Finition</span>
      </span>
      <span>PAGE GAUCHE (1/2)</span>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- PAGE 2 (DROITE) : PROTOCOLE PAS À PAS, FAÇONNAGE & CUISSON            -->
  <!-- ===================================================================== -->
  <div class="sheet-page">
    <div>
      <div class="header-banner">
        <div class="header-titles">
          <h1>{title} — Marche à Suivre</h1>
          <div class="subtitle">Protocole chronologique étape par étape, conduite machine et barème de cuisson</div>
        </div>
        <div class="header-right">
          <div class="header-badge">{code} • DROITE</div>
          <div class="page-indicator">PAGE 2/2 • PROTOCOLE &amp; FOUR</div>
        </div>
      </div>

      <div class="right-content">
        {right_body_html}
      </div>
    </div>

    <div class="footer">
      <span>{code} • {title}</span>
      <span>Lire de gauche à droite classeur ouvert (Pesées à gauche ↔ Protocole à droite)</span>
      <span>PAGE DROITE (2/2)</span>
    </div>
  </div>

</body>
</html>
"""

def get_double_page_params(rec):
    num_tables = len(rec["tables"])
    total_rows = sum(len(t["rows"]) for t in rec["tables"])
    max_cols = max(len(t["headers"]) for t in rec["tables"])
    total_steps = len(rec["col1"]["steps"]) + len(rec["col2"]["steps"])

    # Special case: Fiche 16 (Registre des cuissons) -> Table 1 on Left Page, Table 2 on Right Page!
    if rec["id"] == "16_Registre_General_Cuissons_Atelier":
        return {
            "gap_head": "10px",
            "h1_size": "21px", "sub_size": "11.5px",
            "gap_flash_bot": "10px", "flash_pad": "7px 10px",
            "flash_lbl_size": "9.5px", "flash_val_size": "14px",
            "gap_tables": "10px",
            "th_pad": "7px 7px", "th_size": "10.5px",
            "td_pad": "6.5px 7px", "td_size": "11.5px", "td_name_size": "12px", "td_weight_size": "12px",
            "subtotal_size": "11.5px", "total_size": "12px",
            "proto_pad": "12px 16px",
            "proto_title_size": "14.5px", "proto_step_size": "13.5px", "proto_lh": "1.45",
            "proto_step_margin": "6px",
        }

    # Left page table sizing based on total rows across tables
    if num_tables >= 3 or total_rows >= 18:
        # 2 or 3 tables (Brookie 17 rows, Muffins 19 rows, Frangipane 3 tables, Quiches 16 rows, Dorures 3 tables)
        th_pad = "6.5px 9px"
        th_size = "11.5px"
        td_pad = "5.8px 9px"
        td_size = "13px"
        td_name_size = "13.5px"
        td_weight_size = "15px"
        subtotal_size = "13.5px"
        total_size = "14.5px"
        gap_tables = "10px"
        gap_head = "9px"
        gap_flash_bot = "10px"
        flash_pad = "6.5px 9px"
        flash_lbl_size = "9.5px"
        flash_val_size = "14.5px"
        h1_size = "21px"
        sub_size = "11.5px"
    elif total_rows >= 12 or max_cols >= 7:
        # 1 medium-large table (Viennoise 15 rows, Kouign 12 rows, PLF 12 rows, Cookies 12 rows, Crêpes 8 cols, Cakes 2 tables)
        th_pad = "8px 10px"
        th_size = "12px" if max_cols < 7 else "10.8px"
        td_pad = "7.8px 10px" if max_cols < 7 else "8.5px 7px"
        td_size = "14px" if max_cols < 7 else "12.8px"
        td_name_size = "14.5px" if max_cols < 7 else "13.2px"
        td_weight_size = "16.5px" if max_cols < 7 else "14.5px"
        subtotal_size = "14.5px"
        total_size = "15.5px"
        gap_tables = "12px"
        gap_head = "11px"
        gap_flash_bot = "12px"
        flash_pad = "8px 10px"
        flash_lbl_size = "10px"
        flash_val_size = "15px"
        h1_size = "22px"
        sub_size = "12px"
    else:
        # 1 compact table (Galettes 7 rows, Feuilletage 8 rows, Annexe Rondo 6 rows, Brownie 11 rows, Brioches 11 rows)
        th_pad = "10px 12px"
        th_size = "13px"
        td_pad = "10px 12px"
        td_size = "15px"
        td_name_size = "15.5px"
        td_weight_size = "18px"
        subtotal_size = "15.5px"
        total_size = "16.5px"
        gap_tables = "14px"
        gap_head = "12px"
        gap_flash_bot = "14px"
        flash_pad = "9px 11px"
        flash_lbl_size = "10.5px"
        flash_val_size = "15.5px"
        h1_size = "23px"
        sub_size = "12.5px"

    # Right page protocol sizing based on total steps
    if total_steps >= 9:
        proto_pad = "13px 18px"
        proto_title_size = "15.5px"
        proto_step_size = "14px"
        proto_lh = "1.48"
        proto_step_margin = "8px"
    else:
        proto_pad = "16px 20px"
        proto_title_size = "16.5px"
        proto_step_size = "15px"
        proto_lh = "1.55"
        proto_step_margin = "10px"

    return {
        "gap_head": gap_head,
        "h1_size": h1_size, "sub_size": sub_size,
        "gap_flash_bot": gap_flash_bot, "flash_pad": flash_pad,
        "flash_lbl_size": flash_lbl_size, "flash_val_size": flash_val_size,
        "gap_tables": gap_tables,
        "th_pad": th_pad, "th_size": th_size,
        "td_pad": td_pad, "td_size": td_size, "td_name_size": td_name_size, "td_weight_size": td_weight_size,
        "subtotal_size": subtotal_size, "total_size": total_size,
        "proto_pad": proto_pad,
        "proto_title_size": proto_title_size, "proto_step_size": proto_step_size, "proto_lh": proto_lh,
        "proto_step_margin": proto_step_margin,
    }

def is_subtotal_row(row):
    first = str(row[0]).strip().upper()
    return ("SOUS-TOTAL" in first or 
            "TOTAL DÉTREMPE" in first or 
            "DÉTREMPE AU BAC" in first or 
            "APPAREIL TOTAL" in first)

def format_ingredient_cell(raw_text):
    text = str(raw_text).strip()
    if text.startswith("STANDARD •"):
        rest = text.replace("STANDARD •", "").strip()
        rest = re.sub(r"(\([^)]+\))", r"<span class='ing-note'>\1</span>", rest)
        pill = "<span class='step-pill s3'>STANDARD</span>"
        return f"{pill}{rest}", "step-row-3"
    m = re.match(r"^([1-4])\.\s+(.*)$", text)
    if m:
        step_num = int(m.group(1))
        rest = m.group(2)
        rest = re.sub(r"(\([^)]+\))", r"<span class='ing-note'>\1</span>", rest)
        pill = f"<span class='step-pill s{step_num}'>{step_num}</span>"
        return f"{pill}{rest}", f"step-row-{step_num}"
    else:
        rest = re.sub(r"(\([^)]+\))", r"<span class='ing-note'>\1</span>", text)
        return rest, ""

def format_protocol_step(step_html):
    s = step_html
    s = re.sub(r"Étape\s*1\s*•?", r"<span class='step-pill s1'>ÉTAPE 1</span>", s)
    s = re.sub(r"Étape\s*2\s*•?", r"<span class='step-pill s2'>ÉTAPE 2</span>", s)
    s = re.sub(r"Étape\s*3\s*•?", r"<span class='step-pill s3'>ÉTAPE 3</span>", s)
    s = re.sub(r"Étape\s*4\s*•?", r"<span class='step-pill s4'>ÉTAPE 4</span>", s)
    s = re.sub(r"Étapes\s*2\s*&\s*3\s*•?", r"<span class='step-pill s2'>ÉTAPES 2 & 3</span>", s)
    s = re.sub(r"Bloc\s*1\s*•?", r"<span class='step-pill s1'>BLOC 1</span>", s)
    s = re.sub(r"Bloc\s*2\s*•?", r"<span class='step-pill s2'>BLOC 2</span>", s)
    s = re.sub(r"Déclinaison\s*1\s*•?", r"<span class='step-pill s1'>GOURMET 1</span>", s)
    s = re.sub(r"Déclinaison\s*2\s*•?", r"<span class='step-pill s2'>GOURMET 2</span>", s)
    s = re.sub(r"Déclinaison\s*3\s*•?", r"<span class='step-pill s3'>GOURMET 3</span>", s)
    s = re.sub(r"<strong>([1-4])\)</strong>", r"<span class='step-pill s\1'>\1</span>", s)
    return s

def build_table_html(t):
    headers_html = "".join([f"<th class='{align}'>{h}</th>" for h, align in zip(t["headers"], t["align"])])
    rows_parts = []
    for row in t["rows"]:
        row_is_sub = is_subtotal_row(row)
        cells = []
        step_row_cls = ""
        for idx, (val, align) in enumerate(zip(row, t["align"])):
            if idx == 0:
                cls = "left ing-name"
                if not row_is_sub:
                    formatted_val, step_row_cls = format_ingredient_cell(val)
                else:
                    formatted_val = val
            elif align == "right":
                cls = "right weight-cell"
                formatted_val = val
            else:
                cls = align
                formatted_val = val
            cells.append(f"<td class='{cls}'>{formatted_val}</td>")
        cells_str = "".join(cells)
        if row_is_sub:
            tr_cls = "class='subtotal'"
        elif step_row_cls:
            tr_cls = f"class='{step_row_cls}'"
        else:
            tr_cls = ""
        rows_parts.append(f"<tr {tr_cls}>{cells_str}</tr>")
    rows_html = "\n".join(rows_parts)
    
    total_html = ""
    if t.get("total"):
        cells = []
        for idx, (val, align) in enumerate(zip(t["total"], t["align"])):
            cls = "left" if idx == 0 else "right"
            cells.append(f"<td class='{cls}'>{val}</td>")
        cells_str = "".join(cells)
        total_html = f"<tr class='total-final'>{cells_str}</tr>"
    
    return f"""
    <table class="giant-table">
      <thead><tr>{headers_html}</tr></thead>
      <tbody>
        {rows_html}
        {total_html}
      </tbody>
    </table>
    """

def render_recipe_html(rec):
    params = get_double_page_params(rec)
    fam = rec.get("family", "referentiel")
    theme = FAMILY_THEMES.get(fam, FAMILY_THEMES["referentiel"])
    
    # Flash cards
    flash_parts = []
    for f in rec.get("flash", []):
        cls = f.get("class", "")
        flash_parts.append(f"""
        <div class="flash-card {cls}">
          <div class="lbl">{f['lbl']}</div>
          <div class="val">{f['val']}</div>
        </div>
        """)
    flash_html = "\n".join(flash_parts)

    col1 = rec.get("col1", {"title": "Protocole", "steps": []})
    col2 = rec.get("col2", {"title": "Paramètres", "steps": []})
    col1_steps_html = "\n".join([f"<li>{format_protocol_step(s)}</li>" for s in col1["steps"]])
    col2_steps_html = "\n".join([f"<li>{format_protocol_step(s)}</li>" for s in col2["steps"]])

    # Summary box items from flash cards for the right page
    summary_items = []
    for f in rec.get("flash", []):
        summary_items.append(f"<div class='summary-item'>• {f['lbl']} : <strong>{f['val']}</strong></div>")
    summary_grid_html = "\n".join(summary_items)

    if rec["id"] == "16_Registre_General_Cuissons_Atelier":
        # For Fiche 16 (Oven Master Register), put Table 1 + Col 1 on Left Page, and Table 2 + Col 2 on Right Page!
        t1_html = build_table_html(rec["tables"][0])
        t2_html = build_table_html(rec["tables"][1])
        tables_left_html = f"""
        {t1_html}
        <div class="proto-block" style="margin-top: 8px;">
          <h2>{col1['title']}</h2>
          <ul class="proto-list">{col1_steps_html}</ul>
        </div>
        """
        right_body_html = f"""
        {t2_html}
        <div class="proto-block b2" style="margin-top: 8px;">
          <h2>{col2['title']}</h2>
          <ul class="proto-list">{col2_steps_html}</ul>
        </div>
        """
    else:
        tables_left_html = "\n".join([build_table_html(t) for t in rec.get("tables", [])])
        right_body_html = f"""
        <div class="proto-block">
          <h2>{col1['title']}</h2>
          <ul class="proto-list">
            {col1_steps_html}
          </ul>
        </div>
        <div class="proto-block b2">
          <h2>{col2['title']}</h2>
          <ul class="proto-list">
            {col2_steps_html}
          </ul>
        </div>
        <div class="summary-box">
          <h3>Repères de Contrôle Rapide au Poste ({rec['code']})</h3>
          <div class="summary-grid">
            {summary_grid_html}
          </div>
        </div>
        """

    return HTML_DOUBLE_PAGE_TEMPLATE.format(
        title=rec["title"],
        code=rec["code"],
        family_label=rec.get("family_label", "ATELIER"),
        subtitle=rec["subtitle"],
        flash_html=flash_html,
        tables_left_html=tables_left_html,
        right_body_html=right_body_html,
        **params,
        **theme
    )

def generate_pdf_from_html(html_path, pdf_path):
    cmd = [
        "chromium",
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--print-to-pdf={pdf_path}",
        str(html_path)
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    print(f"=== COMPILATION DES {len(RECIPES)} FICHES EN DOUBLE PAGE VIS-À-VIS (GAUCHE + DROITE) ===")
    individual_pdfs = []
    has_error = False
    
    for rec in RECIPES:
        rec_id = rec["id"]
        html_content = render_recipe_html(rec)
        html_file = SOURCES_DIR / f"{rec_id}.html"
        pdf_file = OUTPUT_DIR / f"{rec_id}.pdf"
        
        html_file.write_text(html_content, encoding="utf-8")
        generate_pdf_from_html(html_file, pdf_file)
        
        reader = pypdf.PdfReader(str(pdf_file))
        num_pages = len(reader.pages)
        if num_pages == 2:
            status = "OK (2 pages vis-à-vis : Gauche + Droite)"
        else:
            status = f"ERREUR PAGINATION ({num_pages} pages au lieu de 2 !)"
            has_error = True
        print(f"[{rec['code']}] {rec['title']} -> {pdf_file.name} : {status}")
        individual_pdfs.append((rec, pdf_file))

    # 1. Page de garde (Page 1 — Recto isolé)
    cover_html = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<style>
@page { size: A4 portrait; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
body {
  width: 210mm; height: 297mm;
  background: #0f172a;
  color: #ffffff;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 24mm 20mm;
}
.cover-top {
  border-bottom: 2px solid #38bdf8;
  padding-bottom: 10mm;
}
.cover-badge {
  display: inline-block;
  background: #0284c7;
  color: #fff;
  padding: 6px 14px;
  border-radius: 4px;
  font-size: 13px;
  font-weight: 900;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  margin-bottom: 6mm;
}
h1 {
  font-size: 38px;
  font-weight: 900;
  line-height: 1.15;
  text-transform: uppercase;
  letter-spacing: -0.5px;
  margin-bottom: 5mm;
}
.subtitle {
  font-size: 18px;
  color: #cbd5e1;
  font-weight: 500;
  line-height: 1.4;
}
.cover-middle {
  background: #1e293b;
  border-left: 6px solid #38bdf8;
  padding: 10mm;
  border-radius: 6px;
}
.cover-middle h2 {
  font-size: 16px;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: #38bdf8;
  margin-bottom: 5mm;
}
.grid-specs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5mm;
}
.spec-item {
  background: #0f172a;
  padding: 4mm 5mm;
  border-radius: 4px;
  border: 1px solid #334155;
}
.spec-item .lbl {
  font-size: 11px;
  color: #94a3b8;
  text-transform: uppercase;
  font-weight: 800;
  margin-bottom: 1mm;
}
.spec-item .val {
  font-size: 14px;
  color: #f8fafc;
  font-weight: 800;
}
.cover-bottom {
  border-top: 1px solid #334155;
  padding-top: 6mm;
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  color: #94a3b8;
  font-weight: 600;
}
</style>
</head>
<body>
  <div class="cover-top">
    <div class="cover-badge">Édition Grand Confort • Double Page en Vis-à-Vis</div>
    <h1>Cahier de Recettes<br>&amp; Protocoles d'Atelier</h1>
    <div class="subtitle">Page de Gauche : Tableaux de Pesées Chronologiques en Gros Caractères<br>Page de Droite : Marche à Suivre Pas à Pas, Façonnages &amp; Barèmes de Cuisson</div>
  </div>

  <div class="cover-middle">
    <h2>Architecture Ergonomique &amp; Codes Couleurs d'Atelier</h2>
    <div class="grid-specs">
      <div class="spec-item">
        <div class="lbl">Vis-à-Vis Classeur Ouvert</div>
        <div class="val">Gauche = Pesées • Droite = Protocole</div>
      </div>
      <div class="spec-item">
        <div class="lbl">Ordre Chronologique des Pesées</div>
        <div class="val">[1] Base → [2] Incorp. → [3] Poudres → [4] Fin</div>
      </div>
      <div class="spec-item">
        <div class="lbl">Viennoiserie &amp; Pâtisserie</div>
        <div class="val">Code Ambre (Vienn.) &amp; Bordeaux (Pâtiss.)</div>
      </div>
      <div class="spec-item">
        <div class="lbl">Traiteur &amp; Référentiels</div>
        <div class="val">Code Émeraude (Traiteur) &amp; Bleu (Réf.)</div>
      </div>
    </div>
  </div>

  <div class="cover-bottom">
    <span>Laboratoire de Tourage, Viennoiserie &amp; Pâtisserie</span>
    <span>Édition Consolidée • 16 Doubles Pages (35 Pages au total)</span>
  </div>
</body>
</html>"""
    cover_html_file = SOURCES_DIR / "00_Couverture.html"
    cover_pdf_file = OUTPUT_DIR / "00_Couverture.pdf"
    cover_html_file.write_text(cover_html, encoding="utf-8")
    generate_pdf_from_html(cover_html_file, cover_pdf_file)

    # 2. Sommaire & Guide de Lecture en Double Page (Pages 2 & 3) pour aligner toutes les recettes sur Pair (Gauche) / Impair (Droite) !
    toc_html = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<style>
@page { size: A4 portrait; margin: 7mm 8mm; }
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
body { width: 100%; color: #0f172a; letter-spacing: 0.15px; }
.sheet-page {
  width: 100%;
  height: 282mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  page-break-after: always;
  break-after: page;
}
.sheet-page:last-child {
  page-break-after: auto;
  break-after: auto;
}
.header { background: #f8fafc; border: 1.5px solid #cbd5e1; border-left: 8px solid #0284c7; border-radius: 7px; padding: 10px 16px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; }
h1 { font-size: 21px; font-weight: 900; text-transform: uppercase; letter-spacing: -0.2px; }
.subtitle { font-size: 11.5px; color: #475569; font-weight: 700; margin-top: 2px; }
.badge { background: #0284c7; color: #fff; padding: 6px 12px; border-radius: 5px; font-weight: 900; font-size: 12px; }
table { width: 100%; border-collapse: collapse; border: 1.5px solid #94a3b8; border-radius: 6px; overflow: hidden; }
th { background: #f1f5f9; color: #0f172a; padding: 8px 10px; text-align: left; font-size: 11.5px; font-weight: 900; text-transform: uppercase; border-bottom: 2px solid #0f172a; }
td { padding: 7.5px 10px; border-bottom: 1px solid #cbd5e1; font-size: 12px; font-weight: 700; color: #0f172a; }
tr:nth-child(even) td { background-color: #f8fafc; }
.fam-pill { display: inline-block; padding: 2px 7px; border-radius: 4px; color: #fff; font-weight: 900; font-size: 9.5px; text-transform: uppercase; }
.fam-tr { background: #059669; }
.fam-vn { background: #d97706; }
.fam-pt { background: #be185d; }
.fam-rf { background: #0284c7; }
.code-col { font-weight: 900; color: #0f172a; white-space: nowrap; }
.page-col { font-weight: 900; text-align: right; color: #000000; white-space: nowrap; }

.guide-block { background: #ffffff; border: 1.5px solid #cbd5e1; border-left: 7px solid #0284c7; border-radius: 7px; padding: 15px 18px; margin-bottom: 14px; }
.guide-block.amber { border-left-color: #d97706; }
.guide-block.green { border-left-color: #059669; }
.guide-block.red { border-left-color: #dc2626; }
.guide-title { font-size: 15.5px; font-weight: 900; text-transform: uppercase; color: #0f172a; border-bottom: 1.5px solid #e2e8f0; padding-bottom: 6px; margin-bottom: 10px; }
.guide-list { list-style: none; font-size: 14px; line-height: 1.52; color: #1e293b; }
.guide-list li { margin-bottom: 8px; }
.step-pill { display: inline-block; padding: 2px 8px; border-radius: 4px; color: #fff; font-weight: 900; font-size: 12px; margin-right: 6px; }
.s1 { background: #0284c7; }
.s2 { background: #d97706; }
.s3 { background: #059669; }
.s4 { background: #7c3aed; }

.footer { border-top: 1.8px solid #cbd5e1; padding-top: 5px; display: flex; justify-content: space-between; font-size: 10px; color: #334155; font-weight: 800; }
</style>
</head>
<body>
  <!-- PAGE 2 (GAUCHE) : SOMMAIRE GÉNÉRAL EN GROS CARACTÈRES -->
  <div class="sheet-page">
    <div>
      <div class="header">
        <div>
          <h1>Sommaire Général des Doubles Pages</h1>
          <div class="subtitle">PAGE DE GAUCHE = PESÉES CHRONOLOGIQUES • PAGE DE DROITE = PROTOCOLE &amp; CUISSON</div>
        </div>
        <div class="badge">SOMMAIRE • GAUCHE</div>
      </div>

      <table>
        <thead>
          <tr>
            <th style="width: 13%;">Fiche</th>
            <th style="width: 14%;">Famille</th>
            <th style="width: 36%;">Désignation de la Recette</th>
            <th style="width: 23%;">Logique de Pesée</th>
            <th class="page-col" style="width: 14%;">Pages</th>
          </tr>
        </thead>
        <tbody>
          <tr><td class="code-col">FICHE 01</td><td><span class="fam-pill fam-tr">Traiteur</span></td><td>Crêpes de Froment (Girocrêpes)</td><td>1. Frasage → 2. Allongement</td><td class="page-col">Pages 4–5</td></tr>
          <tr><td class="code-col">FICHE 02</td><td><span class="fam-pill fam-tr">Traiteur</span></td><td>Galettes de Blé Noir (Girocrêpes)</td><td>1. Frasage → 2. Allongement</td><td class="page-col">Pages 6–7</td></tr>
          <tr><td class="code-col">FICHE 03</td><td><span class="fam-pill fam-vn">Viennois.</span></td><td>Kouign-Amann (100g &amp; Partage 4–6p)</td><td>1. Détrempe → 2. Opale → 3. Beurre</td><td class="page-col">Pages 8–9</td></tr>
          <tr><td class="code-col">FICHE 04</td><td><span class="fam-pill fam-vn">Viennois.</span></td><td>Viennoise (Nature &amp; Chocolat) PAC</td><td>1. Réseau → 2. Opale → 3. Pépites</td><td class="page-col">Pages 10–11</td></tr>
          <tr><td class="code-col">FICHE 05</td><td><span class="fam-pill fam-vn">Viennois.</span></td><td>Feuilletage Inversé (48 feuillets)</td><td>1. Beurre manié → 2. Détrempe</td><td class="page-col">Pages 12–13</td></tr>
          <tr><td class="code-col">FICHE 06</td><td><span class="fam-pill fam-vn">Viennois.</span></td><td>PLF (Pâte Levée Feuilletée) PAC</td><td>1. Frasage → 2. Opale → 3. Tourage</td><td class="page-col">Pages 14–15</td></tr>
          <tr><td class="code-col">FICHE 07</td><td><span class="fam-pill fam-pt">Pâtiss.</span></td><td>Brookie (Cadres 56x36 cm)</td><td>A. Brownie + B. Abaisse Cookie</td><td class="page-col">Pages 16–17</td></tr>
          <tr><td class="code-col">FICHE 08</td><td><span class="fam-pill fam-pt">Pâtiss.</span></td><td>Brownie Fondant Chocolat (56x36 cm)</td><td>1. Choc → 2. Œufs → 3. Poudres</td><td class="page-col">Pages 18–19</td></tr>
          <tr><td class="code-col">FICHE 09</td><td><span class="fam-pill fam-pt">Pâtiss.</span></td><td>Gamme Muffins Atelier (120 g)</td><td>1. Blanchir → 2. Liq. → 3. Poudres</td><td class="page-col">Pages 20–21</td></tr>
          <tr><td class="code-col">FICHE 10</td><td><span class="fam-pill fam-pt">Pâtiss.</span></td><td>Frangipane &amp; Gâteau Nantais</td><td>1. Frangipane • 2. Nantais • 3. Glaçage</td><td class="page-col">Pages 22–23</td></tr>
          <tr><td class="code-col">FICHE 11</td><td><span class="fam-pill fam-pt">Pâtiss.</span></td><td>Gamme Cookies (80 kg &amp; 160 kg)</td><td>1. Crémage → 2. Œufs → 3. Poudres</td><td class="page-col">Pages 24–25</td></tr>
          <tr><td class="code-col">FICHE 12</td><td><span class="fam-pill fam-pt">Pâtiss.</span></td><td>Cakes de Voyage (Format 3 kg)</td><td>Citron/Fruits &amp; Marbré 50/50</td><td class="page-col">Pages 26–27</td></tr>
          <tr><td class="code-col">FICHE 13</td><td><span class="fam-pill fam-tr">Traiteur</span></td><td>Gamme Quiches Traiteur (48 pcs/caisse)</td><td>1. Appareil 50/50 → 2. Garniture</td><td class="page-col">Pages 28–29</td></tr>
          <tr><td class="code-col">FICHE 14</td><td><span class="fam-pill fam-rf">Référent.</span></td><td>Référentiel Dorures &amp; Sirops</td><td>Végétale 1 L • Spéciale • Sirop 44°</td><td class="page-col">Pages 30–31</td></tr>
          <tr><td class="code-col">FICHE 15</td><td><span class="fam-pill fam-vn">Viennois.</span></td><td>Petites Brioches au Sucre (Bacs 40p)</td><td>1. Réseau V2 → 2. Huile en filet</td><td class="page-col">Pages 32–33</td></tr>
          <tr><td class="code-col">FICHE 16</td><td><span class="fam-pill fam-rf">Référent.</span></td><td>Registre Général des Cuissons</td><td>Gauche : Vienn. • Droite : Pâtiss.</td><td class="page-col">Pages 34–35</td></tr>
        </tbody>
      </table>
    </div>
    <div class="footer">
      <span>Laboratoire de Tourage, Viennoiserie &amp; Pâtisserie</span>
      <span>Table des Matières • Page 2 (Gauche)</span>
    </div>
  </div>

  <!-- PAGE 3 (DROITE) : GUIDE DE LECTURE RAPIDE & RÈGLES D'OR -->
  <div class="sheet-page">
    <div>
      <div class="header">
        <div>
          <h1>Guide des Codes Couleurs &amp; Règles d'Atelier</h1>
          <div class="subtitle">COMMENT LIRE LES TABLEAUX DE PESÉES ET CONDUIRE LES MACHINES</div>
        </div>
        <div class="badge">GUIDE • DROITE</div>
      </div>

      <div class="guide-block">
        <div class="guide-title">1. Code Couleur Chronologique des Pesées (De Haut en Bas)</div>
        <ul class="guide-list">
          <li><span class="step-pill s1">1</span> <strong>Étape 1 (Bleu) — Base Cuve / Frasage / Crémage :</strong> Tous les ingrédients portant le numéro <strong>1</strong> se pèsent ensemble et vont dans la cuve dès le démarrage du programme.</li>
          <li><span class="step-pill s2">2</span> <strong>Étape 2 (Ambre) — Incorporation 2ᵉ Phase :</strong> Ingrédients ajoutés au passage en 2ᵉ phase du programme (ex. <strong>Margarine Opale sur PLF/Kouign/Viennoise</strong>, <strong>Huile de colza en filet sur Brioche</strong>, <strong>2ᵉ Eau + Huile sur Crêpes</strong>).</li>
          <li><span class="step-pill s3">3</span> <strong>Étape 3 (Vert) — Poudres Tamisées ou Beurre de Tourage :</strong> Poudres incorporées en 3ᵉ phase (Brownie, Cookie, Muffins) ou Beurre de tourage (PLF, Kouign-Amann).</li>
          <li><span class="step-pill s4">4</span> <strong>Étape 4 (Violet) — Inclusions &amp; Finitions :</strong> Pépites de chocolat, noisettes torréfiées, noix de pécan ou fourrage apparent.</li>
        </ul>
      </div>

      <div class="guide-block amber">
        <div class="guide-title">2. Pilotage par Programmes Machines &amp; Contrôles Thermiques</div>
        <ul class="guide-list">
          <li>• <strong>Programmes Pétrins, Batteurs, Laminoir &amp; Rondo :</strong> Les temps de pétrissage et crans d'abaisse sont centralisés dans les programmes automates (voir <strong>Affiche Murale des Programmes Machines</strong> fixée aux postes).</li>
          <li>• <strong>Température sortie pétrin :</strong> PLF et Kouign-Amann à <strong>18–20 °C strict</strong> • Viennoise à <strong>19–21 °C</strong> • Brioche à l'huile à <strong>22–24 °C</strong>.</li>
          <li>• <strong>Arrêt de pousse PAC (PLF, Viennoise, Brioche) :</strong> Stopper à <strong>70 % – 75 % du volume</strong> et bloquer en cellule rapide jusqu'à <strong>-10 °C à cœur contrôlé à la sonde</strong>.</li>
        </ul>
      </div>

      <div class="guide-block red">
        <div class="guide-title">3. Dorure Végétale, Quiches IQF &amp; Découpe Zéro Chute</div>
        <ul class="guide-list">
          <li>• <strong>Dorures :</strong> Dorure Végétale (bidon 1 L) en standard au pistolet sur Croissants, Viennoises et Brioches. Dorure Spéciale Maison conservée sur Fiche 14.</li>
          <li>• <strong>Quiches Traiteur :</strong> Légumes IQF (épinards, poireaux) mis <strong>directement congelés</strong> dans les fonds avant coulage de l'appareil.</li>
        </ul>
      </div>
    </div>
    <div class="footer">
      <span>Laboratoire de Tourage, Viennoiserie &amp; Pâtisserie</span>
      <span>Guide Opérateur • Page 3 (Droite)</span>
    </div>
  </div>
</body>
</html>"""
    toc_html_file = SOURCES_DIR / "00_Sommaire.html"
    toc_pdf_file = OUTPUT_DIR / "00_Sommaire.pdf"
    toc_html_file.write_text(toc_html, encoding="utf-8")
    generate_pdf_from_html(toc_html_file, toc_pdf_file)

    # 3. Fiche Indépendante : Répertoire des Numéros de Programmes — Ligne de Production Rondo (1 Page A4 + HTML Éditable)
    poster_html = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Fiche Programmes — Ligne de Production Rondo</title>
<style>
@page { size: A4 portrait; margin: 8mm 9mm; }
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
body { width: 100%; color: #0f172a; background: #fff; }
.toolbar-no-print {
  background: #1e293b;
  color: #fff;
  padding: 10px 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
  border-radius: 6px;
}
.toolbar-no-print .hint { font-size: 13px; font-weight: 700; color: #fde68a; }
.toolbar-no-print button {
  background: #f59e0b;
  color: #0f172a;
  border: none;
  padding: 7px 13px;
  border-radius: 5px;
  font-weight: 900;
  font-size: 12.5px;
  cursor: pointer;
  margin-left: 8px;
}
.toolbar-no-print button.secondary { background: #e2e8f0; color: #0f172a; }
@media print {
  .toolbar-no-print { display: none !important; }
}
.sheet-page {
  width: 100%;
  height: 280mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.header-banner {
  background: #0f172a;
  color: #ffffff;
  border-left: 10px solid #f59e0b;
  border-radius: 7px;
  padding: 12px 18px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
.header-banner h1 { font-size: 21px; font-weight: 900; text-transform: uppercase; letter-spacing: 0.3px; }
.header-banner .sub { font-size: 12px; color: #cbd5e1; font-weight: 700; margin-top: 3px; }
.badge-mur {
  background: #f59e0b;
  color: #0f172a;
  padding: 7px 14px;
  border-radius: 5px;
  font-weight: 900;
  font-size: 13px;
  text-transform: uppercase;
}
table.poster-table {
  width: 100%;
  border-collapse: collapse;
  border: 2px solid #0f172a;
  margin-bottom: 10px;
}
table.poster-table th {
  background: #1e293b;
  color: #ffffff;
  padding: 9px 10px;
  font-size: 12px;
  font-weight: 900;
  text-transform: uppercase;
  border: 1.5px solid #334155;
  text-align: left;
}
table.poster-table th.center, table.poster-table td.center { text-align: center; }
table.poster-table td {
  padding: 8px 10px;
  height: 39px;
  border: 1.5px solid #64748b;
  font-size: 14px;
  font-weight: 800;
  color: #0f172a;
  vertical-align: middle;
}
table.poster-table tr:nth-child(even) td { background: #f8fafc; }
table.poster-table td.prog-col {
  font-size: 16px;
  font-weight: 900;
  color: #b45309;
  background: #fffbeb !important;
}
.footer {
  border-top: 2px solid #cbd5e1;
  padding-top: 6px;
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  font-weight: 800;
  color: #334155;
}
</style>
</head>
<body>
  <div class="toolbar-no-print">
    <div class="hint">✏️ Cliquez directement dans n'importe quelle case pour taper un numéro ou ajouter un nouveau produit, puis cliquez sur Imprimer.</div>
    <div>
      <button type="button" onclick="addRow()">+ Ajouter une ligne</button>
      <button type="button" class="secondary" onclick="removeRow()">- Supprimer dernière ligne</button>
      <button type="button" onclick="window.print()">🖨️ Imprimer / Enregistrer en PDF</button>
    </div>
  </div>

  <div class="sheet-page">
    <div>
      <div class="header-banner">
        <div>
          <h1 contenteditable="true">Répertoire des Programmes — Ligne Rondo</h1>
          <div class="sub" contenteditable="true">CORRESPONDANCE NUMÉROS DE PROGRAMMES RONDO &amp; PRODUITS FAÇONNÉS (PÂTE PLF &amp; AUTRES)</div>
        </div>
        <div class="badge-mur" contenteditable="true">LIGNE RONDO</div>
      </div>

      <table class="poster-table" id="rondo-table">
        <thead>
          <tr>
            <th class="center" style="width: 16%;">N° Programme</th>
            <th style="width: 28%;">Produit Façonné</th>
            <th class="center" style="width: 14%;">Pâte Mère</th>
            <th class="center" style="width: 12%;">Calibre Cru</th>
            <th style="width: 30%;">Outil de Découpe / Réglages &amp; Notes</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true">Croissant</td>
            <td class="center" contenteditable="true">PLF</td>
            <td class="center" contenteditable="true">75 g</td>
            <td contenteditable="true">Triangles — Roulage régulier</td>
          </tr>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true">Pain au Chocolat</td>
            <td class="center" contenteditable="true">PLF</td>
            <td class="center" contenteditable="true">85 g</td>
            <td contenteditable="true">Rectangles — 2 barres chocolat</td>
          </tr>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true">Pain aux Raisins</td>
            <td class="center" contenteditable="true">PLF</td>
            <td class="center" contenteditable="true">90 g</td>
            <td contenteditable="true">Crème pâtissière + raisins (boudin tranché)</td>
          </tr>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true">Pain Suisse</td>
            <td class="center" contenteditable="true">PLF</td>
            <td class="center" contenteditable="true">120 g</td>
            <td contenteditable="true">Pliage portefeuille (crème + pépites chocolat)</td>
          </tr>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true">Oranais aux Abricots</td>
            <td class="center" contenteditable="true">PLF</td>
            <td class="center" contenteditable="true">100 g</td>
            <td contenteditable="true">Carrés pliés en losange (crème + 2 oreillons)</td>
          </tr>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true">Cinnamon Roll</td>
            <td class="center" contenteditable="true">PLF</td>
            <td class="center" contenteditable="true">75 g</td>
            <td contenteditable="true">Beurre cannelle cassonade (en caissette)</td>
          </tr>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td contenteditable="true"></td>
          </tr>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td contenteditable="true"></td>
          </tr>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td contenteditable="true"></td>
          </tr>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td contenteditable="true"></td>
          </tr>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td contenteditable="true"></td>
          </tr>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td contenteditable="true"></td>
          </tr>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td contenteditable="true"></td>
          </tr>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td contenteditable="true"></td>
          </tr>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td contenteditable="true"></td>
          </tr>
          <tr>
            <td class="center prog-col" contenteditable="true"></td>
            <td contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td contenteditable="true"></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="footer">
      <span>FICHE RÉPERTOIRE • LIGNE DE PRODUCTION RONDO</span>
      <span>Modifiable au stylo sur feuille ou directement dans le fichier HTML</span>
      <span>1 PAGE A4</span>
    </div>
  </div>

<script>
function addRow() {
  const tbody = document.querySelector('#rondo-table tbody');
  const tr = document.createElement('tr');
  tr.innerHTML = `
    <td class="center prog-col" contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td class="center" contenteditable="true">PLF</td>
    <td class="center" contenteditable="true"></td>
    <td contenteditable="true"></td>
  `;
  tbody.appendChild(tr);
}
function removeRow() {
  const tbody = document.querySelector('#rondo-table tbody');
  if (tbody.rows.length > 1) {
    tbody.deleteRow(tbody.rows.length - 1);
  }
}
</script>
</body>
</html>"""
    # Suppression de l'ancienne affiche 2 pages Pétrins/Laminoir
    for old_poster in [OUTPUT_DIR / "Affiche_Murale_Programmes_Machines.pdf", SOURCES_DIR / "Affiche_Murale_Programmes_Machines.html"]:
        if old_poster.exists():
            old_poster.unlink()

    poster_html_file = SOURCES_DIR / "Affiche_Programmes_Ligne_Rondo.html"
    poster_pdf_file = OUTPUT_DIR / "Affiche_Programmes_Ligne_Rondo.pdf"
    poster_html_file.write_text(poster_html, encoding="utf-8")
    generate_pdf_from_html(poster_html_file, poster_pdf_file)
    poster_pages = len(pypdf.PdfReader(str(poster_pdf_file)).pages)
    print(f"[FICHE RONDO] {poster_pdf_file.name} -> OK ({poster_pages} page A4 dédiée Ligne Rondo)")

    # 4. Feuille Unique Indépendante : Cuissons & Recuissons d'Après-Midi (1 Page A4 + HTML Éditable)
    afternoon_html = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Repères Cuissons Après-Midi — Four 165 °C</title>
<style>
@page { size: A4 portrait; margin: 8mm 9mm; }
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
body { width: 100%; color: #0f172a; background: #fff; }
.toolbar-no-print {
  background: #1e293b;
  color: #fff;
  padding: 10px 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
  border-radius: 6px;
}
.toolbar-no-print .hint { font-size: 13px; font-weight: 700; color: #fde68a; }
.toolbar-no-print button {
  background: #f59e0b;
  color: #0f172a;
  border: none;
  padding: 7px 13px;
  border-radius: 5px;
  font-weight: 900;
  font-size: 12.5px;
  cursor: pointer;
  margin-left: 8px;
}
.toolbar-no-print button.secondary { background: #e2e8f0; color: #0f172a; }
@media print {
  .toolbar-no-print { display: none !important; }
}
.sheet-page {
  width: 100%;
  height: 280mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.header-banner {
  background: #0f172a;
  color: #ffffff;
  border-left: 10px solid #ef4444;
  border-radius: 7px;
  padding: 12px 18px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
.header-banner h1 { font-size: 21px; font-weight: 900; text-transform: uppercase; letter-spacing: 0.3px; }
.header-banner .sub { font-size: 12px; color: #cbd5e1; font-weight: 700; margin-top: 3px; }
.badge-four {
  background: #ef4444;
  color: #ffffff;
  padding: 7px 14px;
  border-radius: 5px;
  font-weight: 900;
  font-size: 15px;
  text-transform: uppercase;
}
table.cuisson-table {
  width: 100%;
  border-collapse: collapse;
  border: 2px solid #0f172a;
  margin-bottom: 10px;
}
table.cuisson-table th {
  background: #1e293b;
  color: #ffffff;
  padding: 8px 10px;
  font-size: 12px;
  font-weight: 900;
  text-transform: uppercase;
  border: 1.5px solid #334155;
  text-align: left;
}
table.cuisson-table th.center, table.cuisson-table td.center { text-align: center; }
table.cuisson-table td {
  padding: 7px 10px;
  height: 36px;
  border: 1.5px solid #64748b;
  font-size: 13.5px;
  font-weight: 800;
  color: #0f172a;
  vertical-align: middle;
}
table.cuisson-table tr:nth-child(even) td { background: #f8fafc; }
table.cuisson-table td.temp-col {
  font-size: 15px;
  font-weight: 900;
  color: #0369a1;
  background: #f0f9ff !important;
}
table.cuisson-table td.time-col {
  font-size: 16px;
  font-weight: 900;
  color: #b91c1c;
  background: #fef2f2 !important;
}
.note-box {
  background: #fffbeb;
  border: 1.5px solid #fde68a;
  border-left: 6px solid #f59e0b;
  border-radius: 5px;
  padding: 9px 12px;
  font-size: 12px;
  font-weight: 700;
  color: #92400e;
  line-height: 1.4;
  margin-bottom: 6px;
}
.footer {
  border-top: 2px solid #cbd5e1;
  padding-top: 5px;
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  font-weight: 800;
  color: #334155;
}
</style>
</head>
<body>
  <div class="toolbar-no-print">
    <div class="hint">✏️ Cliquez directement dans n'importe quelle case pour modifier un temps ou ajouter un produit, puis cliquez sur Imprimer.</div>
    <div>
      <button type="button" onclick="addRow()">+ Ajouter une ligne</button>
      <button type="button" class="secondary" onclick="removeRow()">- Supprimer dernière ligne</button>
      <button type="button" onclick="window.print()">🖨️ Imprimer / Enregistrer en PDF</button>
    </div>
  </div>

  <div class="sheet-page">
    <div>
      <div class="header-banner">
        <div>
          <h1 contenteditable="true">Cuissons &amp; Recuissons d'Après-Midi — Four 165 °C</h1>
          <div class="sub" contenteditable="true">REPÈRES RAPIDES POUR PETITES FOURNÉES • TOUS PRODUITS AU FOUR VENTILÉ À 165 °C</div>
        </div>
        <div class="badge-four" contenteditable="true">165 °C STRICT</div>
      </div>

      <table class="cuisson-table" id="afternoon-table">
        <thead>
          <tr>
            <th style="width: 28%;">Produit</th>
            <th class="center" style="width: 17%;">État au Départ</th>
            <th class="center" style="width: 14%;">Température</th>
            <th class="center" style="width: 17%;">Temps Four</th>
            <th style="width: 24%;">Consigne &amp; Finition</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td contenteditable="true"><strong>Croissant</strong></td>
            <td class="center" contenteditable="true">Congelé direct (PAC)</td>
            <td class="center temp-col" contenteditable="true">165 °C</td>
            <td class="center time-col" contenteditable="true">14 min</td>
            <td contenteditable="true">Dorure végétale • Ouvrir oura fin</td>
          </tr>
          <tr>
            <td contenteditable="true"><strong>Pain au Chocolat</strong></td>
            <td class="center" contenteditable="true">Congelé direct (PAC)</td>
            <td class="center temp-col" contenteditable="true">165 °C</td>
            <td class="center time-col" contenteditable="true">14 min</td>
            <td contenteditable="true">Dorure végétale • Ouvrir oura fin</td>
          </tr>
          <tr>
            <td contenteditable="true"><strong>Viennoise Chocolat</strong> (142 g)</td>
            <td class="center" contenteditable="true">Congelé direct (PAC)</td>
            <td class="center temp-col" contenteditable="true">165 °C</td>
            <td class="center time-col" contenteditable="true">9 min</td>
            <td contenteditable="true">Dorure végétale • Oura fermé</td>
          </tr>
          <tr>
            <td contenteditable="true"><strong>Viennoise Nature</strong> (285 g)</td>
            <td class="center" contenteditable="true">Congelé direct (PAC)</td>
            <td class="center temp-col" contenteditable="true">165 °C</td>
            <td class="center time-col" contenteditable="true">11 min</td>
            <td contenteditable="true">Dorure végétale • Oura fermé</td>
          </tr>
          <tr>
            <td contenteditable="true"><strong>Kouign-Amann (Décongélation)</strong></td>
            <td class="center" contenteditable="true">Ressorti congélateur</td>
            <td class="center temp-col" contenteditable="true">165 °C</td>
            <td class="center time-col" contenteditable="true">4 min</td>
            <td contenteditable="true">Remise en T° rapide • Ne pas recuire</td>
          </tr>
          <tr>
            <td contenteditable="true"><strong>Chausson aux Pommes</strong></td>
            <td class="center" contenteditable="true">Congelé ou Frais</td>
            <td class="center temp-col" contenteditable="true">165 °C</td>
            <td class="center time-col" contenteditable="true">30 min</td>
            <td contenteditable="true">Dorure pinceau • Bien sécher fin</td>
          </tr>
          <tr>
            <td contenteditable="true"><strong>Croissant aux Amandes</strong></td>
            <td class="center" contenteditable="true">Garni crème amande</td>
            <td class="center temp-col" contenteditable="true">165 °C</td>
            <td class="center time-col" contenteditable="true">30 min</td>
            <td contenteditable="true">Sucre glace après refroidissement</td>
          </tr>
          <tr>
            <td contenteditable="true"><strong>Petite Brioche au Sucre</strong> (60 g)</td>
            <td class="center" contenteditable="true">Congelé direct (PAC)</td>
            <td class="center temp-col" contenteditable="true">165 °C</td>
            <td class="center time-col" contenteditable="true">11 à 13 min</td>
            <td contenteditable="true">Dorure vég. + Sucre Grain 10</td>
          </tr>
          <tr>
            <td contenteditable="true"><strong>Cookies</strong> (80 g)</td>
            <td class="center" contenteditable="true">Congelé direct</td>
            <td class="center temp-col" contenteditable="true">165 °C</td>
            <td class="center time-col" contenteditable="true">13 à 14 min</td>
            <td contenteditable="true">Ouras ouverts en continu</td>
          </tr>
          <tr>
            <td contenteditable="true"><strong>Pain Raisins / Suisse / Oranais</strong></td>
            <td class="center" contenteditable="true">Congelé direct (PAC)</td>
            <td class="center temp-col" contenteditable="true">165 °C</td>
            <td class="center time-col" contenteditable="true">15 à 16 min</td>
            <td contenteditable="true">Sirop 44° chaud (Raisins / Oranais)</td>
          </tr>
          <tr>
            <td contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td class="center temp-col" contenteditable="true">165 °C</td>
            <td class="center time-col" contenteditable="true"></td>
            <td contenteditable="true"></td>
          </tr>
          <tr>
            <td contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td class="center temp-col" contenteditable="true">165 °C</td>
            <td class="center time-col" contenteditable="true"></td>
            <td contenteditable="true"></td>
          </tr>
          <tr>
            <td contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td class="center temp-col" contenteditable="true">165 °C</td>
            <td class="center time-col" contenteditable="true"></td>
            <td contenteditable="true"></td>
          </tr>
          <tr>
            <td contenteditable="true"></td>
            <td class="center" contenteditable="true"></td>
            <td class="center temp-col" contenteditable="true">165 °C</td>
            <td class="center time-col" contenteditable="true"></td>
            <td contenteditable="true"></td>
          </tr>
        </tbody>
      </table>

      <div class="note-box">
        💡 <strong>Règle d'or de l'après-midi :</strong> Une petite fournée (1 ou 2 plaques) cuit plus vite qu'un chariot plein du matin. Les temps sont indicatifs : <strong>toujours contrôler la coloration à l'œil sur les 2 dernières minutes</strong>. Tous les produits viennoiserie PAC s'enfournent directement congelés.
      </div>
    </div>

    <div class="footer">
      <span>FICHE ATELIER • RECUISSONS APRÈS-MIDI</span>
      <span>Poste Four Ventilé • Température Unique 165 °C</span>
      <span>1 PAGE A4</span>
    </div>
  </div>

<script>
function addRow() {
  const tbody = document.querySelector('#afternoon-table tbody');
  const tr = document.createElement('tr');
  tr.innerHTML = `
    <td contenteditable="true"></td>
    <td class="center" contenteditable="true">Congelé direct (PAC)</td>
    <td class="center temp-col" contenteditable="true">165 °C</td>
    <td class="center time-col" contenteditable="true"></td>
    <td contenteditable="true"></td>
  `;
  tbody.appendChild(tr);
}
function removeRow() {
  const tbody = document.querySelector('#afternoon-table tbody');
  if (tbody.rows.length > 1) {
    tbody.deleteRow(tbody.rows.length - 1);
  }
}
</script>
</body>
</html>"""
    afternoon_html_file = SOURCES_DIR / "Affiche_Cuissons_Apres_Midi.html"
    afternoon_pdf_file = OUTPUT_DIR / "Affiche_Cuissons_Apres_Midi.pdf"
    afternoon_html_file.write_text(afternoon_html, encoding="utf-8")
    generate_pdf_from_html(afternoon_html_file, afternoon_pdf_file)
    afternoon_pages = len(pypdf.PdfReader(str(afternoon_pdf_file)).pages)
    print(f"[FICHE CUISSONS APRÈS-MIDI] {afternoon_pdf_file.name} -> OK ({afternoon_pages} page A4 dédiée Recuissons)")

    # Suppression de l'ancienne annexe 06b si présente
    for old_f in [OUTPUT_DIR / "06b_PLF_Annexe_Faconnages_Rondo.pdf", SOURCES_DIR / "06b_PLF_Annexe_Faconnages_Rondo.html"]:
        if old_f.exists():
            old_f.unlink()

    print("\n=== ASSEMBLAGE DU LIVRE COMPLET RELIÉ EN DOUBLE PAGE VIS-À-VIS (35 PAGES) ===")
    writer = pypdf.PdfWriter()
    writer.append(str(cover_pdf_file))
    writer.append(str(toc_pdf_file))
    for _, pdf_path in individual_pdfs:
        writer.append(str(pdf_path))
        
    master_pdf = OUTPUT_DIR / "Cahier_Recettes_Complet_Labo.pdf"
    with open(master_pdf, "wb") as f_out:
        writer.write(f_out)
        
    total_pages = len(pypdf.PdfReader(str(master_pdf)).pages)
    print(f"-> Cahier Complet généré avec succès : {master_pdf.name} ({total_pages} pages au total).")
    
    if has_error or total_pages != 35:
        print(f"ATTENTION : Pagination inattendue ({total_pages} pages au lieu de 35) !")
        sys.exit(1)
    else:
        print("\n[V] PARFAIT : 16/16 fiches en Double Page stricte (2 pages chacune). Cahier complet 35/35 pages.")

if __name__ == "__main__":
    main()
