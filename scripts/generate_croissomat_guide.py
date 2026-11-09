import os
from PIL import Image, ImageDraw, ImageFont

img_path = '/home/toto/.gemini/antigravity/brain/bc31aa75-d0a6-4b32-9375-bab1b5922ed5/.user_uploaded/media_1794223680196_9f222d58.jpg'
out_path = '/home/toto/.gemini/antigravity/brain/bc31aa75-d0a6-4b32-9375-bab1b5922ed5/guide_reglages_croissomat.png'

im = Image.open(img_path).convert("RGBA")
W, H = im.size

# Create an overlay for crisp graphics
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
    font_badge = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 13)
    font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
except Exception:
    font_title = font_badge = font_text = font_sub = ImageFont.load_default()

# 1. Title Banner Top
draw.rectangle([(0, 0), (W, 42)], fill=(15, 23, 42, 230))
draw.text((20, 8), "RONDO CROISSOMAT SCM50 • GUIDE DES 3 RÉGLAGES D'ENROULEUR (75g)", fill=(245, 158, 11, 255), font=font_title)

# Knobs definitions
knobs = [
    {
        "id": "1",
        "name": "COMMANDE 1 : ENTRÉE / AMORCE",
        "sub": "Hauteur bord d'attaque : 5 à 6 mm",
        "desc": "Accrochage doux de la base (3,5 mm) sans écrasement",
        "badge_pos": (370, 240),
        "box_pos": (20, 140, 310, 230),
        "arrow_start": (360, 255),
        "arrow_end": (310, 185),
        "color": (59, 130, 246), # Blue
    },
    {
        "id": "2",
        "name": "COMMANDE 2 : SORTIE / PENTE",
        "sub": "Dégagement rouleau : 28 à 32 mm",
        "desc": "Profil divergent : sortie libre du rouleau 3-4 spires",
        "badge_pos": (670, 210),
        "box_pos": (700, 140, 990, 230),
        "arrow_start": (660, 225),
        "arrow_end": (700, 185),
        "color": (16, 185, 129), # Green
    },
    {
        "id": "3",
        "name": "COMMANDE 3 : SERRAGE & CLÉ",
        "sub": "Cambrure tablier : Roulage souple",
        "desc": "3,5 spires aérées (nid d'abeille) + Clé sous le pâton (6h)",
        "badge_pos": (440, 600),
        "box_pos": (20, 480, 340, 580),
        "arrow_start": (430, 580),
        "arrow_end": (340, 530),
        "color": (239, 68, 68), # Red
    }
]

for k in knobs:
    bx1, by1, bx2, by2 = k["box_pos"]
    r, g, b = k["color"]
    # Draw card box
    draw.rectangle([(bx1, by1), (bx2, by2)], fill=(15, 23, 42, 235), outline=(r, g, b, 255), width=2)
    # Badge inside box
    draw.rectangle([(bx1+8, by1+8), (bx1+32, by1+32)], fill=(r, g, b, 255))
    draw.text((bx1+14, by1+10), k["id"], fill=(255, 255, 255, 255), font=font_badge)
    # Title
    draw.text((bx1+40, by1+10), k["name"], fill=(255, 255, 255, 255), font=font_text)
    # Sub & desc
    draw.text((bx1+12, by1+40), k["sub"], fill=(245, 158, 11, 255), font=font_text)
    draw.text((bx1+12, by1+62), k["desc"], fill=(203, 213, 225, 255), font=font_sub)

    # Circle on knob
    cx, cy = k["badge_pos"]
    draw.ellipse([(cx-25, cy-25), (cx+25, cy+25)], outline=(r, g, b, 255), width=4)
    draw.ellipse([(cx-12, cy-12), (cx+12, cy+12)], fill=(r, g, b, 220))
    draw.text((cx-6, cy-9), k["id"], fill=(255, 255, 255, 255), font=font_badge)

    # Connector line
    draw.line([k["arrow_start"], k["arrow_end"]], fill=(r, g, b, 255), width=2)

# Composite and save
final_img = Image.alpha_composite(im, overlay)
final_img.convert("RGB").save(out_path, "PNG")
print("Croissomat guide generated successfully:", out_path)
