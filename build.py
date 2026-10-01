#!/usr/bin/env python3
"""Génère index.html, merci.html, robots.txt et sitemap.xml de la LP KB Toiture (nettoyage de toiture).
Usage : python3 build.py   — modifier la config ci-dessous, relancer, pousser."""
import json, datetime, html

# ---------- Config ----------
GTM_ID   = ""                                            # ex. "GTM-XXXXXXX" ; vide = snippet absent
SITE_URL = "https://cleanibat.github.io/kb-toiture-lp/"  # domaine final à mettre ici (canonical, sitemap)
ROBOTS   = "noindex, follow"                             # LP Ads qui doublonne kbtoiture.fr
BRAND    = "KB Toiture"
TEL_INT  = "+33665425003"
TEL_FR   = "06 65 42 50 03"
EMAIL    = "kbtoiture2@gmail.com"
ADDRESS  = ("39 bis chemin du Clos Lapierre", "52100", "Saint-Dizier")
MAIN_SITE = "https://kbtoiture.fr/"
LP_NAME  = "LP Nettoyage de toiture"

TITLE = "Nettoyage et démoussage de toiture à Saint-Dizier | KB Toiture"
DESC  = ("Démoussage, nettoyage basse pression et traitement hydrofuge de votre toiture à Saint-Dizier "
         "et alentours (52, 51, 55). Devis gratuit, réponse sous 48 h.")

REASSURANCE = [
    ("Devis gratuit", "écrit et détaillé, sans engagement"),
    ("Réponse sous 48 h", "après réception de votre demande"),
    ("Nettoyage basse pression", "adapté à la tuile comme à l'ardoise"),
    ("Abords protégés", "chantier nettoyé en fin d'intervention"),
]

NEEDS = ["Démoussage / nettoyage de toiture", "Traitement hydrofuge incolore", "Traitement hydrofuge coloré",
         "Nettoyage des gouttières", "Nettoyage + hydrofuge", "Autre demande"]

SIGNS = [
    ("Mousses et lichens", "Ils retiennent l'eau à la surface des tuiles et s'installent dans les recouvrements."),
    ("Tuiles devenues poreuses", "Une tuile gorgée d'eau résiste moins bien au gel et laisse plus facilement passer l'humidité."),
    ("Gouttières encombrées", "Les débris de mousse finissent dans les gouttières et les descentes, qui débordent lors des fortes pluies."),
    ("Toiture ternie", "Traces noires, tuiles blanchies ou verdies : la couverture a perdu sa teinte d'origine."),
]

SERVICES = [
    ("Le plus demandé", "Démoussage et nettoyage basse pression",
     "Nous retirons à la main les amas de mousse, puis nous nettoyons la couverture avec une pression adaptée au support, tuile ou ardoise.",
     ["Traitement anti-mousse, algicide et fongicide", "Rinçage de haut en bas", "Pression réglée selon l'état des tuiles"]),
    ("Protection", "Traitement hydrofuge incolore",
     "Appliqué sur toiture propre et sèche, il pénètre dans les pores du matériau. L'eau perle et s'écoule au lieu d'être absorbée, la toiture continue de respirer.",
     ["Aspect de la toiture inchangé", "Effet perlant", "Limite la reprise des mousses"]),
    ("Toiture ternie", "Traitement hydrofuge coloré",
     "Pour des tuiles ternes ou blanchies mais encore saines : l'hydrofuge coloré redonne une teinte uniforme à la toiture tout en la protégeant de l'humidité.",
     ["Teinte choisie avec vous", "Même protection que l'incolore", "Une alternative à la réfection quand les tuiles sont saines"]),
    ("Inclus dans l'intervention", "Nettoyage des gouttières",
     "Un nettoyage de toiture comprend l'évacuation des eaux pluviales : nous vidons gouttières et chéneaux et nous contrôlons les descentes.",
     ["Vidage des gouttières et chéneaux", "Contrôle des soudures", "Vérification des descentes d'eau"]),
]

