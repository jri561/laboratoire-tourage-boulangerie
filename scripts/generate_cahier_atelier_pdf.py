#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur PDF « Chrono Unifié » — Cahier de Production & Fiches d'Atelier
Format A4 portrait strict (210 × 297 mm) en double-page face-à-face.
- En-tête blanc sobre + Mémo Express horizontal en haut
- Tableau pleine largeur avec cases à cocher ☐, colonne principale en gros gras,
  et bandeaux de phases colorés (01 Bleu, 02 Ambre, 03 Vert)
- Instructions Page Droite reliées au même code couleur 01/02/03 avec gros repères chiffrés
"""

import os
import re
import html
import subprocess

BASE_DIR = "/home/toto/.gemini/antigravity/scratch/laboratoire-tourage-boulangerie"
FICHES_DIR = os.path.join(BASE_DIR, "recettes/fiches_atelier_operateurs")
EXPORT_DIR = os.path.join(BASE_DIR, "exports_pdf")

CSS_BASE = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}

body {
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #1c1917;
    background-color: #ffffff;
    font-size: 8.6pt;
    line-height: 1.3;
    margin: 0;
    padding: 0;
    font-variant-numeric: tabular-nums;
    font-feature-settings: "tnum" 1;
}

.page-sheet {
    width: 100%;
    height: 267mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-after: always;
    break-after: page;
    overflow: hidden;
}

.page-sheet:last-child {
    page-break-after: auto;
    break-after: auto;
}

.page-content {
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
    gap: 3.5px;
}

/* === COUVERTURE SOMBRE === */
.cover-sheet {
    width: 210mm;
    height: 296.5mm;
    background-color: #0f172a;
    color: #ffffff;
    padding: 20mm 18mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-after: always;
    break-after: page;
    overflow: hidden;
}

.cover-kicker {
    font-size: 9pt;
    font-weight: 800;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #fbbf24;
    margin-bottom: 6mm;
}

.cover-title {
    font-size: 30pt;
    font-weight: 900;
    line-height: 1.06;
    letter-spacing: -0.02em;
    margin: 0 0 5mm 0;
    color: #ffffff;
}

.cover-subtitle {
    font-size: 11.5pt;
    font-weight: 500;
    color: #cbd5e1;
    margin: 0 0 10mm 0;
    max-width: 155mm;
}

.cover-accent-bar {
    width: 28mm;
    height: 1.6mm;
    background-color: #b45309;
    margin-bottom: 10mm;
}

.cover-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4.5mm;
}

.cover-card {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-left: 4px solid #2563eb;
    border-radius: 4px;
    padding: 4.5mm 5mm;
}

.cover-card.c-amber { border-left-color: #d97706; }
.cover-card.c-green { border-left-color: #16a34a; }

.cover-card-num {
    font-size: 8pt;
    font-weight: 800;
    color: #93c5fd;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 1.5mm;
}

.cover-card.c-amber .cover-card-num { color: #fcd34d; }
.cover-card.c-green .cover-card-num { color: #86efac; }

.cover-card-title {
    font-size: 11pt;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 1.5mm;
}

.cover-card-desc {
    font-size: 8.5pt;
    color: #cbd5e1;
    line-height: 1.35;
}

.cover-footer {
    border-top: 1px solid #334155;
    padding-top: 4mm;
    display: flex;
    justify-content: space-between;
    font-size: 8.5pt;
    color: #94a3b8;
    font-weight: 600;
}

/* === EN-TÊTE ÉPURÉ === */
.cu-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #0f172a;
    padding-bottom: 2mm;
    margin-bottom: 2.5mm;
}

.cu-head-left {
    display: flex;
    flex-direction: column;
    padding-right: 4mm;
}

.cu-kicker {
    display: none;
}

.cu-title {
    font-size: 15pt;
    font-weight: 800;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: #0f172a;
    margin: 0;
}

.cu-sub {
    font-size: 8pt;
    color: #64748b;
    font-weight: 500;
    margin-top: 0.8mm;
}

.cu-pill {
    border: 1.5px solid #0f172a;
    color: #0f172a;
    background-color: #ffffff;
    padding: 1.2mm 3.2mm;
    border-radius: 3px;
    font-weight: 800;
    font-size: 7.5pt;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    white-space: nowrap;
}

.cu-pill.green {
    border-color: #0f172a;
    background-color: #0f172a;
    color: #ffffff;
}

.page-sheet.dense .cu-head {
    padding-bottom: 1.4mm;
    margin-bottom: 1.2mm;
}
.page-sheet.dense .cu-title { font-size: 13.5pt; }

/* === MÉMO EXPRESS (TUILES HAUTES) === */
.memo-strip {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2.2mm;
    margin: 0 0 2.5mm 0;
}

.m-card {
    background-color: #faf8f5;
    border: 1px solid #e7e5e4;
    border-top: 3.5px solid #1e40af;
    border-radius: 3px;
    padding: 1.8mm 2.5mm;
}

.m-card.amber { border-top-color: #b45309; }
.m-card.green { border-top-color: #15803d; }

.m-v {
    font-size: 12.5pt;
    font-weight: 900;
    color: #1c1917;
    line-height: 1.1;
}

.m-l {
    font-size: 6.6pt;
    font-weight: 700;
    text-transform: uppercase;
    color: #78716c;
    margin-top: 0.6mm;
    letter-spacing: 0.03em;
}

/* === TITRES DE SECTION ÉPURÉS === */
.sec-h {
    display: flex;
    align-items: baseline;
    gap: 2mm;
    border-bottom: 1.5px solid #0f172a;
    padding-bottom: 1mm;
    margin: 4px 0 2px 0;
}

.sec-num {
    display: none;
}

.sec-t {
    font-size: 9.5pt;
    font-weight: 800;
    text-transform: uppercase;
    color: #0f172a;
    letter-spacing: 0.03em;
}

.sec-k {
    display: none;
}

.page-sheet.dense .sec-h {
    margin: 1.5px 0 1px 0;
    padding-bottom: 0.8mm;
}
.page-sheet.dense .sec-t { font-size: 8.8pt; }

/* === TABLEAUX PLEINE LARGEUR === */
.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1px 0 3px 0;
    font-size: 8.6pt;
    font-variant-numeric: tabular-nums;
}

.data-table th {
    text-align: left;
    font-size: 7pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: #57534e;
    border-bottom: 2px solid #1c1917;
    padding: 2.5px 4px;
}

.data-table th.num,
.data-table td.num {
    text-align: right;
    font-weight: 700;
}

.data-table td.num {
    white-space: nowrap;
}

.data-table th.main-col {
    background-color: #eff6ff;
    color: #1e3a8a;
    font-size: 7.5pt;
}

.data-table td.main-col {
    background-color: #eff6ff;
    color: #0f172a;
    font-weight: 900;
    font-size: 10.2pt;
    padding-right: 6px;
}

.data-table td {
    padding: 2.8px 4px;
    border-bottom: 1px solid #f0ede8;
    color: #1c1917;
    vertical-align: middle;
}

.data-table td.chk {
    width: 6mm;
    text-align: center;
    font-size: 10pt;
    color: #a8a29e;
    padding: 1px 2px;
}

/* Séparateurs de phase sobres dans le tableau */
.data-table tr.p-band td {
    font-size: 7pt;
    font-weight: 800;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    padding: 3px 4px 1.5px 4px;
    color: #475569;
    background-color: #f8fafc;
    border-top: 1px solid #cbd5e1;
    border-bottom: 1px solid #e2e8f0;
}

.data-table tr.row-subtotal td {
    background-color: #f5f5f4;
    font-weight: 800;
    color: #1c1917;
    border-top: 1.5px solid #a8a29e;
    border-bottom: 1.5px solid #a8a29e;
}
.data-table tr.row-subtotal td.main-col {
    background-color: #dbeafe;
    color: #1e3a8a;
}

.data-table tr.row-total td {
    background-color: #1c1917;
    font-weight: 900;
    font-size: 9pt;
    color: #ffffff;
    border: none;
    padding: 3.5px 4px;
}
.data-table tr.row-total td.num {
    color: #e7e5e4;
}
.data-table tr.row-total td.main-col {
    background-color: #1e40af;
    color: #ffffff;
    font-size: 11pt;
}

/* Variantes densité */
.data-table.compact { font-size: 7.7pt; }
.data-table.compact th { font-size: 6.6pt; padding: 1.8px 3.5px; }
.data-table.compact td { padding: 1.8px 3.5px; }
.data-table.compact td.main-col { font-size: 9pt; }
.data-table.compact tr.row-total td { font-size: 8.2pt; }
.data-table.compact tr.row-total td.main-col { font-size: 9.5pt; }

.data-table.ultra-compact {
    font-size: 6.8pt;
    line-height: 1.12;
    margin: 1px 0 2px 0;
}
.data-table.ultra-compact th { font-size: 6.2pt; padding: 1.2px 3px; }
.data-table.ultra-compact td { padding: 1.2px 3px; }
.data-table.ultra-compact td.main-col { font-size: 7.8pt; }
.data-table.ultra-compact tr.p-band td { font-size: 6.4pt; padding: 1.2px 4px; }
.data-table.ultra-compact tr.row-total td { font-size: 7.2pt; padding: 2px 3px; }
.data-table.ultra-compact tr.row-total td.main-col { font-size: 8.2pt; }

.data-table.wide { font-size: 7.4pt; }
.data-table.wide th { font-size: 6.4pt; padding: 1.8px 3px; }
.data-table.wide td { padding: 1.8px 3px; }
.data-table.wide th:first-child,
.data-table.wide td:first-child { width: 32%; }
.data-table.wide td.num { white-space: normal; }
.data-table.wide td.main-col { font-size: 8.4pt; }

.data-table.wide-text {
    width: 100%;
    font-size: 7.2pt;
}
.data-table.wide-text th:first-child,
.data-table.wide-text td:first-child {
    width: 30%;
}
.data-table.wide-text th,
.data-table.wide-text td {
    overflow-wrap: break-word;
    white-space: normal;
}

/* Modes agrandis pour pages de pesée aérées (occupent la page sans vide inutile) */
.data-table.large-tbl { font-size: 10.6pt; margin: 4px 0 8px 0; }
.data-table.large-tbl th { font-size: 8.2pt; padding: 6px 6px; }
.data-table.large-tbl td { padding: 7.5px 6px; }
.data-table.large-tbl td.main-col { font-size: 13.2pt; }
.data-table.large-tbl tr.p-band td { font-size: 8pt; padding: 6px 6px 3px 6px; }
.data-table.large-tbl tr.row-total td { font-size: 11pt; padding: 8.5px 6px; }
.data-table.large-tbl tr.row-total td.main-col { font-size: 14pt; }

.data-table.xl-tbl { font-size: 12.5pt; margin: 8px 0 14px 0; }
.data-table.xl-tbl th { font-size: 9pt; padding: 9px 8px; }
.data-table.xl-tbl td { padding: 13px 8px; }
.data-table.xl-tbl td.main-col { font-size: 16pt; }
.data-table.xl-tbl tr.p-band td { font-size: 8.8pt; padding: 10px 8px 5px 8px; }
.data-table.xl-tbl tr.row-total td { font-size: 13pt; padding: 13px 8px; }
.data-table.xl-tbl tr.row-total td.main-col { font-size: 17pt; }

/* === LISTE D'ÉTAPES ÉPURÉE (PAGE DROITE) === */
.step-rows {
    display: flex;
    flex-direction: column;
    margin: 1px 0 4px 0;
}

.s-row {
    display: grid;
    grid-template-columns: 26mm 1fr;
    border-bottom: 1px solid #e2e8f0;
    padding: 2mm 0;
    background-color: #ffffff;
}

.s-row:last-child {
    border-bottom: none;
}

.s-left {
    padding-right: 3mm;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
}

.s-val {
    font-size: 10pt;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.15;
}

.s-lbl {
    font-size: 6.8pt;
    font-weight: 600;
    color: #64748b;
    margin-top: 0.3mm;
}

.s-right {
    padding: 0;
    display: block;
    font-size: 8.4pt;
    color: #334155;
    line-height: 1.32;
}

.s-right strong.st {
    color: #0f172a;
    font-size: 8.8pt;
    display: block;
    margin-bottom: 0.4mm;
}

/* === LISTES SOBRES & PARAGRAPHES === */
.clean-list {
    margin: 1px 0 3px 14px;
    padding: 0;
    font-size: 8.1pt;
    color: #1c1917;
}
.clean-list li { margin-bottom: 1.5px; }
.note-line {
    font-size: 7.9pt;
    color: #57534e;
    margin: 1px 0 2px 0;
}

/* === ENCADRÉ RÈGLE D'OR / CRITIQUE === */
.alert-critical {
    background-color: #fef2f2;
    border: 1.5px solid #ef4444;
    border-left: 5px solid #dc2626;
    border-radius: 4px;
    color: #7f1d1d;
    font-size: 8.2pt;
    font-weight: 800;
    text-transform: uppercase;
    text-align: center;
    padding: 2.2mm 3.5mm;
    margin-top: auto;
    letter-spacing: 0.02em;
}

/* === PIED DE PAGE DISCRET === */
.page-footer {
    border-top: 1px solid #e7e5e4;
    padding-top: 1.6mm;
    margin-top: 1.5mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.4pt;
    color: #78716c;
    font-weight: 700;
}
"""

