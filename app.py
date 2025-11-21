import streamlit as st
import os, json, random, io
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image as PdfImage, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

# -----------------------------------------------------
# CONFIG GLOBAL
# -----------------------------------------------------

st.set_page_config(page_title="Jeu Divinatoire – V7 (sans Whisper)", layout="wide")

IMAGE_PATH = "images"
DATA_PATH = "data/cards.json"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    cards = json.load(f)


# -----------------------------------------------------
# FONCTIONS
# -----------------------------------------------------

def afficher_carte(num, container=None, width=240):
    c = cards[str(num)]
    cont = container if container else st

    cont.image(os.path.join(IMAGE_PATH, c["image"]), width=width)
    cont.markdown(f"### {c['nom']}")
    cont.markdown(f"**Symboles :** {c['symboles']}")
    cont.markdown("**Texte inscrit :**")
    for t in c["texte"]:
        cont.markdown(f"- {t}")
    cont.markdown(f"**Interprétation :** {c['interpretation']}")


def interpretation_generale(tirage):
    themes = []
    energies = []
    cycles = 0

    for num in tirage:
        txt = cards[str(num)]["interpretation"].lower()

        if "cycle" in txt:
            cycles += 1
        if "action" in txt:
            energies.append("action")
        if "abondance" in txt:
            energies.append("abondance")
        if "intuition" in txt:
            themes.append("intuition")
        if "racine" in txt or "origine" in txt:
            themes.append("origines")
        if "renaissance" in txt:
            themes.append("renaissance")
        if "protection" in txt:
            themes.append("protection")

    out = "### Interprétation générale\n"

    if cycles > 1:
        out += "- Une dynamique cyclique influence fortement la situation.\n"
    if "action" in energies:
        out += "- Une action ou décision immédiate est favorisée.\n"
    if "abondance" in energies:
        out += "- Une période d’expansion et d’opportunités est signalée.\n"
    if "intuition" in themes:
        out += "- L’intuition joue un rôle important.\n"
    if "origines" in themes:
        out += "- Un retour aux fondements personnels apparaît.\n"
    if "renaissance" in themes:
        out += "- Une renaissance ou un nouveau départ est en cours.\n"
    if "protection" in themes:
        out += "- Une énergie protectrice entoure ce tirage.\n"

    if out.strip() == "### Interprétation générale":
        out += "Le tirage est neutre ou en transition."

    return out


def export_pdf_single_page(tirage):
    buffer = io.BytesIO()
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Tirage – Tarot Illustré", styles["Title"]))
    story.append(Spacer(1, 0.3 * inch))

    for num in tirage:
        c = cards[str(num)]
        story.append(Paragraph(f"<b>{c['nom']}</b>", styles["Heading2"]))
        story.append(PdfImage(os.path.join(IMAGE_PATH, c["image"]), width=2.2 * inch, height=3.2 * inch))
        story.append(Paragraph("<br/>".join(c["texte"]), styles["BodyText"]))
        story.append(Paragraph(f"<i>{c['interpretation']}</i>", styles["Italic"]))
        story.append(Spacer(1, 0.4 * inch))

    story.append(Paragraph(interpretation_generale(tirage), styles["BodyText"]))

    doc = SimpleDocTemplate(buffer, pagesize=letter)
    doc.build(story)
    buffer.seek(0)
    return buffer


# -----------------------------------------------------
# API interne A2
# -----------------------------------------------------

def route(path):
    st.session_state["internal_api_route"] = path

def internal_api_handler():
    if "internal_api_route" not in st.session_state:
        return

    path = st.session_state["internal_api_route"]

    if path == "/internal_api/cards":
        return cards

    if path.startswith("/internal_api/card/"):
        num = path.split("/")[-1]
        return cards.get(num, {})

    if path == "/internal_api/tirage/simple":
        return random.sample(range(1, 25), 1)

    if path == "/internal_api/tirage/3":
        return random.sample(range(1, 25), 3)

    if path == "/internal_api/tirage/7":
        return random.sample(range(1, 25), 7)

    if path == "/internal_api/tirage/saisons":
        return random.sample(range(1, 25), 4)

    if path == "/internal_api/tirage/quotidien":
        return random.sample(range(1, 25), 1)


# -----------------------------------------------------
# UI
# -----------------------------------------------------

st.title("Jeu Divinatoire – Version 7 (sans Whisper)")


# Tirage quotidien
st.header("Tirage du jour")
if "daily" not in st.session_state or st.session_state.get("daily_date") != str(datetime.now().date()):
    if st.button("Générer le tirage du jour"):
        st.session_state.daily = random.sample(range(1, 25), 1)
        st.session_state.daily_date = str(datetime.now().date())

if "daily" in st.session_state:
    afficher_carte(st.session_state.daily[0])
    st.caption(f"Tirage généré le {st.session_state.daily_date}")


# -----------------------------------------------------
# Galerie + Popups
# -----------------------------------------------------

st.header("Galerie (cliquer pour détails)")

cols = st.columns(3)
for i in range(1, 25):
    with cols[(i - 1) % 3]:
        if st.button(cards[str(i)]["nom"], key=f"btn{i}"):
            st.session_state.modal = i
        st.image(os.path.join(IMAGE_PATH, cards[str(i)]["image"]), width=180)

if "modal" in st.session_state:
    with st.modal(cards[str(st.session_state.modal)]["nom"]):
        afficher_carte(st.session_state.modal, width=280)
        if st.button("Fermer"):
            del st.session_state.modal


# -----------------------------------------------------
# Tirages complets
# -----------------------------------------------------

st.header("Tirages")

# Simple
if st.button("Tirage simple"):
    t = random.sample(range(1, 25), 1)
    afficher_carte(t[0])
    st.markdown(interpretation_generale(t))

# 3 cartes
if st.button("Tirage 3 cartes"):
    t = random.sample(range(1, 25), 3)
    cols3 = st.columns(3)
    for idx, num in enumerate(t):
        afficher_carte(num, cols3[idx])
    st.markdown(interpretation_generale(t))

# Saisons
if st.button("Tirage des saisons"):
    t = random.sample(range(1, 25), 4)
    saisons = ["Printemps", "Été", "Automne", "Hiver"]
    cols4 = st.columns(4)
    for idx, num in enumerate(t):
        cols4[idx].markdown(f"### {saisons[idx]}")
        afficher_carte(num, cols4[idx])
    st.markdown(interpretation_generale(t))

# Grand tirage 7 cartes
if st.button("Grand tirage 7 cartes"):
    t = random.sample(range(1, 25), 7)
    cols7 = st.columns(3)
    for idx, num in enumerate(t):
        afficher_carte(num, cols7[idx % 3])

    st.markdown(interpretation_generale(t))

    pdf = export_pdf_single_page(t)
    st.download_button("Télécharger PDF Tarot Illustré", data=pdf, file_name="tirage.pdf")
