import os
import re
import json

CATALOGUE_DIR = '/home/toto/.gemini/antigravity/scratch/laboratoire-tourage-boulangerie/recettes/catalogue'

POLES_ORDER = [
    ("1. VIENNOISERIES FEUILLETÉES & TOURAGE", [
        "croissant-pac-excellence.md",
        "pain-chocolat-equerre-pac.md",
        "pain-raisins-escargot-pac.md",
        "pain-suisse-chocolatine-pac.md",
        "oranais-abricots-pac.md",
        "cinnamon-roll-feuillete-pac.md",
        "cruffin-atelier-pac.md",
        "kouign-amann-pac.md",
        "feuilletage-inverse-universel.md",
    ]),
    ("2. VIENNOISERIE GÉNÉRALE & PÂTES LEVÉES", [
        "v-vie-01-pain-viennois-nature-pac.md",
        "v-vie-02-pain-viennois-chocolat-pac.md",
        "brioche-individuelle-sucre-pac.md",
    ]),
    ("3. PÂTISSERIE BOULANGÈRE & ÉPIPHANIE", [
        "frangipane-galette-rois-pac.md",
        "galettes-rois-variations-pomme-poire-nutolade.md",
        "gateau-nantais-traditionnel.md",
    ]),
    ("4. BISCUITERIE, CAKES & SNACKING", [
        "brookie-cadres-60x40.md",
        "brownie-fondant-chocolat.md",
        "cookies-classique-noisette.md",
        "muffins-gamme-atelier.md",
        "cakes-de-voyage.md",
    ]),
    ("5. CRÊPERIE, TRAITEUR & RÉFÉRENTIELS", [
        "crepes-froment-girocrepes.md",
        "galettes-ble-noir-girocrepes.md",
        "quiches-traiteur.md",
        "dorures-et-sirops-referentiel.md",
    ]),
]

def clean_text(s):
    s = re.sub(r'\*\*(.*?)\*\*', r'\1', s)
    s = re.sub(r'\*(.*?)\*', r'\1', s)
    s = re.sub(r'`(.*?)`', r'\1', s)
    s = re.sub(r'\$(.*?)\$', r'\1', s)
    s = s.replace('—', '-').replace('➔', '->').replace('→', '->')
    s = re.sub(r'[\U00010000-\U0010ffff\u2600-\u27bf\u2b50\ufe0f]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def parse_markdown_tables(text):
    tables = []
    lines = text.splitlines()
    cur_table = []
    for line in lines:
        s = line.strip()
        if s.startswith('|') and s.endswith('|'):
            cells = [c.strip() for c in s.split('|')[1:-1]]
            if all(re.match(r'^:?-+:?$', c) for c in cells if c):
                continue
            cur_table.append(cells)
        else:
            if cur_table:
                tables.append(cur_table)
                cur_table = []
    if cur_table:
        tables.append(cur_table)
    return tables

def extract_recipe(filepath, pole_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    lines = text.splitlines()
    
    raw_title = next((l[2:].strip() for l in lines if l.startswith('# ')), os.path.basename(filepath))
    title = clean_text(raw_title)
    for prefix in ["Fiche Technique d'Atelier :", "CAHIER TECHNIQUE R&D :", "FICHE TECHNIQUE D'ATELIER :", "Cahier de Laboratoire R&D •", "RÉFÉRENTIEL GÉNÉRAL :"]:
        title = title.replace(prefix, "").strip()
    title = title.replace("- FORMAT DOUBLE-PAGE", "").strip()

    code_m = re.search(r'`([A-Z]+-[A-Z]+-\d+[^`]*)`', text)
    code = code_m.group(1) if code_m else "ATELIER"

    tables = parse_markdown_tables(text)
    
    weigh_table = None
    for t in tables:
        hdr = " ".join(t[0]).lower()
        if any(bad in hdr for bad in ['paramètre clé', 'repère', 'symptôme', 'défaut']):
            continue
        if any(k in hdr for k in ['ingrédient', 'composant', 'matière', 'diamètre']):
            body_str = " ".join(" ".join(r) for r in t[1:])
            if 'g' in body_str or 'kg' in body_str:
                weigh_table = t
                break
    if not weigh_table and tables:
        # fallback: pick table with 'g' and not 'paramètre clé'
        candidates = [t for t in tables if 'paramètre clé' not in " ".join(t[0]).lower()]
        if candidates:
            weigh_table = max(candidates, key=len)

    clean_headers = []
    clean_rows = []
    if weigh_table and len(weigh_table) > 1:
        hdrs = [clean_text(h) for h in weigh_table[0]]
        keep_indices = []
        ing_idx = 0
        phase_idx = -1
        for i, h in enumerate(hdrs):
            hl = h.lower()
            if any(k in hl for k in ['phase', 'ordre', 'bloc', 'étape']):
                if i <= 1:
                    phase_idx = i
            elif any(k in hl for k in ['ingrédient', 'composant', 'matière', 'paramètre']):
                ing_idx = i
            elif any(k in hl for k in ['%', 'base 1', 'rôle', 'spécification', 'biochimique', 'objectif', 'justification', 'tolérance', 'remarque']):
                continue
            else:
                keep_indices.append(i)
        
        keep_indices = keep_indices[:3]
        clean_headers = [hdrs[ing_idx]] + [hdrs[i] for i in keep_indices]
        
        for r in weigh_table[1:]:
            if len(r) <= ing_idx:
                continue
            ing_name = clean_text(r[ing_idx])
            if not ing_name:
                continue
            phase_raw = clean_text(r[phase_idx]) if phase_idx >= 0 and phase_idx < len(r) else ""
            
            row_type = "normal"
            dot = ""
            if any(k in ing_name.upper() for k in ['SOUS-TOTAL', 'SOUS TOTAL', 'DÉTREMPE', 'PÂTE AU BAC']):
                row_type = "subtotal"
            if any(k in ing_name.upper() for k in ['TOTAL PÂTON', 'POIDS TOTAL', 'MASSE TOTALE', 'TOTAL COMPLET', 'TOTAL GARNITURE']):
                row_type = "total"
            
            if '[1]' in phase_raw or '1' == phase_raw or 'bleu' in phase_raw.lower():
                dot = "dot-1"
            elif '[2]' in phase_raw or '2' == phase_raw or 'ambre' in phase_raw.lower():
                dot = "dot-2"
            elif '[3]' in phase_raw or '[4]' in phase_raw or '3' == phase_raw or 'vert' in phase_raw.lower():
                dot = "dot-3"

            cols = []
            for idx in keep_indices:
                val = clean_text(r[idx]) if idx < len(r) else "-"
                cols.append(val)
            
            clean_rows.append({
                "type": row_type,
                "dot": dot,
                "ingredient": ing_name,
                "cols": cols
            })

    return {
        "file": os.path.basename(filepath),
        "pole": pole_name,
        "code": code,
        "title": title,
        "headers": clean_headers,
        "rows": clean_rows
    }

data = []
for pole, filenames in POLES_ORDER:
    for fn in filenames:
        fp = os.path.join(CATALOGUE_DIR, fn)
        if os.path.exists(fp):
            d = extract_recipe(fp, pole)
            data.append(d)
            print(f"OK: {d['code']:10s} | {len(d['rows']):2d} rows | cols={d['headers'][1:]} | {d['title'][:45]}")

with open('/home/toto/.gemini/antigravity/scratch/laboratoire-tourage-boulangerie/scripts/extracted_summary.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