CSS_BOOK_MARGINS = """
@page { size: A4 portrait; margin: 15mm 14mm 14mm 18mm; }
@page :first { margin: 0; }
@page :left { margin: 15mm 18mm 14mm 14mm; }
@page :right { margin: 15mm 14mm 14mm 18mm; }
"""

CSS_SHEET_MARGINS = """
@page { size: A4 portrait; margin: 15mm 14mm 14mm 18mm; }
@page :first { margin: 15mm 18mm 14mm 14mm; }
@page :left { margin: 15mm 18mm 14mm 14mm; }
@page :right { margin: 15mm 14mm 14mm 18mm; }
"""


def clean_inline(text: str) -> str:
    """Formate le Markdown inline (gras, italique, code) en HTML propre."""
    text = html.escape(text)
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.*?)`', r'\1', text)
    text = text.replace('$\\rightarrow$', '→').replace('$\\ge$', '≥').replace('$\\le$', '≤').replace('$\\pm$', '±')
    text = re.sub(r'\$([^$]+)\$', r'\1', text)
    return text


def is_numeric_cell(raw: str) -> bool:
    s = re.sub(r'[*`]', '', raw).strip()
    if re.match(r'^(\+?\s*[0-9]|~[0-9]|—|-|PM$)', s):
        return True
    if any(u in s for u in (' g', ' kg', ' pcs', ' p.', ' min', ' °C', ' mm', ' cm')):
        if re.search(r'\d', s) and len(s) < 28:
            return True
    return False


