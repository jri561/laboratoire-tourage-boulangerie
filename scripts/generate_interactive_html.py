import base64
import json
from PIL import Image

# 1. Prepare base64 crop of the panel image
orig_path = '/home/toto/.gemini/antigravity/brain/bc31aa75-d0a6-4b32-9375-bab1b5922ed5/.user_uploaded/media_1794213420765_3a2fa12e.jpg'
orig = Image.open(orig_path)
crop_box = (120, 160, 760, 860)
panel_crop = orig.crop(crop_box)
panel_crop.save('/tmp/panel_crop.jpg', 'JPEG', quality=90)

with open('/tmp/panel_crop.jpg', 'rb') as f:
    b64_img = base64.b64encode(f.read()).decode('utf-8')

# Hotspots coordinates in percentage of panel_crop (width=640, height=700)
cw, ch = crop_box[2] - crop_box[0], crop_box[3] - crop_box[1]

# List of hotspots with detailed metadata
hotspots = [
    {
        "id": 1,
        "name": "Arrêt d'Urgence",
        "category": "securite",
        "catName": "Sécurité",
        "x": round((388 - crop_box[0]) / cw * 100, 2),
        "y": round((388 - crop_box[1]) / ch * 100, 2),
        "icon": "🔴",
        "role": "Coup de poing de sécurité absolue.",
        "action": "Coupe instantanément les moteurs du tapis et l'alimentation des 4 prises d'accessoires. Ne pas utiliser pour un arrêt standard.",
        "rearm": "Tourner d'un quart de tour vers la droite pour le déverrouiller, puis appuyer sur [R] pour réinitialiser la machine.",
        "suisse": "Normalement armé (position haute).",
        "raisin": "Normalement armé.",
        "oranais": "Normalement armé."
    },
    {
        "id": 2,
        "name": "Afficheur Paramètre (LED Rouge)",
        "category": "affichage",
        "catName": "Affichage",
        "x": round((350 - crop_box[0]) / cw * 100, 2),
        "y": round((508 - crop_box[1]) / ch * 100, 2),
        "icon": "📟",
        "role": "Affiche la valeur courante de la fonction sélectionnée.",
        "action": "Affiche soit la vitesse du tapis (%), la longueur de coupe guillotine (mm), ou le débit de l'accessoire sélectionné.",
        "rearm": "Réglable en direct via les touches [-] et [+].",
        "suisse": "Affiche 48 (mm) pour la coupe ou 35 (%) pour la vitesse.",
        "raisin": "Affiche 18 (mm) pour la coupe d'escargot.",
        "oranais": "Affiche 120 (mm) pour les carrés de 12x12 cm."
    },
    {
        "id": 3,
        "name": "Touches de Saisie [-] / [+] / [↵]",
        "category": "saisie",
        "catName": "Saisie & Validation",
        "x": round((415 - crop_box[0]) / cw * 100, 2),
        "y": round((508 - crop_box[1]) / ch * 100, 2),
        "icon": "🎛️",
        "role": "Incrémentation, décrémentation et validation de consigne.",
        "action": "[-] diminue la valeur | [+] augmente la valeur | [↵ Entrée] valide et mémorise temporairement la consigne.",
        "rearm": "Appuyer sur Entrée après chaque modification pour prise en compte immédiate.",
        "suisse": "Utilisé pour caler la coupe à 48 mm.",
        "raisin": "Utilisé pour caler la coupe à 18 mm.",
        "oranais": "Utilisé pour caler la coupe à 120 mm."
    },
    {
        "id": 4,
        "name": "Afficheur N° Programme (. 1 .)",
        "category": "recettes",
        "catName": "Programmes",
        "x": round((500 - crop_box[0]) / cw * 100, 2),
        "y": round((508 - crop_box[1]) / ch * 100, 2),
        "icon": "📂",
        "role": "Indique le numéro de la recette active (de 1 à 99).",
        "action": "Permet d'identifier instantanément quelle viennoiserie est programmée dans la mémoire de l'automate.",
        "rearm": "Changement de recette via la touche Répertoire.",
        "suisse": "Affecter par exemple au Programme 04.",
        "raisin": "Affecter par exemple au Programme 03.",
        "oranais": "Affecter par exemple au Programme 05."
    },
    {
        "id": 5,
        "name": "Liste & Sauvegarde (Disquette)",
        "category": "recettes",
        "catName": "Mémoire",
        "x": round((550 - crop_box[0]) / cw * 100, 2),
        "y": round((508 - crop_box[1]) / ch * 100, 2),
        "icon": "💾",
        "role": "Rappel de programme (Haut) et Enregistrement (Bas).",
        "action": "Touche Disquette : maintenir appuyé 2 secondes pour graver définitivement tous les réglages actuels dans le numéro de recette actif.",
        "rearm": "Bip sonore ou clignotement confirmant l'enregistrement.",
        "suisse": "Sauvegarder une fois les 120 g brut validés à la pesée.",
        "raisin": "Sauvegarder une fois les 90 g brut validés.",
        "oranais": "Sauvegarder une fois les carrés de 60 g validés."
    },
    {
        "id": 6,
        "name": "Vitesse Générale Tapis (1...100%)",
        "category": "ligne",
        "catName": "Vitesse Ligne",
        "x": round((228 - crop_box[0]) / cw * 100, 2),
        "y": round((575 - crop_box[1]) / ch * 100, 2),
        "icon": "⚡",
        "role": "Vitesse d'avancement du tapis convoyeur principal.",
        "action": "Plage de réglage de 0,5 à 8 m/min. Règle la cadence globale de travail de l'atelier.",
        "rearm": "Recommandation : 35 % à 40 % pour un confort optimal de façonnage manuel.",
        "suisse": "Régler à 35 % (~3,5 m/min).",
        "raisin": "Régler à 30 % (permet un enroulement régulier du boudin).",
        "oranais": "Régler à 35 %."
    },
    {
        "id": 7,
        "name": "Longueur de Coupe Guillotine (mm)",
        "category": "ligne",
        "catName": "Coupe Guillotine",
        "x": round((228 - crop_box[0]) / cw * 100, 2),
        "y": round((630 - crop_box[1]) / ch * 100, 2),
        "icon": "📐",
        "role": "Distance d'avancement du tapis entre deux coupes.",
        "action": "Paramètre N°1 du grammage des pièces ! Chaque millimètre en plus ou en moins modifie le poids net du pâton.",
        "rearm": "Saisir au millimètre près avec [+] et [-].",
        "suisse": "48 mm pile (donne les 70 g de pâte à plat).",
        "raisin": "18 mm (donne les 55 g de pâte de l'escargot).",
        "oranais": "120 mm (donne le carré parfait de 12x12 cm = 60 g)."
    },
    {
        "id": 8,
        "name": "Vitesse / Débit Accessoires (1...100%)",
        "category": "ligne",
        "catName": "Débit Accessoires",
        "x": round((228 - crop_box[0]) / cw * 100, 2),
        "y": round((755 - crop_box[1]) / ch * 100, 2),
        "icon": "⚙️",
        "role": "Régime moteur de l'accessoire motorisé sélectionné.",
        "action": "Permet de moduler le débit de crème de la doseuse ou la vitesse de rotation du rouleau de pépites.",
        "rearm": "Sélectionner d'abord la prise (1, 2, 3 ou 4) puis ajuster.",
        "suisse": "Calibrer la doseuse (2) pour débiter 35 g de crème / 48 mm.",
        "raisin": "Calibrer la doseuse (2) à 20 g et l'épandeur (3) à 15 g.",
        "oranais": "Calibrer la doseuse (2) à 25 g / plot."
    },
    {
        "id": 9,
        "name": "Guillotine ON / OFF",
        "category": "outils",
        "catName": "Outils Ligne",
        "x": round((285 - crop_box[0]) / cw * 100, 2),
        "y": round((575 - crop_box[1]) / ch * 100, 2),
        "icon": "🔪",
        "role": "Enclenchement de la guillotine transversale.",
        "action": "La LED verte s'allume lorsque la guillotine est active. Si éteinte, la bande passe sous la lame sans être coupée.",
        "rearm": "Vérifier que le capot de sécurité est bien fermé.",
        "suisse": "ACTIF (LED allumée).",
        "raisin": "ACTIF (tranchage du boudin).",
        "oranais": "ACTIF (découpe des carrés)."
    },
    {
        "id": 10,
        "name": "Mode de Coupe (Stop-and-Go / Continu)",
        "category": "outils",
        "catName": "Outils Ligne",
        "x": round((348 - crop_box[0]) / cw * 100, 2),
        "y": round((575 - crop_box[1]) / ch * 100, 2),
        "icon": "⏸️",
        "role": "Sélection du mode d'avance pendant la coupe.",
        "action": "Mode Stop-and-Go : le tapis stoppe net pendant la descente/remontée de la lame. Évite l'arrachement ou le biseautage de la coupe.",
        "rearm": "Laisser TOUJOURS en mode Stop-and-Go pour la viennoiserie.",
        "suisse": "Stop-and-Go obligatoire.",
        "raisin": "Stop-and-Go obligatoire.",
        "oranais": "Stop-and-Go obligatoire."
    },
    {
        "id": 11,
        "name": "Doseuse Continue (Ruban)",
        "category": "depose",
        "catName": "Dépose Crème",
        "x": round((285 - crop_box[0]) / cw * 100, 2),
        "y": round((625 - crop_box[1]) / ch * 100, 2),
        "icon": "〰️",
        "role": "Dépose continue de crème sur la bande.",
        "action": "La pompe à crème tourne de façon ininterrompue, synchronisée avec l'avancement du tapis.",
        "rearm": "Les 4 buses déposent 4 cordons parallèles sur 14 cm.",
        "suisse": "ACTIF (Mode continu sur 14 cm de large).",
        "raisin": "ACTIF (Dépose sur demi-bande avant racleur).",
        "oranais": "INACTIF (utiliser le mode cadencé)."
    },
    {
        "id": 12,
        "name": "Doseuse Cadencée (Plots)",
        "category": "depose",
        "catName": "Dépose Crème",
        "x": round((348 - crop_box[0]) / cw * 100, 2),
        "y": round((625 - crop_box[1]) / ch * 100, 2),
        "icon": "🔲",
        "role": "Dépose intermittente par plots séparés.",
        "action": "La pompe à crème s'active pendant une durée précise pour déposer une noisette de crème au centre de chaque pièce.",
        "rearm": "Synchronisé avec le pas d'avance de la guillotine.",
        "suisse": "INACTIF.",
        "raisin": "INACTIF.",
        "oranais": "ACTIF (1 plot de 25 g au centre de chaque pas de 120 mm)."
    },
    {
        "id": 13,
        "name": "Épandeur d'Inclusions ON / OFF",
        "category": "depose",
        "catName": "Saupoudreur",
        "x": round((415 - crop_box[0]) / cw * 100, 2),
        "y": round((625 - crop_box[1]) / ch * 100, 2),
        "icon": "🍫",
        "role": "Distribution des pépites de chocolat ou des raisins secs.",
        "action": "Active le moteur du rouleau cannelé sous la trémie pour déverser une pluie régulière d'inclusions.",
        "rearm": "Canaliser avec les déflecteurs latéraux.",
        "suisse": "ACTIF (15 g de pépites 50 % sur les 14 cm de crème).",
        "raisin": "ACTIF (15 g de raisins secs sur la crème étalée).",
        "oranais": "INACTIF (pas d'inclusions)."
    },
    {
        "id": 14,
        "name": "Enrouleur de Boudin ON / OFF",
        "category": "faconnage",
        "catName": "Enrouleur",
        "x": round((415 - crop_box[0]) / cw * 100, 2),
        "y": round((575 - crop_box[1]) / ch * 100, 2),
        "icon": "🌀",
        "role": "Commande de l'enrouleur transversal de pâte.",
        "action": "Vient rouler la bande de pâte garnie pour former un boudin cylindrique régulier de Ø 48 mm.",
        "rearm": "Régler la hauteur du treillis métallique et des coulisses.",
        "suisse": "INACTIF (le pliage est 100% manuel à la sortie).",
        "raisin": "ACTIF (forme le boudin du pain aux raisins).",
        "oranais": "INACTIF."
    },
    {
        "id": 15,
        "name": "Touches Manuelles / Purge 🖐️",
        "category": "manuel",
        "catName": "Commandes Manuelles",
        "x": round((348 - crop_box[0]) / cw * 100, 2),
        "y": round((670 - crop_box[1]) / ch * 100, 2),
        "icon": "🖐️",
        "role": "Action manuelle instantanée (Jog / Test unitaire).",
        "action": "Permet de tester unitairement : coup de guillotine manuel, amorçage de la crème (purge des bulles d'air), test débit chocolat.",
        "rearm": "Fonctionne uniquement quand le tapis principal est à l'arrêt.",
        "suisse": "Purger la crème jusqu'à écoulement continu sans air.",
        "raisin": "Purger la crème.",
        "oranais": "Purger et vérifier le poids du plot test (25 g)."
    },
    {
        "id": 16,
        "name": "Bouton Bleu [ R ] (Reset / PMH)",
        "category": "commande",
        "catName": "Réarmement",
        "x": round((530 - crop_box[0]) / cw * 100, 2),
        "y": round((615 - crop_box[1]) / ch * 100, 2),
        "icon": "🔵",
        "role": "Reset défauts & Remontée Point Mort Haut guillotine.",
        "action": "Après un arrêt d'urgence ou une coupure, appuyer sur [R] pour réarmer la chaîne de sécurité et remonter la lame en position haute.",
        "rearm": "Indispensable avant tout redémarrage de la ligne.",
        "suisse": "Appui au démarrage après mise sous tension.",
        "raisin": "Appui au démarrage.",
        "oranais": "Appui au démarrage."
    },
    {
        "id": 17,
        "name": "Bouton Vert START [ I ]",
        "category": "commande",
        "catName": "Marche Ligne",
        "x": round((470 - crop_box[0]) / cw * 100, 2),
        "y": round((650 - crop_box[1]) / ch * 100, 2),
        "icon": "▶️",
        "role": "Mise en marche générale de la ligne Polyline.",
        "action": "Démarre le tapis principal et synchronise tous les accessoires dont la LED verte est allumée.",
        "rearm": "Vérifier que les opérateurs sont prêts en bout de ligne.",
        "suisse": "Lance la bande 28 cm, le crémage, chocolat et coupe.",
        "raisin": "Lance la production complète.",
        "oranais": "Lance la production complète."
    },
    {
        "id": 18,
        "name": "Bouton Rouge STOP [ 0 ]",
        "category": "commande",
        "catName": "Arrêt Standard",
        "x": round((530 - crop_box[0]) / cw * 100, 2),
        "y": round((705 - crop_box[1]) / ch * 100, 2),
        "icon": "⏹️",
        "role": "Arrêt normal et propre de la production.",
        "action": "Arrête le tapis et suspend immédiatement le dosage et la guillotine sans désarmer les sécurités.",
        "rearm": "Appuyer sur START [I] pour reprendre à tout moment.",
        "suisse": "Utilisé en fin de pâton ou changement de plaque.",
        "raisin": "Arrêt standard.",
        "oranais": "Arrêt standard."
    },
    {
        "id": 19,
        "name": "Prise Accessoire ( 1 ) : Guillotine",
        "category": "accessoires",
        "catName": "Canal 1",
        "x": round((290 - crop_box[0]) / cw * 100, 2),
        "y": round((755 - crop_box[1]) / ch * 100, 2),
        "icon": "1️⃣",
        "role": "Canal de commande de la guillotine transversale.",
        "action": "Appuyer sur (1) pour afficher et régler les paramètres avancés de la guillotine sur l'écran LED (temps d'arrêt stop-and-go).",
        "rearm": "La LED confirme la sélection du canal 1.",
        "suisse": "Assigné à la Guillotine transversale.",
        "raisin": "Assigné à la Guillotine transversale.",
        "oranais": "Assigné à la Guillotine transversale."
    },
    {
        "id": 20,
        "name": "Prise Accessoire ( 2 ) : Doseuse Crème",
        "category": "accessoires",
        "catName": "Canal 2",
        "x": round((355 - crop_box[0]) / cw * 100, 2),
        "y": round((755 - crop_box[1]) / ch * 100, 2),
        "icon": "2️⃣",
        "role": "Canal de commande de la doseuse de crème à 4 buses.",
        "action": "Appuyer sur (2) pour régler le débit de pompage sur l'écran LED gauche via [-] et [+].",
        "rearm": "Permet d'ajuster le grammage exact de crème en cours de route.",
        "suisse": "Régler pour débiter 35 g / 4,8 cm.",
        "raisin": "Régler pour débiter 20 g / 1,8 cm.",
        "oranais": "Régler pour débiter 25 g / plot."
    },
    {
        "id": 21,
        "name": "Prise Accessoire ( 3 ) : Épandeur Inclusions",
        "category": "accessoires",
        "catName": "Canal 3",
        "x": round((420 - crop_box[0]) / cw * 100, 2),
        "y": round((755 - crop_box[1]) / ch * 100, 2),
        "icon": "3️⃣",
        "role": "Canal de commande du déversoir de pépites / raisins.",
        "action": "Appuyer sur (3) pour afficher et régler la vitesse de rotation du rouleau distributeur.",
        "rearm": "Ajuster selon le calibre des grains.",
        "suisse": "Régler pour 15 g de pépites de chocolat.",
        "raisin": "Régler pour 15 g de raisins secs bruts.",
        "oranais": "Non utilisé (éteint)."
    },
    {
        "id": 22,
        "name": "Prise Accessoire ( 4 ) : Enrouleur de Boudin",
        "category": "accessoires",
        "catName": "Canal 4",
        "x": round((485 - crop_box[0]) / cw * 100, 2),
        "y": round((755 - crop_box[1]) / ch * 100, 2),
        "icon": "4️⃣",
        "role": "Canal de commande de l'enrouleur transversal motorisé.",
        "action": "Appuyer sur (4) pour régler la vitesse relative d'enroulement par rapport au tapis.",
        "rearm": "Évite le serrage excessif ou le boudin trop lâche.",
        "suisse": "Non utilisé.",
        "raisin": "Synchronisé pour rouler le boudin Ø 48 mm.",
        "oranais": "Non utilisé."
    }
]

