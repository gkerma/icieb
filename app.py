import streamlit as st
import random
import os

# -------------------------------------------------------------------
# Localisation des images (placez vos PNG dans un dossier 'images')
# -------------------------------------------------------------------
IMAGE_PATH = "images"   # Exemple : images/carte_01.png

# -------------------------------------------------------------------
# Cartes (données complètes)
# -------------------------------------------------------------------

cards = {
    1: {"nom": "Source", "symboles": "Montagnes, spirales, étoile colorée.",
        "texte": ["Le retour aux origines", "Les sagesses ancestrales", "Les connaissances anciennes"],
        "interpretation": "Carte des racines, du fondement intérieur.", "image": "carte_01.png"},
    2: {"nom": "Cycles", "symboles": "Cercle lunaire, formes circulaires.",
        "texte": ["Les phases de la lune", "Le cycle des saisons", "Les boucles sans fin"],
        "interpretation": "Apprentissage par répétition, karma.", "image": "carte_02.png"},
    3: {"nom": "Surprise", "symboles": "Jaillissement lumineux.",
        "texte": ["Les directions de la vie", "Les images des rêves", "Le souvenir des merveilles"],
        "interpretation": "Éveil, surprise, synchronicité.", "image": "carte_03.png"},
    # ...
    # Continuez les cartes jusqu'à 24
    # ...
    24: {"nom": "Été", "symboles": "Foudre jaune, chaleur.",
        "texte": ["Les fruits et saveurs", "Les réserves de chaleur", "Le temps des jeux"],
        "interpretation": "Vitalité, intensité, abondance.",
        "image": "carte_24.png"},
}

# -------------------------------------------------------------------
# Fonctions d’affichage
# -------------------------------------------------------------------

def afficher_carte(num):
    carte = cards[num]
    st.subheader(f"Carte {num} – {carte['nom']}")

    # Affiche l'image si elle existe
    img_path = os.path.join(IMAGE_PATH, carte["image"])
    if os.path.exists(img_path):
        st.image(img_path, use_column_width=True)

    st.write(f"**Symboles :** {carte['symboles']}")
    st.write("**Texte de la carte :**")
    for t in carte["texte"]:
        st.write(f"- {t}")
    st.write(f"**Interprétation :** {carte['interpretation']}")


# -------------------------------------------------------------------
# Application
# -------------------------------------------------------------------

st.title("Jeu Divinatoire des 24 Cartes – Version Illustrée")

st.markdown("Tirage interactif avec textes + images extraites du PDF.")

# Tirage simple
st.header("Tirage simple")
if st.button("Tirer 1 carte"):
    n = random.randint(1, 24)
    afficher_carte(n)

# Tirage 3 cartes
st.header("Tirage en 3 cartes")
if st.button("Tirer 3 cartes"):
    tirage = random.sample(range(1, 24), 3)
    positions = ["Situation", "Obstacle", "Résolution"]
    for pos, num in zip(positions, tirage):
        st.markdown(f"### {pos}")
        afficher_carte(num)

# Tirage 4 saisons
st.header("Tirage des 4 saisons")
if st.button("Tirage 4 cartes"):
    tirage = random.sample(range(1, 24), 4)
    saisons = ["Printemps", "Été", "Automne", "Hiver"]
    for saison, num in zip(saisons, tirage):
        st.markdown(f"### {saison}")
        afficher_carte(num)
