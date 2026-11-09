import os
from PIL import Image, ImageDraw, ImageFont

img_path = '/home/toto/.gemini/antigravity/brain/bc31aa75-d0a6-4b32-9375-bab1b5922ed5/.user_uploaded/media_1794223680196_9f222d58.jpg'
out_path = '/home/toto/.gemini/antigravity/brain/bc31aa75-d0a6-4b32-9375-bab1b5922ed5/guide_croissomat_scm50_sens_reel.png'

im = Image.open(img_path).convert("RGBA")
W, H = im.size

overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    font_badge = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 17)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 13)
    font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
except Exception:
    font_title = font_badge = font_text = font_sub = ImageFont.load_default()

# 1. Title Banner Top with Flow Arrow
draw.rectangle([(0, 0), (W, 46)], fill=(15, 23, 42, 240))
draw.text((20, 10), "SENS DE LA PÂTE : DROITE ---> GAUCHE (ENROULEUR SCM50)", fill=(245, 158, 11, 255), font=font_title)

# Draw a large direction arrow banner in the background
draw.rectangle([(W - 280, 52), (W - 10, 86)], fill=(59, 130, 246, 220))
draw.text((W - 270, 58), "ARRIVÉE TRIANGLES [AMONT]", fill=(255, 255, 255, 255), font=font_text)

draw.rectangle([(10, 52), (250, 86)], fill=(16, 185, 129, 220))
draw.text((20, 58), "SORTIE CROISSANTS [AVAL]", fill=(255, 255, 255, 255), font=font_text)

# Knobs definitions based on REAL DIRECTION (Right to Left):
knobs = [
    {
        "id": "A",
        "name": "POIGNÉE SUPÉRIEURE DROITE",
        "role": "ENTRÉE / AMORCE DU TRIANGLE",
        "sub": "Cible : 5,0 à 6,0 mm (1,5x pâte)",
        "desc": "Accrochage doux de la base sans écrasement",
        "badge_pos": (615, 230),
        "box_pos": (580, 96, 990, 196),
        "arrow_start": (615, 205),
        "arrow_end": (650, 196),
        "color": (59, 130, 246), # Blue (Infeed)
    },
    {
        "id": "B",
        "name": "POIGNÉE SUPÉRIEURE GAUCHE",
        "role": "SORTIE / DÉGAGEMENT DU ROULEAU",
        "sub": "Cible : 28 à 32 mm (diamètre rouleau)",
        "desc": "ATTENTION : Remonter la molette vers le haut\npour ne pas écraser le croissant fini !",
        "badge_pos": (430, 275),
        "box_pos": (20, 110, 440, 225),
        "arrow_start": (430, 250),
        "arrow_end": (350, 225),
        "color": (16, 185, 129), # Green (Outfeed)
    },
    {
        "id": "C",
        "name": "POIGNÉE INFÉRIEURE",
        "role": "GALBE, SERRAGE & POSITION CLÉ (6h)",
        "sub": "Cible : Position souple (gauche de coulisse)",
        "desc": "Roulage aéré (3-4 spires lâches) + pointe calée\nrigoureusement plaquée sous le pâton à 6h",
        "badge_pos": (450, 560),
        "box_pos": (20, 480, 430, 595),
        "arrow_start": (440, 540),
        "arrow_end": (350, 490),
        "color": (239, 68, 68), # Red (Curling pressure & Key)
    }
]

for k in knobs:
    bx1, by1, bx2, by2 = k["box_pos"]
    r, g, b = k["color"]
    # Draw card box
    draw.rectangle([(bx1, by1), (bx2, by2)], fill=(15, 23, 42, 240), outline=(r, g, b, 255), width=2)
    # Badge inside box
    draw.rectangle([(bx1+8, by1+8), (bx1+32, by1+32)], fill=(r, g, b, 255))
    draw.text((bx1+13, by1+10), k["id"], fill=(255, 255, 255, 255), font=font_badge)
    # Title
    draw.text((bx1+40, by1+10), k["name"], fill=(255, 255, 255, 255), font=font_text)
    draw.text((bx1+12, by1+34), k["role"], fill=(r, g, b, 255), font=font_text)
    draw.text((bx1+12, by1+56), k["sub"], fill=(245, 158, 11, 255), font=font_text)
    draw.text((bx1+12, by1+76), k["desc"], fill=(203, 213, 225, 255), font=font_sub)

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
print("Real direction guide generated successfully:", out_path)