STEPS = [
    ("Diagnostic et préparation", "Nous examinons l'état des tuiles et le type de végétation présente. Les abords de la maison, les façades et les plantations sont protégés avant de commencer."),
    ("Nettoyage et traitement", "Retrait des mousses, application du produit anti-mousse avec son temps de pose, puis rinçage à basse ou moyenne pression, de haut en bas."),
    ("Application de l'hydrofuge", "Sur support sec, nous pulvérisons l'hydrofuge incolore ou coloré en passes croisées, jusqu'à saturation du matériau."),
    ("Contrôle et remise en état", "Nous vérifions l'effet perlant, nous contrôlons les gouttières et nous nettoyons le chantier avant de partir."),
]

GALLERY = [
    ("toiture-nettoyee.jpg", 680, 510, "Toiture en tuiles après nettoyage et traitement hydrofuge", "Nettoyage et traitement", "Démoussage et protection hydrofuge"),
    ("pose-tuiles.jpg", 1400, 1050, "Couvreurs de KB Toiture posant des tuiles neuves autour d'une fenêtre de toit", "Couverture", "Notre métier d'origine : couvreur zingueur"),
    ("fenetre-de-toit.jpg", 800, 966, "Fenêtre de toit neuve posée sur une toiture en tuiles anciennes", "Fenêtre de toit", "Remplacement et raccords d'étanchéité"),
]

ZONES = [
    ("Grand Saint-Dizier", ["Saint-Dizier (52100)", "Bettancourt-la-Ferrée", "Chancenay", "Valcourt", "Moëslains", "Eurville-Bienville"]),
    ("Lac du Der et sud", ["Éclaron-Braucourt-Sainte-Livière", "Wassy", "Montier-en-Der", "Sommevoire", "Joinville"]),
    ("Meuse et Marne", ["Ancerville (55170)", "Bar-le-Duc", "Ligny-en-Barrois", "Vitry-le-François (51300)", "Sermaize-les-Bains", "Thiéblemont-Farémont"]),
]

FAQ = [
    ("Quelle est la meilleure période pour nettoyer une toiture ?",
     "Le nettoyage se fait en toute saison. Nous fixons la date d'intervention en fonction de la météo, l'hydrofuge s'appliquant sur un support sec."),
    ("Combien coûte un nettoyage de toiture ?",
     "Le prix dépend de la surface, de la pente, de l'accès, de l'état des tuiles et du traitement choisi (démoussage seul, hydrofuge incolore ou coloré). Nous vous remettons un devis gratuit, écrit et détaillé, après avoir vu la toiture ou vos photos."),
    ("Le nettoyage risque-t-il d'abîmer mes tuiles ?",
     "Nous travaillons à basse ou moyenne pression, réglée selon le support, après avoir retiré les mousses à la main. Si des tuiles sont cassées ou trop fragiles, nous vous le signalons avant d'intervenir : nous sommes couvreurs et pouvons les remplacer."),
    ("Hydrofuge incolore ou coloré : lequel choisir ?",
     "L'incolore protège sans modifier l'aspect de la toiture. Le coloré convient aux tuiles ternies ou blanchies que vous souhaitez raviver. Nous vous conseillons au cas par cas lors du diagnostic."),
    ("Faut-il une autorisation de la mairie ?",
     "Un nettoyage ou un hydrofuge incolore ne modifient pas l'aspect de la maison et ne demandent pas de démarche. Si l'hydrofuge coloré change la teinte de la toiture, une déclaration préalable en mairie peut être nécessaire : renseignez-vous auprès de votre commune, surtout en secteur protégé."),
    ("Que deviennent les mousses et les déchets ?",
     "Les mousses retirées sont ramassées, les gouttières sont vidées et les abords sont nettoyés en fin de chantier."),
    ("Intervenez-vous pour les entreprises et les collectivités ?",
     "Oui. Nous intervenons pour les particuliers comme pour les professionnels, syndics et collectivités de Haute-Marne et des communes voisines de la Marne et de la Meuse."),
]

