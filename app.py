
import streamlit as st, os, json, random
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

with open("data/cards.json",encoding="utf-8") as f:
    cards=json.load(f)

st.title("Jeu Divinatoire – V5 (Minimal Demo)")

st.header("Tirage Vocal")
audio=st.file_uploader("Envoyez votre audio", type=["wav","mp3","m4a"])
if audio:
    res=client.audio.transcriptions.create(file=audio, model="whisper-1", language="fr")
    st.write("Vous avez dit :", res.text)

st.header("Cartes")
cols=st.columns(3)
for i in range(1,25):
    with cols[(i-1)%3]:
        c=cards[i]
        st.image("images/"+c["image"])
        st.write(c["nom"])
