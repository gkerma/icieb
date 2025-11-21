
import streamlit as st, random, os, json, threading
from datetime import datetime
from fastapi import FastAPI
import uvicorn

st.set_page_config(layout="wide")

IMAGE_PATH="images"

with open("data/cards.json","r",encoding="utf-8") as f:
    cards=json.load(f)

# --- API ---
api = FastAPI()

@api.get("/api/cards")
def all_cards():
    return cards

@api.get("/api/card/{id}")
def card(id:int):
    return cards[str(id)]

def tirage_simple():
    return [random.randint(1,24)]

def tirage_3():
    return random.sample(range(1,25),3)

def tirage_7():
    return random.sample(range(1,25),7)

def tirage_saisons():
    return random.sample(range(1,25),4)

@api.get("/api/tirage/simple")
def api_simple(): return tirage_simple()

@api.get("/api/tirage/3")
def api_3(): return tirage_3()

@api.get("/api/tirage/7")
def api_7(): return tirage_7()

@api.get("/api/tirage/saisons")
def api_saisons(): return tirage_saisons()

def run_api():
    uvicorn.run(api, host="0.0.0.0", port=8000)

threading.Thread(target=run_api, daemon=True).start()

# --- UI functions ---
def afficher_carte(num, container=None, width=240):
    c=cards[str(num)]
    cont=container if container else st
    cont.image(os.path.join(IMAGE_PATH,c["image"]), width=width)
    cont.markdown(f"### {c['nom']}")
    cont.markdown(f"**Symboles :** {c['symboles']}")
    for t in c["texte"]:
        cont.markdown(f"- {t}")
    cont.markdown(f"**Interprétation :** {c['interpretation']}")

def interpretation_generale(tirage):
    return "### Synthèse du tirage\nUne dynamique symbolique émerge..."

def export_markdown(tirage):
    md=f"""---
title: "Tirage du {datetime.now().date()}"
date: {datetime.now().date()}
---

# Résultat du tirage

"""
    for num in tirage:
        c=cards[str(num)]
        md+=f"## Carte {num} – {c['nom']}\n"
        md+=f"![{c['nom']}]({IMAGE_PATH}/{c['image']})\n"
        for t in c["texte"]:
            md+=f"- {t}\n"
        md+=f"**Interprétation :** {c['interpretation']}\n\n"
    md+="\n"+interpretation_generale(tirage)
    return md

st.title("Jeu Divinatoire – Version 4 (API + Popup + Dark Mode + Daily Draw)")

# Daily draw
st.header("Tirage Quotidien")
if "daily" not in st.session_state or st.session_state.daily_date != str(datetime.now().date()):
    if st.button("Générer le tirage du jour"):
        st.session_state.daily = tirage_simple()
        st.session_state.daily_date = str(datetime.now().date())
if "daily" in st.session_state:
    afficher_carte(st.session_state.daily[0])
    st.markdown(f"Tirage du jour : {st.session_state.daily_date}")

# Gallery with modal
st.header("Galerie (clic pour détail)")
cols=st.columns(3)
for i in range(1,25):
    if cols[(i-1)%3].button(cards[str(i)]["nom"], key=f"btn{i}"):
        st.session_state.modal=i
    cols[(i-1)%3].image(os.path.join(IMAGE_PATH,cards[str(i)]["image"]), width=160)

if "modal" in st.session_state:
    with st.modal(cards[str(st.session_state.modal)]["nom"]):
        afficher_carte(st.session_state.modal)
        if st.button("Fermer"):
            del st.session_state.modal

# 7-card draw
st.header("Grand Tirage 7 Cartes")
if st.button("Tirer 7 cartes"):
    t=tirage_7()
    cols7=st.columns(3)
    for idx,num in enumerate(t):
        afficher_carte(num, cols7[idx%3], width=200)
    md=export_markdown(t)
    st.download_button("Exporter en Markdown HexoJS", data=md, file_name="tirage.md")