# ---------- Gabarits ----------
e = html.escape
ICON_PHONE = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
ICON_CHECK = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" d="M5 12.5l4.5 4.5L19 7.5"/></svg>'

def gtm_head():
    if not GTM_ID: return "<!-- GTM : renseigner GTM_ID dans build.py -->"
    return ("<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});"
            "var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;"
            "j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})"
            f"(window,document,'script','dataLayer','{GTM_ID}');</script>")

def gtm_body():
    if not GTM_ID: return ""
    return (f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" '
            'style="display:none;visibility:hidden"></iframe></noscript>')

def head(title, desc, path, robots, extra=""):
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{gtm_head()}
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{SITE_URL}{path}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE_URL}img/pose-tuiles.jpg">
<meta property="og:url" content="{SITE_URL}{path}">
<meta name="theme-color" content="#0B1E36">
<link rel="icon" type="image/png" href="img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
{extra}
</head>
<body>
{gtm_body()}"""

def header():
    return f"""<header class="top">
  <div class="wrap top-in">
    <a class="brand" href="index.html" aria-label="{BRAND}"><img src="img/logo.png" width="92" height="50" alt="Logo {BRAND}"><span>KB <b>Toiture</b></span></a>
    <nav class="top-nav" aria-label="Sections"><a href="#prestations">Prestations</a><a href="#methode">Méthode</a><a href="#zone">Zone</a><a href="#faq">Questions</a></nav>
    <a class="btn btn-call" href="tel:{TEL_INT}">{ICON_PHONE}<span>{TEL_FR}</span></a>
  </div>
</header>"""

def footer():
    return f"""<footer class="foot">
  <div class="wrap foot-in">
    <div><a class="brand brand-light" href="index.html"><img src="img/logo.png" width="92" height="50" alt="" loading="lazy"><span>KB <b>Toiture</b></span></a>
      <p>Artisan couvreur zingueur à Saint-Dizier. Nettoyage, démoussage et traitement hydrofuge de toiture en Haute-Marne, Marne et Meuse.</p></div>
    <div><h3>Contact</h3><p><a href="tel:{TEL_INT}">{TEL_FR}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>{ADDRESS[0]}<br>{ADDRESS[1]} {ADDRESS[2]}</p></div>
    <div><h3>KB Toiture</h3><p><a href="{MAIN_SITE}">Site principal : kbtoiture.fr</a><br><a href="{MAIN_SITE}couverture">Couverture</a><br><a href="{MAIN_SITE}zinguerie">Zinguerie</a></p></div>
  </div>
  <div class="wrap foot-legal">© <span id="year">2026</span> {BRAND} · Les informations envoyées par le formulaire servent uniquement à répondre à votre demande.</div>
</footer>
<div class="mbar"><a href="tel:{TEL_INT}" class="mbar-call">{ICON_PHONE} Appeler</a><a href="#devis" class="mbar-form">Devis gratuit</a></div>
<script src="main.js" defer></script>
</body>
</html>"""

def form():
    opts = "".join(f"<option>{e(n)}</option>" for n in NEEDS)
    return f"""<form id="devisForm" class="form" method="POST" action="contact.php">
  <h2>Demandez votre devis gratuit</h2>
  <p class="form-sub">Nous vous recontactons sous 48 h.</p>
  <input type="hidden" name="Source" value="{LP_NAME}">
  <input type="text" name="_honey" tabindex="-1" autocomplete="off" class="hp" aria-hidden="true">
  <div class="row"><label>Nom et prénom<input type="text" name="Nom" required autocomplete="name"></label>
  <label>Téléphone<input type="tel" name="Téléphone" required autocomplete="tel" inputmode="tel"></label></div>
  <div class="row"><label>E-mail<input type="email" name="Email" required autocomplete="email"></label>
  <label>Commune<input type="text" name="Localité" required autocomplete="address-level2" placeholder="Saint-Dizier, Wassy…"></label></div>
  <label>Votre besoin<select name="Besoin" required><option value="" disabled selected>Choisir…</option>{opts}</select></label>
  <label>Message <span class="opt">(facultatif)</span><textarea name="Message" rows="3" placeholder="Type de couverture (tuile, ardoise), surface approximative, présence de mousse, accès…"></textarea></label>
  <button type="submit" class="btn btn-main" data-sending="Envoi…">Recevoir mon devis gratuit</button>
  <p class="form-note">Vos coordonnées servent uniquement à répondre à votre demande.</p>
