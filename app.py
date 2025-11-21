import streamlit as st
import os, json, random, io
from datetime import datetime
from openai import OpenAI
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image as PdfImage, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

# -----------------------------------------------------
# CONFIG GLOBAL
# -----------------------------------------------------

st.set_page_config(page_title="Jeu Divinatoire – V7", layout="wide")

IMAGE_PATH = "images"
DATA_PATH = "data/cards.json"

# Chargement des données
with open(DATA_PATH, "r", encoding="utf-8") as f:
    cards = json.load(f)

# Whisper API
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


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
        out += "- Une dynamique cyclique importante influence la situation.\n"
    if "action" in energies:
        out += "- Une action concrète ou décision est favorisée maintenant.\n"
    if "abondance" in energies:
        out += "- Une période d’expansion positive est présente.\n"
    if "intuition" in themes:
        out += "- L’intuition joue un rôle clé dans ce tirage.\n"
    if "origines" in themes:
        out += "- Un retour aux sources ou à vos fondations est indiqué.\n"
    if "renaissance" in themes:
        out += "- Une renaissance intérieure ou un nouveau départ est en cours.\n"
    if "protection" in themes:
        out += "- Une énergie protectrice enveloppe ce tirage.\n"

    if out.strip() == "### Interprétation générale":
        out += "Ce tirage semble neutre ou en transition."

    return out


def export_pdf_single_page(tirage):
    """Génération PDF en page unique style Tarot Illustré"""
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
# API INTERNE (A2)
# -----------------------------------------------------

def route(path):
    st.session_state["internal_api_route"] = path


def internal_api_handler():
    if "internal_api_route" not in st.session_state:
        return

    path = st.session_state["internal_api_route"]

    # Routing simple
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
# UI : TITRE
# -----------------------------------------------------

st.title("Jeu Divinatoire – Version 7 Complète")


# -----------------------------------------------------
# TIRAGE VOCAL (WHISPER)
# -----------------------------------------------------

st.header("Tirage vocal (Whisper)")

audio = st.file_uploader("Envoyez un fichier audio (wav, mp3, m4a)", type=["wav", "mp3", "m4a"])
if audio:
    st.write("Transcription en cours…")
    resp = client.audio.transcriptions.create(
        file=audio,
        model="whisper-1",
        language="fr"
    )
    st.success("Vous avez dit : " + resp.text)


# -----------------------------------------------------
# TIRAGE DU JOUR
# -----------------------------------------------------

st.header("Tirage du jour")

if "daily" not in st.session_state or st.session_state.get("daily_date") != str(datetime.now().date()):
    if st.button("Générer le tirage du jour"):
        st.session_state.daily = random.sample(range(1, 25), 1)
        st.session_state.daily_date = str(datetime.now().date())

if "daily" in st.session_state:
    afficher_carte(st.session_state.daily[0])
    st.caption(f"Tirage généré le {st.session_state.daily_date}")

# -----------------------------------------------------
# THEME MYSTIQUE AVANCÉ — ANIMATIONS + HALO
# -----------------------------------------------------

st.markdown("""
<style>

body {
    background: radial-gradient(circle at 50% 20%, #1d1a33, #0d0b16 70%);
    animation: bgfade 12s ease-in-out infinite alternate;
}

@keyframes bgfade {
  0% { background: radial-gradient(circle at 50% 20%, #1d1a33, #0d0b16 70%); }
  100% { background: radial-gradient(circle at 50% 20%, #221d44, #0b0810 70%); }
}

/* --- TITRE AVEC AURA --- */
h1, h2, h3 {
    text-shadow: 0 0 15px #8d5cf6, 0 0 30px #5f34c7;
}

h1 {
    animation: glowpulse 4s infinite ease-in-out;
}

@keyframes glowpulse {
  0% { text-shadow: 0px 0px 10px #a879ff; }
  50% { text-shadow: 0px 0px 25px #d3a3ff; }
  100% { text-shadow: 0px 0px 10px #a879ff; }
}


/* --- CARDS: halo & animations --- */
img {
    border-radius: 15px;
    box-shadow: 0 0 12px rgba(202, 151, 255, 0.4);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

img:hover {
    transform: scale(1.05);
    box-shadow: 0 0 30px rgba(225, 189, 255, 0.8);
}

/* --- MYSTIC PARTICLES --- */
.mystic-particles {
    position: fixed;
    pointer-events: none;
    top: 0; left: 0;
    width: 100%; height: 100%;
    overflow: hidden;
    z-index: 0;
}

.particle {
    position: absolute;
    width: 4px;
    height: 4px;
    background: radial-gradient(circle, #d9b8ff 0%, #8d5cf6 70%);
    border-radius: 50%;
    animation: floatUp 10s linear infinite;
    opacity: 0.7;
}

@keyframes floatUp {
    0% { transform: translateY(100vh) scale(0.3); opacity:0; }
    20% { opacity:0.8; }
    100% { transform: translateY(-10vh) scale(1); opacity:0; }
}

/* --- MODAL POPUP --- */
[data-baseweb="modal"] {
    background: rgba(10, 10, 20, 0.85) !important;
    backdrop-filter: blur(10px);
    border: 1px solid #8d5cf6 !important;
    box-shadow: 0px 0px 20px #8d5cf6;
}

</style>

<div class="mystic-particles">
    """ + 
    "\n".join([
        f'<div class="particle" style="left:{i*4}%; animation-delay:{i*0.5}s;"></div>'
        for i in range(1, 25)
    ])
+ """
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# GALLERIE + POPUP
# -----------------------------------------------------

st.header("Galerie (cliquer pour plus de détails)")

cols = st.columns(3)
for i in range(1, 25):
    with cols[(i - 1) % 3]:
        if st.button(cards[str(i)]["nom"], key=f"btn{i}"):
            st.session_state.modal = i
        st.image(os.path.join(IMAGE_PATH, cards[str(i)]["image"]), width=180)

if "modal" in st.session_state:
    with st.modal(cards[str(st.session_state.modal)]["nom"]):
        afficher_carte(st.session_state.modal, width=300)
        if st.button("Fermer"):
            del st.session_state.modal


# -----------------------------------------------------
# TIRAGES COMPLETS
# -----------------------------------------------------

st.header("Tirages")

# Tirage simple
if st.button("Tirage simple"):
    t = random.sample(range(1, 25), 1)
    afficher_carte(t[0])
    st.markdown(interpretation_generale(t))


# Tirage 3 cartes
if st.button("Tirage 3 cartes"):
    t = random.sample(range(1, 25), 3)
    cols3 = st.columns(3)
    for idx, num in enumerate(t):
        afficher_carte(num, cols3[idx])
    st.markdown(interpretation_generale(t))


# Tirage saisons
if st.button("Tirage des saisons"):
    saisons = ["Printemps", "Été", "Automne", "Hiver"]
    t = random.sample(range(1, 25), 4)
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
    st.download_button("Exporter en PDF Tarot Illustré", data=pdf, file_name="tirage.pdf")
