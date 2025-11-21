import streamlit as st
import random
import os

IMAGE_PATH = "images"

# load cards dynamically
cards = {
}
# Minimal placeholder list based on numbering
for i in range(1,25):
    cards[i] = {"nom": f"Carte {i}", "image": f"carte_{i:02d}.png"}

def afficher_carte(num):
    c = cards[num]
    st.subheader(f"Carte {num} – {c['nom']}")
    img_path = os.path.join(IMAGE_PATH, c["image"])
    if os.path.exists(img_path):
        st.image(img_path, use_column_width=True)

st.title("Pack Streamlit prêt à déployer")

if st.button("Tirer une carte"):
    afficher_carte(random.randint(1,24))