</form>"""

def index():
    ld_business = {"@context": "https://schema.org", "@type": "RoofingContractor", "name": BRAND, "url": MAIN_SITE,
        "telephone": TEL_INT, "email": EMAIL, "image": SITE_URL + "img/pose-tuiles.jpg",
        "address": {"@type": "PostalAddress", "streetAddress": ADDRESS[0], "postalCode": ADDRESS[1], "addressLocality": ADDRESS[2], "addressCountry": "FR"},
        "areaServed": [c for _, cs in ZONES for c in cs]}
    ld_faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    extra = (f'<script type="application/ld+json">{json.dumps(ld_business, ensure_ascii=False)}</script>\n'
             f'<script type="application/ld+json">{json.dumps(ld_faq, ensure_ascii=False)}</script>')
    reas = "".join(f"<li>{ICON_CHECK}<span><b>{e(t)}</b> {e(d)}</span></li>" for t, d in REASSURANCE)
    signs = "".join(f"<li><h3>{e(t)}</h3><p>{e(d)}</p></li>" for t, d in SIGNS)
    services = "".join(
        f'<article class="card"><span class="tag">{e(tag)}</span><h3>{e(t)}</h3><p>{e(d)}</p><ul>'
        + "".join(f"<li>{ICON_CHECK}{e(x)}</li>" for x in pts) + "</ul></article>" for tag, t, d, pts in SERVICES)
    steps = "".join(f'<li><span class="num">{i:02d}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (t, d) in enumerate(STEPS, 1))
    gallery = "".join(
        f'<figure><img src="img/{f}" width="{w}" height="{h}" alt="{e(alt)}" loading="lazy"><figcaption><b>{e(t)}</b>{e(c)}</figcaption></figure>'
        for f, w, h, alt, t, c in GALLERY)
    zones = "".join(f"<div><h3>{e(t)}</h3><ul>" + "".join(f"<li>{e(c)}</li>" for c in cs) + "</ul></div>" for t, cs in ZONES)
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in FAQ)
    return head(TITLE, DESC, "", ROBOTS, extra) + header() + f"""
<main>
<section class="hero">
  <div class="wrap hero-in">
    <div class="hero-txt">
      <p class="eyebrow">Artisan couvreur zingueur · Saint-Dizier (52)</p>
      <h1>Nettoyage et démoussage de toiture <em>à Saint-Dizier et alentours</em></h1>
      <p class="lead">Karl Burel et son équipe de couvreurs retirent mousses et lichens, nettoient votre toiture à basse pression et la protègent avec un traitement hydrofuge incolore ou coloré. Devis gratuit.</p>
      <div class="cta"><a href="#devis" class="btn btn-main">Demander un devis gratuit</a><a href="tel:{TEL_INT}" class="btn btn-ghost">{ICON_PHONE}<span>{TEL_FR}</span></a></div>
      <ul class="reas">{reas}</ul>
    </div>
    <div class="hero-form" id="devis">{form()}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap two">
    <figure class="photo"><img src="img/toiture-mousse.jpg" width="800" height="966" alt="Toiture ancienne en tuiles avec mousses et lichens avant intervention" loading="lazy"><figcaption>Mousses et lichens sur une toiture ancienne</figcaption></figure>
    <div>
      <p class="eyebrow">Pourquoi nettoyer sa toiture</p>
      <h2>Mousses, lichens, tuiles poreuses : <em>les signes à surveiller</em></h2>
      <p class="intro">Avec l'humidité et le temps, la végétation s'installe sur la couverture. Elle retient l'eau, et une tuile qui reste humide supporte moins bien le gel.</p>
      <ul class="signs">{signs}</ul>
    </div>
  </div>
