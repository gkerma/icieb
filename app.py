
import streamlit as st, random, os, json
from datetime import datetime

st.set_page_config(page_title="Jeu Divinatoire – V3", layout="wide")

IMAGE_PATH="images"

with open("data/cards.json","r",encoding="utf-8") as f:
    cards=json.load(f)

def afficher_carte(num, container=None, width=240):
    c=cards[str(num)]
    cont=container if container else st
    cont.markdown(f"### Carte {num} – {c['nom']}")
    img=os.path.join(IMAGE_PATH, c["image"])
    if os.path.exists(img):
        cont.image(img, width=width)
    cont.markdown(f"**Symboles :** {c['symboles']}")
    cont.markdown("**Texte inscrit :**")
    for t in c["texte"]:
        cont.markdown(f"- {t}")
    cont.markdown(f"**Interprétation :** {c['interpretation']}")

def interpretation_generale(tirage):
    themes=[]; energies=[]; cycles=0
    for num in tirage:
        it=cards[str(num)]["interpretation"].lower()
        if "cycle" in it: cycles+=1
        if "action" in it: energies.append("action")
        if "abondance" in it: energies.append("abondance")
        if "intuition" in it: themes.append("intuition")
        if "racine" in it or "origine" in it: themes.append("origines")
        if "renaissance" in it: themes.append("renaissance")
        if "protection" in it: themes.append("protection")

    txt="### Interprétation générale du tirage\n"
    if cycles>1: txt+="- Cycle dominant : transformation lente.\n"
    if "action" in energies: txt+="- Une action immédiate est favorisée.\n"
    if "abondance" in energies: txt+="- Expansion ou opportunités positives.\n"
    if "intuition" in themes: txt+="- L’intuition est essentielle.\n"
    if "origines" in themes: txt+="- Retour aux fondements personnels.\n"
    if "renaissance" in themes: txt+="- Une renaissance intérieure est en cours.\n"
    if "protection" in themes: txt+="- Présence d’une énergie protectrice.\n"
    if txt.strip()=="### Interprétation générale du tirage":
        txt+="Tirage neutre ou en attente d’évolution."
    return txt

def export_markdown(tirage):
    md="---\ntitle: 'Tirage du '+str(datetime.now().date())+'"\ndate: "+str(datetime.now().date())+"\n---\n\n"
    md+="# Résultat du tirage\n\n"
    for num in tirage:
        c=cards[str(num)]
        md+=f"## Carte {num} – {c['nom']}\n"
        md+=f"![{c['nom']}](images/{c['image']})\n"
        for t in c["texte"]:
            md+=f"- {t}\n"
        md+=f"**Interprétation :** {c['interpretation']}\n\n"
    md+="\n"+interpretation_generale(tirage)
    return md

st.title("Jeu Divinatoire – Version 3 (Galerie + 7 cartes + Export + API)")

# Galerie
st.header("Galerie des 24 cartes")
cols=st.columns(3)
for i,num in enumerate(cards.keys()):
    with cols[i%3]:
        afficher_carte(int(num), container=cols[i%3], width=180)

# Grand tirage 7 cartes
st.header("Grand Tirage 7 Cartes")
if st.button("Tirer 7 cartes"):
    tirage=random.sample(range(1,25),7)
    cols7=st.columns(3)
    for idx,num in enumerate(tirage):
        afficher_carte(num, cols7[idx%3], width=200)
    st.markdown(interpretation_generale(tirage))
    md=export_markdown(tirage)
    st.download_button("Exporter en Markdown HexoJS", data=md, file_name="tirage.md")