# Generate HTML
html_content = f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guide Interactif • Console Rondo Polyline</title>
    <style>
        :root {{
            --bg: #0f172a;
            --panel-bg: #1e293b;
            --card-bg: #1e293b;
            --border: #334155;
            --text: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #38bdf8;
            --accent-glow: rgba(56, 189, 248, 0.4);
            --danger: #ef4444;
            --warning: #f59e0b;
            --success: #10b981;
            --purple: #a855f7;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.5;
            padding: 24px;
        }}
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border);
            padding-bottom: 16px;
            margin-bottom: 24px;
        }}
        .header h1 {{
            font-size: 1.5rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .header .badge {{
            background: #0284c7;
            color: white;
            font-size: 0.75rem;
            padding: 4px 10px;
            border-radius: 9999px;
            font-weight: 600;
        }}
        .filters {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 20px;
        }}
        .filter-btn {{
            background: var(--panel-bg);
            color: var(--text);
            border: 1px solid var(--border);
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 0.875rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .filter-btn:hover {{
            background: #334155;
            border-color: var(--accent);
        }}
        .filter-btn.active {{
            background: #0284c7;
            border-color: var(--accent);
            color: white;
            box-shadow: 0 0 12px var(--accent-glow);
        }}
        .main-container {{
            display: grid;
            grid-template-columns: 1fr 420px;
            gap: 24px;
            align-items: start;
        }}
        @media (max-width: 1024px) {{
            .main-container {{ grid-template-columns: 1fr; }}
        }}
        .interactive-screen {{
            background: #0b1120;
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 16px;
            position: relative;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .image-wrapper {{
            position: relative;
            display: inline-block;
            max-width: 100%;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        }}
        .panel-img {{
            display: block;
            max-width: 100%;
            height: auto;
            user-select: none;
        }}
        .pin {{
            position: absolute;
            transform: translate(-50%, -50%);
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: #0284c7;
            border: 2px solid white;
            color: white;
            font-weight: 700;
            font-size: 11px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 0 10px rgba(0,0,0,0.8), 0 0 6px var(--accent-glow);
            transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
            z-index: 10;
        }}
        .pin:hover, .pin.active {{
            transform: translate(-50%, -50%) scale(1.35);
            background: #f59e0b;
            border-color: #fff;
            box-shadow: 0 0 20px rgba(245, 158, 11, 0.9);
            z-index: 20;
        }}
        .pin.cat-securite {{ background: #ef4444; }}
        .pin.cat-affichage {{ background: #f59e0b; }}
        .pin.cat-saisie {{ background: #f59e0b; }}
        .pin.cat-recettes {{ background: #ea580c; }}
        .pin.cat-ligne {{ background: #10b981; }}
        .pin.cat-outils {{ background: #0ea5e9; }}
        .pin.cat-depose {{ background: #a855f7; }}
        .pin.cat-faconnage {{ background: #f97316; }}
        .pin.cat-manuel {{ background: #64748b; }}
        .pin.cat-commande {{ background: #10b981; }}
        .pin.cat-accessoires {{ background: #14b8a6; }}
        .pin.dimmed {{
            opacity: 0.15;
            transform: translate(-50%, -50%) scale(0.8);
            pointer-events: none;
        }}
        .details-card {{
            background: var(--panel-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.4);
            position: sticky;
            top: 24px;
        }}
        .details-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid var(--border);
        }}
        .details-badge {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #0284c7;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.25rem;
            font-weight: 700;
            color: white;
            box-shadow: 0 0 10px var(--accent-glow);
        }}
        .details-title h2 {{
            font-size: 1.2rem;
            font-weight: 700;
            color: white;
        }}
        .details-title span {{
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--accent);
            font-weight: 600;
        }}
        .detail-row {{
            margin-bottom: 14px;
        }}
        .detail-label {{
            font-size: 0.75rem;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 0.05em;
            color: var(--text-muted);
            margin-bottom: 4px;
        }}
        .detail-text {{
            font-size: 0.9rem;
            color: #e2e8f0;
        }}
        .recipe-box {{
            background: #0f172a;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 12px;
            margin-top: 16px;
        }}
        .recipe-box h3 {{
            font-size: 0.8rem;
            text-transform: uppercase;
            color: #f59e0b;
            font-weight: 700;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .recipe-item {{
            font-size: 0.85rem;
            margin-bottom: 6px;
            display: flex;
            justify-content: space-between;
        }}
        .recipe-item strong {{
            color: #93c5fd;
        }}
        .pulse {{
            animation: pulse-ring 2s infinite;
        }}
        @keyframes pulse-ring {{
            0% {{ box-shadow: 0 0 0 0 rgba(56, 189, 248, 0.7); }}
            70% {{ box-shadow: 0 0 0 12px rgba(56, 189, 248, 0); }}
            100% {{ box-shadow: 0 0 0 0 rgba(56, 189, 248, 0); }}
        }}
    </style>
</head>
<body>

    <div class="header">
        <div>
            <h1>RONDO POLYLINE • GUIDE INTERACTIF DE CONSOLE</h1>
            <p style="color:var(--text-muted); font-size:0.875rem;">Clique ou survole n'importe quelle touche pour afficher ses réglages et spécifications d'atelier.</p>
        </div>
        <div class="badge">Atelier Tourage & Viennoiserie</div>
    </div>

    <div class="filters">
        <button class="filter-btn active" onclick="filterRecipe('all')">👁️ Toutes les Touches (22)</button>
        <button class="filter-btn" onclick="filterRecipe('suisse')">🍫 Réglages PAIN SUISSE</button>
        <button class="filter-btn" onclick="filterRecipe('raisin')">🍇 Réglages PAIN AUX RAISINS</button>
        <button class="filter-btn" onclick="filterRecipe('oranais')">🍑 Réglages ORANAIS</button>
    </div>

    <div class="main-container">
        
        <!-- Interactive Panel Area -->
        <div class="interactive-screen">
            <div class="image-wrapper" id="imageWrapper">
                <img src="data:image/jpeg;base64,{b64_img}" alt="Tableau de commande Rondo Polyline" class="panel-img" id="panelImg">
                <!-- Pins injected here by JS -->
            </div>
        </div>

        <!-- Details Card -->
        <div class="details-card" id="detailsCard">
            <div class="details-header">
                <div class="details-badge" id="cardBadge">1</div>
                <div class="details-title">
                    <h2 id="cardTitle">Arrêt d'Urgence</h2>
                    <span id="cardCat">SÉCURITÉ</span>
                </div>
            </div>

            <div class="detail-row">
                <div class="detail-label">Rôle & Action Automate</div>
                <div class="detail-text" id="cardRole">Coup de poing de sécurité absolue. Coupe instantanément les moteurs du tapis et l'alimentation des 4 prises d'accessoires.</div>
            </div>

            <div class="detail-row">
                <div class="detail-label">Procédure Opérateur & Réarmement</div>
                <div class="detail-text" id="cardAction">Tourner d'un quart de tour vers la droite pour le déverrouiller, puis appuyer sur [R] pour réinitialiser la machine.</div>
            </div>

            <div class="recipe-box">
                <h3>⚙️ Réglages Recommandés en Production</h3>
                <div class="recipe-item"><span>🍫 Pain Suisse :</span> <strong id="cardSuisse">48 mm / 35 %</strong></div>
                <div class="recipe-item"><span>🍇 Pain aux Raisins :</span> <strong id="cardRaisin">18 mm / 30 %</strong></div>
                <div class="recipe-item"><span>🍑 Oranais Abricots :</span> <strong id="cardOranais">120 mm / 35 %</strong></div>
            </div>
        </div>

    </div>

    <script>
        const hotspots = {json.dumps(hotspots, indent=4)};

        const imageWrapper = document.getElementById('imageWrapper');
        const cardBadge = document.getElementById('cardBadge');
        const cardTitle = document.getElementById('cardTitle');
        const cardCat = document.getElementById('cardCat');
        const cardRole = document.getElementById('cardRole');
        const cardAction = document.getElementById('cardAction');
        const cardSuisse = document.getElementById('cardSuisse');
        const cardRaisin = document.getElementById('cardRaisin');
        const cardOranais = document.getElementById('cardOranais');

        // Create pins
        hotspots.forEach(h => {{
            const pin = document.createElement('div');
            pin.className = `pin cat-${{h.category}} pulse`;
            pin.style.left = `${{h.x}}%`;
            pin.style.top = `${{h.y}}%`;
            pin.innerText = h.id;
            pin.id = `pin-${{h.id}}`;

            pin.addEventListener('click', () => selectPin(h));
            pin.addEventListener('mouseenter', () => selectPin(h));

            imageWrapper.appendChild(pin);
        }});

        function selectPin(h) {{
            document.querySelectorAll('.pin').forEach(p => p.classList.remove('active'));
            const activePin = document.getElementById(`pin-${{h.id}}`);
            if (activePin) activePin.classList.add('active');

            cardBadge.innerText = h.id;
            cardBadge.className = `details-badge cat-${{h.category}}`;
            cardTitle.innerText = h.name;
            cardCat.innerText = h.catName.toUpperCase();
            cardRole.innerText = h.role;
            cardAction.innerText = h.action + " " + (h.rearm ? "(" + h.rearm + ")" : "");
            cardSuisse.innerText = h.suisse;
            cardRaisin.innerText = h.raisin;
            cardOranais.innerText = h.oranais;
        }}

        // Default select item 1
        selectPin(hotspots[0]);

        // Recipe filter logic
        const recipePresets = {{
            'all': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],
            'suisse': [1,2,3,4,5,6,7,9,10,11,13,15,16,17,18,19,20,21], // Coupe 48mm, Guillotine, Doseuse Continue, Épandeur choco
            'raisin': [1,2,3,4,5,6,7,9,10,11,13,14,15,16,17,18,19,20,21,22], // Coupe 18mm, Guillotine, Doseuse Continue, Épandeur, Enrouleur
            'oranais': [1,2,3,4,5,6,7,9,10,12,15,16,17,18,19,20] // Coupe 120mm, Guillotine, Doseuse Plots cadencés
        }};

        function filterRecipe(recipe) {{
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            event.target.classList.add('active');

            const allowed = recipePresets[recipe];
            hotspots.forEach(h => {{
                const el = document.getElementById(`pin-${{h.id}}`);
                if (allowed.includes(h.id)) {{
                    el.classList.remove('dimmed');
                }} else {{
                    el.classList.add('dimmed');
                }}
            }});

            // Select first visible
            const first = hotspots.find(h => allowed.includes(h.id));
            if (first) selectPin(first);
        }}
    </script>
</body>
</html>
'''

# Write to scratch and brain artifacts
out_path1 = '/home/toto/.gemini/antigravity/scratch/laboratoire-tourage-boulangerie/guide_interactif_panneau_polyline.html'
out_path2 = '/home/toto/.gemini/antigravity/brain/bc31aa75-d0a6-4b32-9375-bab1b5922ed5/guide_interactif_panneau_polyline.html'

with open(out_path1, 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(out_path2, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Interactive HTML guide generated successfully!')