</section>

<section class="sec sec-alt" id="prestations">
  <div class="wrap">
    <p class="eyebrow">Nos prestations</p>
    <h2>Démoussage, nettoyage et <em>traitement hydrofuge</em></h2>
    <div class="cards">{services}</div>
  </div>
</section>

<section class="sec sec-dark" id="methode">
  <div class="wrap">
    <p class="eyebrow">Notre méthode</p>
    <h2>Une intervention en <em>4 étapes</em></h2>
    <ol class="steps">{steps}</ol>
    <div class="cta center"><a href="#devis" class="btn btn-main">Demander un devis gratuit</a></div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow">Sur nos chantiers</p>
    <h2>Des couvreurs <em>sur votre toit</em></h2>
    <p class="intro">Nous sommes couvreurs zingueurs : pendant le nettoyage, nous repérons une tuile cassée, un solin décollé ou une gouttière percée, et nous pouvons les réparer.</p>
    <div class="gallery">{gallery}</div>
  </div>
</section>

<section class="sec sec-alt" id="zone">
  <div class="wrap">
    <p class="eyebrow">Zone d'intervention</p>
    <h2>Nettoyage de toiture en <em>Haute-Marne, Marne et Meuse</em></h2>
    <p class="intro">Depuis Saint-Dizier, nous nous déplaçons dans les communes suivantes et leurs environs.</p>
    <div class="zones">{zones}</div>
  </div>
</section>

<section class="sec" id="faq">
  <div class="wrap narrow">
    <p class="eyebrow">Questions fréquentes</p>
    <h2>Avant de faire nettoyer <em>votre toiture</em></h2>
    <div class="faq">{faq}</div>
  </div>
</section>

<section class="final">
  <div class="wrap">
    <h2>Votre toiture a besoin d'un nettoyage ?</h2>
    <p>Décrivez-nous votre toiture : nous vous recontactons sous 48 h avec un devis gratuit.</p>
    <div class="cta center"><a href="#devis" class="btn btn-main">Demander un devis gratuit</a><a href="tel:{TEL_INT}" class="btn btn-ghost">{ICON_PHONE}<span>{TEL_FR}</span></a></div>
  </div>
</section>
</main>
""" + footer()

def merci():
    return head("Demande envoyée | " + BRAND, "Votre demande de devis a bien été envoyée à KB Toiture.", "merci.html", "noindex, nofollow") + header() + f"""
<main>
<section class="final thanks">
  <div class="wrap">
    <h1>Votre demande est bien envoyée</h1>
    <p>Merci. Nous vous recontactons sous 48 h pour préparer votre devis. Pour une demande urgente, appelez-nous directement.</p>
    <div class="cta center"><a href="tel:{TEL_INT}" class="btn btn-main">{ICON_PHONE}<span>{TEL_FR}</span></a><a href="index.html" class="btn btn-ghost">Retour à la page</a></div>
  </div>
</section>
</main>
""" + footer()

if __name__ == "__main__":
    open("index.html", "w", encoding="utf-8").write(index())
    open("merci.html", "w", encoding="utf-8").write(merci())
    open("robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n")
    today = datetime.date.today().isoformat()
    urls = f"<url><loc>{SITE_URL}</loc><lastmod>{today}</lastmod></url>" if ROBOTS.startswith("index") else ""
    open("sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    print("OK : index.html, merci.html, robots.txt, sitemap.xml")