def phase_key(raw: str) -> tuple[str, str]:
    """Associe une phase Markdown à son code couleur (p1=Bleu, p2=Ambre, p3=Vert) et son libellé."""
    s = re.sub(r'[*`\[\]]', '', raw).strip().upper()
    if s in ('1', 'A', '1 A', '1 B'):
        return 'p1', f'PHASE {s} • BASE / FRASAGE'
    if s in ('2', 'B', 'C'):
        return 'p2', f'PHASE {s} • AJOUT / ÉMULSION'
    if s in ('3', '4', 'D', 'OPTION', '4 A', '4 B', '3 B', 'DÉCOR', 'FOURRAGE'):
        return 'p3', f'PHASE {s} • TOURAGE / FINITION'
    return 'p4', s


def render_table(table_lines: list[str], force_ultra_compact: bool = False, scale_cls: str = "") -> str:
    if len(table_lines) < 2:
        return ""
    headers = [p.strip() for p in table_lines[0].strip('|').split('|')]
    rows = []
    for ln in table_lines[2:]:
        cells = [p.strip() for p in ln.strip('|').split('|')]
        if cells:
            rows.append(cells)

    has_phase_col = bool(headers and headers[0].strip().lower() in ('phase', 'étape', 'bloc'))
    # Pour les tableaux avec colonne Phase/Ingrédient, on remplace la colonne Phase par des bandeaux colorés
    # et on ajoute une colonne case à cocher ☐ pour l'opérateur au poste de balance.
    use_checklist = has_phase_col and len(headers) >= 3

    num_cols = set()
    for c_idx in range(len(headers)):
        h_low = headers[c_idx].strip().lower()
        if c_idx == 0 or (use_checklist and c_idx == 1) or h_low in ('étape', 'phase', 'bloc'):
            continue
        matches = sum(1 for r in rows if c_idx < len(r) and is_numeric_cell(r[c_idx]))
        if rows and matches >= max(1, len(rows) // 2):
            num_cols.add(c_idx)

    # Première colonne numérique mise en avant (généralement 1 Bac / 1 Moule / Lot Std)
    main_num_col = min(num_cols) if num_cols else None

    classes = ["data-table"]
    if force_ultra_compact:
        classes.append("ultra-compact")
    elif len(rows) > 15:
        classes.append("compact")
    elif scale_cls:
        classes.append(scale_cls)
    eff_cols = len(headers) if not use_checklist else len(headers)
    if eff_cols >= 5 and not scale_cls:
        classes.append("wide")
    if eff_cols >= 4 and any(len(c) > 35 for r in rows for c in r):
        classes.append("wide-text")

    out = [f'<table class="{" ".join(classes)}"><thead><tr>']
    if use_checklist:
        for c_idx in range(1, len(headers)):
            cls_parts = []
            if c_idx in num_cols:
                cls_parts.append("num")
            if c_idx == main_num_col:
                cls_parts.append("main-col")
            cls = f' class="{" ".join(cls_parts)}"' if cls_parts else ''
            out.append(f'<th{cls}>{clean_inline(headers[c_idx])}</th>')
    else:
        for c_idx, h in enumerate(headers):
            cls_parts = []
            if c_idx in num_cols:
                cls_parts.append("num")
            if c_idx == main_num_col:
                cls_parts.append("main-col")
            cls = f' class="{" ".join(cls_parts)}"' if cls_parts else ''
            out.append(f'<th{cls}>{clean_inline(h)}</th>')
    out.append('</tr></thead><tbody>')

    last_phase = None
    colspan = len(headers) - 1 if use_checklist else len(headers)

    for r in rows:
        lbl_upper = (r[0] + " " + (r[1] if len(r) > 1 else "")).upper()
        tr_cls = ""
        if "SOUS-TOTAL" in lbl_upper or "SOUS-BLOC" in lbl_upper or "S-TOT" in lbl_upper:
            tr_cls = ' class="row-subtotal"'
        elif "TOTAL" in r[0].upper() or "MASSE" in r[0].upper():
            tr_cls = ' class="row-total"'

        if use_checklist and not tr_cls:
            p_cls, p_lbl = phase_key(r[0])
            if p_cls != last_phase:
                out.append(f'<tr class="p-band {p_cls}"><td colspan="{colspan}">{html.escape(p_lbl)}</td></tr>')
                last_phase = p_cls

        out.append(f'<tr{tr_cls}>')
        if use_checklist:
            for c_idx in range(1, len(headers)):
                val = r[c_idx] if c_idx < len(r) else ""
                cls_parts = []
                if c_idx in num_cols:
                    cls_parts.append("num")
                if c_idx == main_num_col:
                    cls_parts.append("main-col")
                cls = f' class="{" ".join(cls_parts)}"' if cls_parts else ''
                out.append(f'<td{cls}>{clean_inline(val)}</td>')
        else:
            for c_idx in range(len(headers)):
                val = r[c_idx] if c_idx < len(r) else ""
                cls_parts = []
                if c_idx in num_cols:
                    cls_parts.append("num")
                if c_idx == main_num_col:
                    cls_parts.append("main-col")
                cls = f' class="{" ".join(cls_parts)}"' if cls_parts else ''
                out.append(f'<td{cls}>{clean_inline(val)}</td>')
        out.append('</tr>')
    out.append('</tbody></table>')
    return "\n".join(out)


def render_kpi_from_table(table_lines: list[str]) -> str:
    """Transforme un tableau Repères Flash (<= 3 lignes) en bandeau Mémo Express 3 tuiles."""
    rows = []
    for ln in table_lines[2:]:
        cells = [p.strip() for p in ln.strip('|').split('|')]
        if len(cells) >= 2:
            rows.append(cells)
    if not rows:
        return ""
    accents = ["", " amber", " green"]
    out = ['<div class="memo-strip">']
    for idx, r in enumerate(rows[:3]):
        lbl = clean_inline(r[0])
        val = clean_inline(r[1])
        out.append(f'<div class="m-card{accents[idx % 3]}"><div class="m-v">{val}</div><div class="m-l">{lbl}</div></div>')
    out.append('</div>')
    return "\n".join(out)


def extract_step_metric(stitle: str, sbody: str, num: str) -> tuple[str, str]:
    """Extrait un repère chiffré (durée, température, puis dimension/poids) pour le bloc gauche."""
    m_paren = re.search(r'\(([^)\[\]]*\d[^)\[\]]*)\)', stitle)
    if m_paren:
        val = m_paren.group(1).strip()
        if not re.match(r'^[\d\s.,]+$', val) and len(val) <= 18:
            return val, f"ÉTAPE {num}"
    plain = re.sub(r'[*`]', '', sbody)

    # Priorité 1 : durées avec minutes+secondes (ex. "4 min 30 s à 5 min" -> "4'30–5 min")
    m_min_sec = re.search(r'(\d+)\s*min\s*(\d+)\s*(?:s\b|sec)?\s*(?:à|[–-])\s*(\d+)\s*min', plain)
    if m_min_sec:
        val = f"{m_min_sec.group(1)}'{m_min_sec.group(2)}–{m_min_sec.group(3)} min"
        return val, f"ÉTAPE {num}"

    # Priorité 2 : durées simples ou plages (min, sec, s, h)
    m_dur = re.search(
        r'(?<![\d.,])(\d+(?:[.,]\d+)?(?:\s*(?:[–-]|à)\s*\d+(?:[.,]\d+)?)?\s*(?:min|sec|s\b|h\b))',
        plain,
    )
    if m_dur:
        val = re.sub(r'\s+', ' ', m_dur.group(1).strip()).replace(' à ', '–')
        if len(val) <= 18:
            return val, f"ÉTAPE {num}"

    # Priorité 3 : températures (°C), y compris "19 °C à 21 °C" -> "19–21 °C"
    m_temp_range = re.search(r'([-+]?\s*\d+(?:[.,]\d+)?)\s*°C\s*(?:à|[–-])\s*([-+]?\s*\d+(?:[.,]\d+)?)\s*°C', plain)
    if m_temp_range:
        t1 = m_temp_range.group(1).replace(' ', '')
        t2 = m_temp_range.group(2).replace(' ', '')
        val = f"{t1}–{t2} °C"
        if len(val) <= 18:
            return val, f"ÉTAPE {num}"
    m_temp = re.search(
        r'(?<![\d.,])([-+]?\s*\d+(?:[.,]\d+)?(?:\s*(?:[–-]|à)\s*[-+]?\s*\d+(?:[.,]\d+)?)?\s*°C)',
        plain,
    )
    if m_temp:
        val = re.sub(r'\s+', ' ', m_temp.group(1).strip()).replace('- ', '-').replace('+ ', '+').replace(' à ', '–')
        if len(val) <= 18:
            return val, f"ÉTAPE {num}"

    # Priorité 4 (fallback) : dimensions / poids / pourcentages
    m_val = re.search(
        r'(?<![\d.,])(?<!\d )([-+]?\s*\d+(?:\s\d{3})*(?:[.,]\d+)?(?:\s*[–-]\s*[-+]?\s*\d+(?:\s\d{3})*(?:[.,]\d+)?)?\s*(?:mm|cm|g\b|kg|%)|≥\s*\d+\s*\w+)',
        plain,
    )
    if m_val:
        val = re.sub(r'\s+', ' ', m_val.group(1).strip()).replace('- ', '-').replace('+ ', '+')
        if len(val) <= 18:
            return val, f"ÉTAPE {num}"
    return f"ÉTAPE {num}", "CONSIGNE"


def render_page_body(md_block: str, is_right: bool) -> tuple[str, str, bool]:
    """Convertit une demi-fiche Markdown (gauche ou droite) en HTML structuré Chrono Unifié."""
    lines = md_block.strip().splitlines()
    # Estimer la hauteur réelle sur page (en tenant compte des multi-tableaux et tableaux larges)
    total_tbl_rows = 0
    num_tables = 0
    max_cols = 0
    in_reperes = False
    in_tbl = False
    for ln in lines:
        st = ln.strip()
        if st.startswith('### ') or st.startswith('#### '):
            in_reperes = "repères flash" in st.lower()
            in_tbl = False
        elif not in_reperes and st.startswith('|'):
            if not re.match(r'^\|\s*[-:]+', st):
                total_tbl_rows += 1
                max_cols = max(max_cols, len(st.strip('|').split('|')))
                if not in_tbl:
                    num_tables += 1
                    in_tbl = True
        else:
            in_tbl = False

    is_dense = (total_tbl_rows > 18) or (total_tbl_rows >= 15 and max_cols >= 6)
    scale_cls = ""
    if not is_right and not is_dense:
        if total_tbl_rows <= 9 and num_tables == 1:
            scale_cls = "xl-tbl"
        elif total_tbl_rows <= 15 and max_cols <= 5:
            scale_cls = "large-tbl"
    blocks = []
    alert_html = ""
    sec_num = 0
    i = 0
    step_cards = []
    phase_classes = ['p1', 'p2', 'p3', 'p4']

    def flush_steps():
        nonlocal step_cards
        if step_cards:
            blocks.append('<div class="step-rows">' + "".join(step_cards) + '</div>')
            step_cards = []

    while i < len(lines):
        s = lines[i].strip()
        if not s or s == '---' or s.startswith('## PAGE '):
            i += 1
            continue

        # Titre de section
        if s.startswith('### ') or s.startswith('#### '):
            flush_steps()
            title = s.lstrip('#').strip()
            if "repères flash" in title.lower():
                j = i + 1
                while j < len(lines) and not lines[j].strip().startswith('|'):
                    j += 1
                while j < len(lines) and lines[j].strip().startswith('|'):
                    j += 1
                i = j
                continue

            sec_num += 1
            clean_t = re.sub(r'^\d+\.\s*', '', title)
            p_cls = phase_classes[min(sec_num - 1, 3)]
            num_badge = f"{sec_num:02d}"
            # Extraire éventuelle info clé entre parenthèses à la fin du titre pour le badge KPI à droite
            kpi_badge = ""
            m_end = re.search(r'\(([^)]+)\)\s*$', clean_t)
            if m_end and len(m_end.group(1)) <= 26:
                kpi_badge = f'<span class="sec-k">{clean_inline(m_end.group(1))}</span>'
                clean_t = clean_t[:m_end.start()].strip()
            blocks.append(
                f'<div class="sec-h">'
                f'<span class="sec-num {p_cls}">{num_badge}</span>'
                f'<span class="sec-t">{clean_inline(clean_t)}</span>'
                f'{kpi_badge}</div>'
            )
            i += 1
            continue

        # Tableaux
        if s.startswith('|'):
            flush_steps()
            tbl = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                tbl.append(lines[i].strip())
                i += 1
            blocks.append(render_table(tbl, force_ultra_compact=is_dense, scale_cls=scale_cls))
            continue

        # Cartes d'étapes numérotées (1. **Titre :** texte)
        m_step = re.match(r'^(\d+)\.\s+\*\*(.*?)\*\*\s*(.*)$', s)
        if m_step and is_right:
            num, stitle, sbody = m_step.groups()
            stitle = stitle.rstrip(':').strip()
            sbody = sbody.lstrip(':').strip()
            sub_bullets = []
            j = i + 1
            while j < len(lines) and (lines[j].startswith('   -') or lines[j].startswith('   *')):
                sub_bullets.append(lines[j].strip()[2:].strip())
                j += 1
            if sub_bullets:
                sbody = (sbody + " " if sbody else "") + " • ".join(sub_bullets)
                i = j
            else:
                i += 1
            p_cls = phase_classes[min(max(sec_num - 1, 0), 3)]
            m_val, m_lbl = extract_step_metric(stitle, sbody, num)
            if m_lbl == "CONSIGNE":
                left_step_html = f'<div class="s-left"><span class="s-lbl" style="margin-top:0;font-size:8pt;font-weight:700;">Étape {num}</span></div>'
            else:
                left_step_html = f'<div class="s-left"><span class="s-val">{clean_inline(m_val)}</span></div>'
            step_cards.append(
                f'<div class="s-row">'
                f'{left_step_html}'
                f'<div class="s-right"><strong class="st">{clean_inline(stitle)}</strong>{clean_inline(sbody)}</div>'
                f'</div>'
            )
            continue

        # Listes à puces
        if s.startswith('- ') or s.startswith('* '):
            flush_steps()
            items = []
            while i < len(lines) and (lines[i].strip().startswith('- ') or lines[i].strip().startswith('* ')):
                txt = lines[i].strip()[2:].strip()
                if is_right and ("INTERDICTION" in txt.upper() or ("OURA" in txt.upper() and "FERMÉ" in txt.upper() and "STRICTEMENT" in txt.upper())):
                    alert_html = f'<div class="alert-critical">{clean_inline(txt)}</div>'
                else:
                    items.append(f'<li>{clean_inline(txt)}</li>')
                i += 1
            if items:
                blocks.append('<ul class="clean-list">' + "".join(items) + '</ul>')
            continue

        # Callout / Alerte
        if s.startswith('> '):
            flush_steps()
            q_lines = []
            while i < len(lines) and lines[i].strip().startswith('> '):
                q_lines.append(lines[i].strip()[2:].strip())
                i += 1
            q_text = " ".join(q_lines)
            if is_right or "INTERDIT" in q_text.upper() or "ATTENTION" in q_text.upper():
                alert_html = f'<div class="alert-critical">{clean_inline(q_text)}</div>'
            else:
                blocks.append(f'<p class="note-line">{clean_inline(q_text)}</p>')
            continue

        flush_steps()
        blocks.append(f'<p class="note-line">{clean_inline(s)}</p>')
        i += 1

    flush_steps()
    return "\n".join(blocks), alert_html, is_dense


def parse_fiche_pages(md_path: str, page_start: int, total_pages: int) -> list[str]:
    text = open(md_path, encoding='utf-8').read()
    lines = text.splitlines()

    title = ""
    meta = ""
    body_lines = []
    for idx, ln in enumerate(lines):
        if idx == 0 and ln.startswith('# '):
            title = ln[2:].strip()
        elif idx <= 2 and ln.startswith('**'):
            meta = ln.strip()
        else:
            body_lines.append(ln)

    body_text = "\n".join(body_lines)
    parts = body_text.split('<!-- PAGE_BREAK -->')
    left_md = parts[0] if len(parts) > 0 else ""
    right_md = parts[1] if len(parts) > 1 else ""

    left_html, left_alert, left_dense = render_page_body(left_md, is_right=False)
    right_html, right_alert, right_dense = render_page_body(right_md, is_right=True)

    section_label = title
    left_cls = "page-sheet dense" if left_dense else "page-sheet"
    right_cls = "page-sheet dense" if right_dense else "page-sheet"

    # Nettoyer le sous-titre (retirer les codes internes "Codes : ...")
    clean_meta_parts = [p.strip() for p in meta.split('|') if not re.match(r'^\*\*Codes?\s*:', p.strip(), re.I)]
    meta_html = f'<div class="cu-sub">{clean_inline(" | ".join(clean_meta_parts))}</div>' if clean_meta_parts else ''

    page_left = f"""
    <div class="{left_cls}">
      <div class="page-content">
        <div class="cu-head">
          <div class="cu-head-left">
            <h1 class="cu-title">{clean_inline(title)}</h1>
            {meta_html}
          </div>
          <div class="cu-pill">PESÉE</div>
        </div>
        {left_html}
        {left_alert}
      </div>
      <footer class="page-footer">
        <span>{clean_inline(section_label)}</span>
        <span>{page_start} / {total_pages}</span>
      </footer>
    </div>
    """

    page_right = f"""
    <div class="{right_cls}">
      <div class="page-content">
        <div class="cu-head">
          <div class="cu-head-left">
            <h1 class="cu-title">{clean_inline(title)}</h1>
            {meta_html}
          </div>
          <div class="cu-pill green">FABRICATION</div>
        </div>
        {right_html}
        {right_alert}
      </div>
      <footer class="page-footer">
        <span>{clean_inline(section_label)}</span>
        <span>{page_start + 1} / {total_pages}</span>
      </footer>
    </div>
    """
    return [page_left, page_right]


def build_cover_html() -> str:
    return """
    <div class="cover-sheet">
      <div>
        <div class="cover-kicker">LABORATOIRE DE TOURAGE &amp; BOULANGERIE • EDITION CHRONO UNIFIÉ</div>
        <h1 class="cover-title">CAHIER DE PRODUCTION<br>&amp; FICHES D'ATELIER</h1>
        <div class="cover-accent-bar"></div>
        <p class="cover-subtitle">Fiches de pesée, fabrication, façonnage et cuisson pour la production quotidienne.</p>

        <div class="cover-grid">
          <div class="cover-card">
            <div class="cover-card-num">PÔLE 1 • FICHES 01 – 02</div>
            <div class="cover-card-title">Pâte Levée Feuilletée (PLF)</div>
            <div class="cover-card-desc">Détrempe commune, tourage 1D + 1S (12 couches) et 7 façonnages sur Rondo Polyline &amp; Croissomat SCM50.</div>
          </div>
          <div class="cover-card">
            <div class="cover-card-num">PÔLE 2 • FICHES 03 – 04</div>
            <div class="cover-card-title">Pains Viennois &amp; Brioches PAC</div>
            <div class="cover-card-desc">Méthode directe : Pains Viennois 280 g &amp; 140 g, Petites Brioches au Sucre 75 g.</div>
          </div>
          <div class="cover-card c-amber">
            <div class="cover-card-num">PÔLE 3 • FICHE 05</div>
            <div class="cover-card-title">Kouign-Amann Breton</div>
            <div class="cover-card-desc">Beurre manié sucré (3 820 g/bac), individuels 100 g &amp; partage 400/600 g en octogone.</div>
          </div>
          <div class="cover-card c-amber">
            <div class="cover-card-num">PÔLE 4 • FICHES 06 – 07</div>
            <div class="cover-card-title">Feuilletage Inversé &amp; Épiphanie</div>
            <div class="cover-card-desc">Feuilletage 48 couches, Frangipane, Pommes &amp; Poire-Nutolade.</div>
          </div>
          <div class="cover-card c-green">
            <div class="cover-card-num">PÔLE 5 • FICHES 08 – 13</div>
            <div class="cover-card-title">Biscuiterie &amp; Gâteaux de Voyage</div>
            <div class="cover-card-desc">Cookies coupe-fil 80 g, Muffins 120 g, Brownie &amp; Brookie en cadres 56×36 cm, Cakes &amp; Nantais.</div>
          </div>
          <div class="cover-card c-green">
            <div class="cover-card-num">PÔLE 6 • FICHES 14 – 17</div>
            <div class="cover-card-title">Girocrêpes, Traiteur &amp; Cuissons</div>
            <div class="cover-card-desc">Crêpes froment, Galettes blé noir, Quiches, Dorures, Sirop 44° et barèmes de cuisson.</div>
          </div>
        </div>
      </div>

      <div class="cover-footer">
        <span>CONFORME PRODUCTION QUOTIDIENNE • IMPRESSION RECTO-VERSO RELIURE CENTRALE</span>
        <span>37 PAGES • DOUBLE-PAGE A4</span>
      </div>
    </div>
    """


def build_sommaire_pages(total_pages: int) -> list[str]:
    p1 = f"""
    <div class="page-sheet dense">
      <div class="page-content">
        <div class="cu-head">
          <div class="cu-head-left">
            <h1 class="cu-title">Sommaire des Recettes</h1>
            <div class="cu-sub">Cahier de production • Fiches 01 à 18</div>
          </div>
          <div class="cu-pill">PAGES 2 – {total_pages}</div>
        </div>

        <table class="data-table">
          <thead><tr><th>Fiche</th><th>Pôle</th><th>Produits</th><th class="num">Pages</th></tr></thead>
          <tbody>
            <tr><td><strong>01</strong></td><td>Pôle 1 • PLF</td><td><strong>Pâte Levée Feuilletée (Recette commune)</strong></td><td class="num">2 – 3</td></tr>
            <tr><td><strong>02</strong></td><td>Pôle 1 • PLF</td><td><strong>Façonnages &amp; Calibres PLF (5 produits)</strong></td><td class="num">4 – 5</td></tr>
            <tr><td><strong>03</strong></td><td>Pôle 2 • Pâtes Levées</td><td><strong>Pains Viennois Nature &amp; Pépites Chocolat</strong></td><td class="num">6 – 7</td></tr>
            <tr><td><strong>04</strong></td><td>Pôle 2 • Pâtes Levées</td><td><strong>Petite Brioche au Sucre</strong></td><td class="num">8 – 9</td></tr>
            <tr><td><strong>05</strong></td><td>Pôle 3 • Breton</td><td><strong>Kouign-Amann Individuel &amp; Partage</strong></td><td class="num">10 – 11</td></tr>
            <tr><td><strong>06</strong></td><td>Pôle 4 • Feuilletage</td><td><strong>Feuilletage Inversé &amp; Plaques Pâtisserie</strong></td><td class="num">12 – 13</td></tr>
            <tr><td><strong>07</strong></td><td>Pôle 4 • Épiphanie</td><td><strong>Galettes des Rois (Frangipane, Pommes, Poire-Nutolade)</strong></td><td class="num">14 – 15</td></tr>
            <tr><td><strong>08</strong></td><td>Pôle 5 • Biscuiterie</td><td><strong>Cookies Classique &amp; Chocolat-Noisette</strong></td><td class="num">16 – 17</td></tr>
            <tr><td><strong>09</strong></td><td>Pôle 5 • Biscuiterie</td><td><strong>Muffins Pépites / Cœur Nutolade &amp; Noisette</strong></td><td class="num">18 – 19</td></tr>
            <tr><td><strong>10</strong></td><td>Pôle 5 • Biscuiterie</td><td><strong>Brownie Fondant Chocolat &amp; Noix</strong></td><td class="num">20 – 21</td></tr>
            <tr><td><strong>11</strong></td><td>Pôle 5 • Biscuiterie</td><td><strong>Brookie</strong></td><td class="num">22 – 23</td></tr>
            <tr><td><strong>12</strong></td><td>Pôle 5 • Biscuiterie</td><td><strong>Cakes de Voyage (Citron Pavot, Marbré)</strong></td><td class="num">24 – 25</td></tr>
            <tr><td><strong>13</strong></td><td>Pôle 5 • Biscuiterie</td><td><strong>Gâteau Nantais</strong></td><td class="num">26 – 27</td></tr>
            <tr><td><strong>14</strong></td><td>Pôle 6 • Girocrêpes</td><td><strong>Crêpes de Froment</strong></td><td class="num">28 – 29</td></tr>
            <tr><td><strong>15</strong></td><td>Pôle 6 • Girocrêpes</td><td><strong>Galettes de Blé Noir</strong></td><td class="num">30 – 31</td></tr>
            <tr><td><strong>16</strong></td><td>Pôle 6 • Traiteur</td><td><strong>Quiches (Lorraine, Chèvre-Épinards, Poireaux)</strong></td><td class="num">32 – 33</td></tr>
            <tr><td><strong>17</strong></td><td>Pôle 6 • Finitions</td><td><strong>Dorures, Sirop 44° &amp; Barèmes de Cuisson</strong></td><td class="num">34 – 35</td></tr>
            <tr><td><strong>18</strong></td><td>Pôle 5 • Biscuiterie</td><td><strong>Pain d'Épices (Lingots 280 g)</strong></td><td class="num">36 – 37</td></tr>
          </tbody>
        </table>
      </div>
      <footer class="page-footer">
        <span>SOMMAIRE GÉNÉRAL</span>
        <span>1 / {total_pages}</span>
      </footer>
    </div>
    """
    return [p1]


def compile_html_to_pdf(body_html: str, css_margins: str, out_name: str, title: str):
    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
<style>{CSS_BASE}\n{css_margins}</style>
</head>
<body>
{body_html}
</body>
</html>"""
    html_out = os.path.join(EXPORT_DIR, f"{out_name}.html")
    pdf_out = os.path.join(EXPORT_DIR, f"{out_name}.pdf")
    with open(html_out, "w", encoding="utf-8") as f:
        f.write(full_html)
    cmd = [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_out}",
        html_out,
    ]
    subprocess.run(cmd, capture_output=True, text=True, check=True)
    if os.path.exists(pdf_out):
        print(f"  [PDF OK] {out_name}.pdf ({os.path.getsize(pdf_out):,} octets)")
    return pdf_out


def build_pdf():
    os.makedirs(EXPORT_DIR, exist_ok=True)
    print("=== GÉNÉRATION DES PDFS « CHRONO UNIFIÉ » ===")

    fiches_ordered = [
        ("01-recette-maitresse-plf-commune.md", "01_Recette_Maitresse_PLF_Commune", "Fiche 01 - Recette Maîtresse PLF Commune"),
        ("02-annexe-faconnages-et-calibres-plf.md", "02_Annexe_Faconnages_Calibres_PLF", "Fiche 02 - Façonnages & Calibres PLF"),
        ("03-fiche-atelier-pain-viennois-nature-et-chocolat-pac.md", "03_Pain_Viennois_Nature_Chocolat_PAC", "Fiche 03 - Pains Viennois PAC"),
        ("04-fiche-atelier-petite-brioche-sucre-pac.md", "04_Petite_Brioche_Sucre_PAC", "Fiche 04 - Petite Brioche au Sucre PAC"),
        ("05-fiche-atelier-kouign-amann.md", "05_Kouign_Amann_Individuel_Partage", "Fiche 05 - Kouign-Amann"),
        ("06-fiche-atelier-feuilletage-inverse-universel.md", "06_Feuilletage_Inverse_Universel", "Fiche 06 - Feuilletage Inversé"),
        ("07-fiche-atelier-galettes-rois-epiphanie-gamme.md", "07_Galettes_Rois_Epiphanie_Gamme", "Fiche 07 - Galettes des Rois Épiphanie"),
        ("08-fiche-atelier-cookies-classique-noisette.md", "08_Cookies_Classique_Noisette", "Fiche 08 - Cookies Coupe-Fil 80 g"),
        ("09-fiche-atelier-muffins-gamme-atelier.md", "09_Muffins_Gamme_Atelier", "Fiche 09 - Muffins Gamme Atelier"),
        ("10-fiche-atelier-brownie-fondant-chocolat.md", "10_Brownie_Fondant_Noix", "Fiche 10 - Brownie Cadres 56x36"),
        ("11-fiche-atelier-brookie-cadres-60x40.md", "11_Brookie_Cadres_56x36", "Fiche 11 - Brookie Cadres 56x36"),
        ("12-fiche-atelier-cakes-de-voyage.md", "12_Cakes_de_Voyage_Mix", "Fiche 12 - Cakes de Voyage"),
        ("13-fiche-atelier-gateau-nantais.md", "13_Gateau_Nantais_OPAL", "Fiche 13 - Gâteau Nantais"),
        ("14-fiche-atelier-crepes-froment-girocrepes.md", "14_Crepes_Froment_Girocrepes", "Fiche 14 - Crêpes Froment Girocrêpes"),
        ("15-fiche-atelier-galettes-ble-noir-girocrepes.md", "15_Galettes_Ble_Noir_Girocrepes", "Fiche 15 - Galettes Blé Noir Girocrêpes"),
        ("16-fiche-atelier-quiches-traiteur.md", "16_Quiches_Traiteur", "Fiche 16 - Quiches Traiteur"),
        ("17-fiche-atelier-dorures-sirops-et-cuissons.md", "17_Dorures_Sirops_Et_Cuissons", "Fiche 17 - Dorures, Sirops & Cuissons"),
        ("18-fiche-atelier-pain-depices.md", "18_Pain_dEpices_Lingots_280g", "Fiche 18 - Pain d'Épices (Lingots 280 g)"),
    ]

    total_book_pages = 1 + 2 * len(fiches_ordered)  # 37 pages
    book_chunks = build_sommaire_pages(total_book_pages)
    cur_page = 2
    for md_name, _, _ in fiches_ordered:
        fpath = os.path.join(FICHES_DIR, md_name)
        book_chunks.extend(parse_fiche_pages(fpath, cur_page, total_book_pages))
        cur_page += 2

    book_html = "\n".join(book_chunks)
    compile_html_to_pdf(book_html, CSS_BOOK_MARGINS, "Cahier_Recettes_Complet_Labo", "Cahier de Production Chrono Unifié")

    for md_name, out_name, title in fiches_ordered:
        fpath = os.path.join(FICHES_DIR, md_name)
        pages = parse_fiche_pages(fpath, 1, 2)
        compile_html_to_pdf("\n".join(pages), CSS_SHEET_MARGINS, out_name, title)

    plf_pages = parse_fiche_pages(os.path.join(FICHES_DIR, "01-recette-maitresse-plf-commune.md"), 1, 4)
    plf_pages += parse_fiche_pages(os.path.join(FICHES_DIR, "02-annexe-faconnages-et-calibres-plf.md"), 3, 4)
    compile_html_to_pdf("\n".join(plf_pages), CSS_SHEET_MARGINS, "01_02_PLF_Commune_Et_Faconnages", "Fiches 01-02 - PLF Commune & Façonnages")

    print("=> Génération terminée avec succès.")


if __name__ == "__main__":
    build_pdf()
