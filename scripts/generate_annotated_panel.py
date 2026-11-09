import os
from PIL import Image, ImageDraw, ImageFont

# Load original image
orig_path = '/home/toto/.gemini/antigravity/brain/bc31aa75-d0a6-4b32-9375-bab1b5922ed5/.user_uploaded/media_1794213420765_3a2fa12e.jpg'
orig = Image.open(orig_path)

# Canvas dimensions: 1920 x 1080 (Full HD)
canvas_w, canvas_h = 1920, 1080
canvas = Image.new('RGB', (canvas_w, canvas_h), color=(18, 24, 32)) # Deep premium slate background
draw = ImageDraw.Draw(canvas)

# Try loading standard font or fall back
try:
    font_title = ImageFont.truetype('/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf', 28)
    font_subtitle = ImageFont.truetype('/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf', 16)
    font_sec = ImageFont.truetype('/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf', 16)
    font_item = ImageFont.truetype('/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf', 13)
    font_desc = ImageFont.truetype('/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf', 12)
    font_badge = ImageFont.truetype('/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf', 13)
except Exception:
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()
    font_sec = ImageFont.load_default()
    font_item = ImageFont.load_default()
    font_desc = ImageFont.load_default()
    font_badge = ImageFont.load_default()

# 1. Prepare panel image on the left
# Crop: x: 120 to 760, y: 160 to 860
crop_box = (120, 160, 760, 860)
panel_crop = orig.crop(crop_box)
panel_h = 960
scale = panel_h / panel_crop.height
panel_w = int(panel_crop.width * scale)
panel_resized = panel_crop.resize((panel_w, panel_h), Image.Resampling.LANCZOS)

# Paste panel onto canvas (margin 40px left, 60px top)
panel_x, panel_y = 40, 60
canvas.paste(panel_resized, (panel_x, panel_y))

# Draw border around panel
draw.rectangle([panel_x - 2, panel_y - 2, panel_x + panel_w + 2, panel_y + panel_h + 2], outline=(70, 90, 120), width=2)

# Helper function to convert orig (x, y) to canvas (x, y)
def to_canvas(ox, oy):
    cx = panel_x + int((ox - crop_box[0]) * scale)
    cy = panel_y + int((oy - crop_box[1]) * scale)
    return cx, cy

# 2. Header
draw.text((canvas_w // 2 - 200, 15), "RONDO POLYLINE • GUIDE DES TOUCHES ET RÉGLAGES MACHINE", fill=(255, 255, 255), font=font_title)

# Define Key Hotspots / Badges
# Format: (Number, Label, Category, OriginalX, OriginalY, Description, WorkshopValue)
items = [
    (1, "ARRÊT D'URGENCE", "Sécurité", 388, 388, "Coup de poing rouge. Coupe immédiate moteurs & prises.", "Réarmement : 1/4 tour"),
    (2, "AFFICHAGE VALEUR", "Affichage", 350, 508, "Afficheur LED rouge de la valeur sélectionnée (% ou mm).", "Suisse: 48 | Oranais: 120"),
    (3, "SAISIE [-] / [+] / [↵]", "Saisie", 415, 508, "Touches de réglage -/+ et validation Entrée de la consigne.", "Incrément pas à pas"),
    (4, "N° PROGRAMME", "Recettes", 500, 508, "Affiche la recette active de 1 à 99 mémorisable.", "Prog 1: Suisse | 2: Raisin"),
    (5, "LISTE & SAUVEGARDE", "Recettes", 550, 508, "Haut: Rappel programme | Bas: Disquette (appui 2s = save).", "Mémorisation recettes"),
    (6, "VITESSE TAPIS (%)", "Ligne", 228, 575, "Règle la vitesse du tapis convoyeur de 0,5 à 8 m/min.", "Atelier : 35 % à 45 %"),
    (7, "LONGUEUR COUPE (mm)", "Ligne", 228, 630, "Pas d'avance du tapis entre chaque coup de guillotine.", "Suisse 48mm | Oranais 120mm"),
    (8, "VITESSE ACCESSOIRES", "Ligne", 228, 755, "Règle la vitesse du moteur de l'accessoire sélectionné.", "Doseuse / Épandeur en %"),
    (9, "GUILLOTINE ON/OFF", "Outils", 285, 575, "Active/coupe la guillotine transversale (LED verte).", "ON pour Suisse & Oranais"),
    (10, "MODE COUPE STOP/GO", "Outils", 348, 575, "Tapis s'arrête net à la coupe (évite le déchirement).", "Obligatoire Stop-and-Go"),
    (11, "DOSEUSE CONTINUE", "Dépose", 285, 625, "Dépose continue en ruban synchronisée au tapis.", "Pain Suisse (4 cordons)"),
    (12, "DOSEUSE CADENCÉE", "Dépose", 348, 625, "Dépose par plots intermittents à intervalle fixe.", "Oranais (1 plot de 25g/carré)"),
    (13, "ÉPANDEUR INCLUSIONS", "Dépose", 415, 625, "Active le saupoudreur de chocolat / raisins.", "Suisse : 15g pépites 50%"),
    (14, "ENROULEUR BOUDIN", "Façonnage", 415, 575, "Active l'enrouleur transversal pour former le boudin.", "Pain aux Raisins (Ø 48mm)"),
    (15, "TEST MANUEL / PURGE", "Manuel", 348, 670, "Touches 🖐️ : purge doseuse, test lame unitaire, test grains.", "Amorçage tuyaux crème"),
    (16, "RESET BLEU [R]", "Commande", 530, 615, "Réarmement défauts + Remonte la lame au Point Mort Haut.", "Après ouverture carter"),
    (17, "START TAPIS [I]", "Commande", 470, 650, "Lance le tapis convoyeur et les outils synchronisés.", "Démarrage fabrication"),
    (18, "STOP GÉNÉRAL [0]", "Commande", 530, 705, "Arrêt net du tapis et suspension du dosage/coupe.", "Pause ou fin de bande"),
    (19, "PRISE (1) GUILLOTINE", "Accessoires", 290, 755, "Prise motorisée 1 : Guillotine transversale.", "Vitesse & dwell time"),
    (20, "PRISE (2) DOSEUSE", "Accessoires", 355, 755, "Prise motorisée 2 : Doseuse 4 buses crème.", "Débit régulé 35g ou 25g"),
    (21, "PRISE (3) ÉPANDEUR", "Accessoires", 420, 755, "Prise motorisée 3 : Épandeur de pépites / raisins.", "Débit pépites / raisins"),
    (22, "PRISE (4) ENROULEUR", "Accessoires", 485, 755, "Prise motorisée 4 : Enrouleur transversal boudin.", "Vitesse roulage boudin")
]

# Colors by category
cat_colors = {
    "Sécurité": (220, 50, 50),
    "Affichage": (240, 180, 20),
    "Saisie": (240, 180, 20),
    "Recettes": (255, 140, 0),
    "Ligne": (46, 204, 113),
    "Outils": (52, 152, 219),
    "Dépose": (155, 89, 182),
    "Façonnage": (230, 126, 34),
    "Manuel": (149, 165, 166),
    "Commande": (46, 204, 113),
    "Accessoires": (26, 188, 156)
}

# Draw badges on panel
for num, label, cat, ox, oy, desc, wval in items:
    cx, cy = to_canvas(ox, oy)
    color = cat_colors.get(cat, (255, 255, 255))
    
    # Outer glow
    draw.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=(0, 0, 0, 180), outline=(255, 255, 255), width=2)
    draw.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], fill=color)
    
    # Text number
    num_str = str(num)
    bbox = font_badge.getbbox(num_str)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((cx - tw // 2, cy - th // 2 - 2), num_str, fill=(255, 255, 255), font=font_badge)

# 3. Right Legend Panel
legend_x = panel_x + panel_w + 30
legend_w = canvas_w - legend_x - 30
legend_y = 60

# Background card for legend
draw.rectangle([legend_x, legend_y, legend_x + legend_w, legend_y + panel_h], fill=(26, 34, 46), outline=(70, 90, 120), width=2)

# Legend Header
draw.rectangle([legend_x, legend_y, legend_x + legend_w, legend_y + 40], fill=(35, 47, 64))
draw.text((legend_x + 15, legend_y + 10), "INDEX DÉTAILLÉ DES TOUCHES & FONCTIONS OPÉRATOIRES", fill=(255, 255, 255), font=font_sec)

# Render legend rows (in two columns if needed or clean grid)
# 22 items -> 2 columns of 11 items
col_w = legend_w // 2 - 15
row_h = 75

for i, (num, label, cat, ox, oy, desc, wval) in enumerate(items):
    c_idx = 0 if i < 11 else 1
    r_idx = i if i < 11 else i - 11
    
    rx = legend_x + 15 + c_idx * (col_w + 15)
    ry = legend_y + 50 + r_idx * row_h
    
    color = cat_colors.get(cat, (255, 255, 255))
    
    # Badge
    draw.ellipse([rx, ry + 2, rx + 24, ry + 26], fill=color, outline=(255, 255, 255), width=1)
    n_str = str(num)
    bbox = font_badge.getbbox(n_str)
    draw.text((rx + 12 - (bbox[2] - bbox[0]) // 2, ry + 14 - (bbox[3] - bbox[1]) // 2 - 2), n_str, fill=(255, 255, 255), font=font_badge)
    
    # Label & Category tag
    draw.text((rx + 32, ry), label, fill=(255, 255, 255), font=font_item)
    # Tag
    draw.text((rx + 32, ry + 18), f"[{cat.upper()}] {desc}", fill=(180, 200, 220), font=font_desc)
    # Workshop Value
    draw.text((rx + 32, ry + 36), f"⚙️ Règlage : {wval}", fill=(240, 200, 90), font=font_desc)

# Save result
output_path = '/home/toto/.gemini/antigravity/scratch/laboratoire-tourage-boulangerie/guide_visuel_panneau_polyline_rondo.png'
canvas.save(output_path, 'PNG')
# Also copy to artifact dir
artifact_path = '/home/toto/.gemini/antigravity/brain/bc31aa75-d0a6-4b32-9375-bab1b5922ed5/guide_visuel_panneau_polyline_rondo.png'
canvas.save(artifact_path, 'PNG')
print('Annotated poster generated successfully:', output_path)
