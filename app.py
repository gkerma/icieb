import streamlit as st
import random

# -------------------------------------------------------------------
#  DÉFINITION COMPLÈTE DES 24 CARTES AVEC TEXTES + INTERPRÉTATION
# -------------------------------------------------------------------

cards = {
    1: {
        "nom": "Source",
        "symboles": "Montagnes, spirales, étoile colorée.",
        "texte": [
            "Le retour aux origines",
            "Les sagesses ancestrales",
            "Les connaissances anciennes"
        ],
        "interpretation": "Carte des racines, du fondement intérieur, du retour à l’essentiel. Elle indique une purification, un recentrage ou une vérité première."
    },
    2: {
        "nom": "Cycles",
        "symboles": "Cercle lunaire, formes circulaires.",
        "texte": [
            "Les phases de la lune",
            "Le cycle des saisons",
            "Les boucles sans fin"
        ],
        "interpretation": "Représente l’apprentissage par répétition, les rythmes temporels, le karma, les retours et les renaissances successives."
    },
    3: {
        "nom": "Surprise",
        "symboles": "Jaillissement orange/jaune.",
        "texte": [
            "Les directions de la vie",
            "Les images des rêves",
            "Le souvenir des merveilles"
        ],
        "interpretation": "Symbole d’intuition soudaine, de synchronicité, d’événement inattendu. Invitation à l’ouverture."
    },
    4: {
        "nom": "Réalisation",
        "symboles": "Oiseau / origami multicolore.",
        "texte": [
            "Le hasard des mélanges",
            "Les découvertes humaines",
            "Les inventions technologiques"
        ],
        "interpretation": "Créativité technique, assemblage ingénieux, concrétisation. Le monde des idées devient matière."
    },
    5: {
        "nom": "Battement",
        "symboles": "Cœur rose stylisé.",
        "texte": [
            "Les rythmes invisibles",
            "Les sourires cachés",
            "Le reflet caché"
        ],
        "interpretation": "Émotions subtiles, intuitions du cœur, signaux faibles. Sensibilité accrue."
    },
    6: {
        "nom": "Souffle",
        "symboles": "Papillon turquoise.",
        "texte": [
            "Les mouvements de la vie",
            "Les échanges invisibles",
            "Le sourire annoncé"
        ],
        "interpretation": "Communication légère, message à venir, respiration nouvelle, nouvelle relation."
    },
    7: {
        "nom": "Passé",
        "symboles": "Carrés bleus superposés (strates).",
        "texte": [
            "Les civilisations perdues",
            "Les 7 merveilles du Monde",
            "Le temps perdu"
        ],
        "interpretation": "Mémoire, nostalgie, héritage, exploration de traces anciennes. Questionner l’histoire personnelle."
    },
    8: {
        "nom": "Maintenant",
        "symboles": "Étoile à 8 branches.",
        "texte": [
            "Le joker",
            "Les matins ensoleillés",
            "Les instants présents"
        ],
        "interpretation": "Puissance immédiate, opportunité directe. C’est la carte de l’action instantanée."
    },
    9: {
        "nom": "Séduction",
        "symboles": "Fleur multicolore.",
        "texte": [
            "Le plaisir de l’enfance",
            "Les jeux de société",
            "Les musiques de la nature"
        ],
        "interpretation": "Joie, charme, attraction naturelle, innocence. Retour au jeu."
    },
    10: {
        "nom": "Espoirs",
        "symboles": "Bulbe lumineux violet/bleu.",
        "texte": [
            "Les projets d’avenir",
            "Les clés de la réussite",
            "Le plaisir de l’inconnu"
        ],
        "interpretation": "Projection positive, confiance, futur ouvert, croissance personnelle."
    },
    11: {
        "nom": "Oubli",
        "symboles": "Nuage bleu.",
        "texte": [
            "Les douleurs du passé",
            "Les événements tragiques",
            "Le désir de l’enfance"
        ],
        "interpretation": "Lâcher prise, deuil, effacement, dissolution nécessaire. Disparition d’un poids."
    },
    12: {
        "nom": "Secret",
        "symboles": "Personnage méditatif.",
        "texte": [
            "Les autres",
            "Les échanges discrets",
            "Le monde personnel"
        ],
        "interpretation": "Intériorité, silence, mystère, intuition sociale, confidences."
    },
    13: {
        "nom": "Enfant",
        "symboles": "Visage rond jaune.",
        "texte": [
            "Les projets d’avenir",
            "Les sourires de demain",
            "Le bonheur de la jeunesse"
        ],
        "interpretation": "Naissance d’idée, renouveau, énergie jeune, innocence créatrice."
    },
    14: {
        "nom": "Mère",
        "symboles": "Oiseau sacré / figure maternelle.",
        "texte": [
            "Les origines du Monde",
            "Les remèdes ancestraux",
            "Le souvenir de la douceur"
        ],
        "interpretation": "Protection, soin, guérison, enracinement féminin."
    },
    15: {
        "nom": "Père",
        "symboles": "Figure rouge + disque doré.",
        "texte": [
            "Les sources d’inspiration",
            "Les recettes anciennes",
            "Le pouvoir de la famille"
        ],
        "interpretation": "Transmission, force, cadre, structure, sagesse masculine."
    },
    16: {
        "nom": "Avatar",
        "symboles": "Masques, bras levés, outils.",
        "texte": [
            "Les costumes de la vie",
            "Les ombres et lumières",
            "Le parcours discret"
        ],
        "interpretation": "Rôles sociaux, identité variable, illusions, double jeu."
    },
    17: {
        "nom": "Dieu",
        "symboles": "Goutte rose, ailes vertes.",
        "texte": [
            "Les croyances personnelles",
            "Les sociétés secrètes",
            "Le souvenir d’un faiseur"
        ],
        "interpretation": "Foi, énergie créatrice, spiritualité, ordres invisibles."
    },
    18: {
        "nom": "Labyrinthe",
        "symboles": "Spirale verte + pointe orange.",
        "texte": [
            "Le parcours initiatique",
            "Les chemins de traverse",
            "Les portes dérobées"
        ],
        "interpretation": "Épreuve, choix, investigation, quête profonde."
    },
    19: {
        "nom": "Ève",
        "symboles": "Silhouette féminine rose.",
        "texte": [
            "Les mères des mères",
            "Les femmes du monde",
            "Le premier pas"
        ],
        "interpretation": "Origine féminine, douceur, intuition, premier élan."
    },
    20: {
        "nom": "Adam",
        "symboles": "Silhouette masculine.",
        "texte": [
            "Les pères des anciens",
            "Les premiers hommes",
            "Le premier voyageur"
        ],
        "interpretation": "Initiative, exploration, ascendance masculine."
    },
    21: {
        "nom": "Automne",
        "symboles": "Arbre plein de fruits.",
        "texte": [
            "Le temps d’après",
            "Les fins de cycles",
            "Les souvenirs de demain"
        ],
        "interpretation": "Récolte, transition, bilan, acheminement vers autre chose."
    },
    22: {
        "nom": "Hiver",
        "symboles": "Arbre gelé, flocons.",
        "texte": [
            "Les fins des temps",
            "Les réserves de froid",
            "Le blanc immaculé"
        ],
        "interpretation": "Pause, purification, immobilité sacrée, morte saison."
    },
    23: {
        "nom": "Printemps",
        "symboles": "Spirale verte + bourgeons.",
        "texte": [
            "Le début de la route",
            "Les premiers amusements",
            "Les parfums floraux"
        ],
        "interpretation": "Renaissance, élan, joie, croissance."
    },
    24: {
        "nom": "Été",
        "symboles": "Foudre jaune, chaleur, silhouette mauve.",
        "texte": [
            "Les fruits et saveurs",
            "Les réserves de chaleur",
            "Le temps des jeux"
        ],
        "interpretation": "Vitalité, intensité, abondance, énergie solaire."
    }
}

# -------------------------------------------------------------------
#  Interface Streamlit
# -------------------------------------------------------------------

st.title("Jeu Divinatoire des 24 Cartes – Version Complète")

st.markdown("Système de tirage interactif avec interprétations détaillées et le contenu exact des cartes.")


# -------------------------
# Tirage simple
# -------------------------
st.header("Tirage simple (1 carte)")
if st.button("Tirer une carte"):
    n = random.randint(1, 24)
    carte = cards[n]
    st.subheader(f"Carte {n} – {carte['nom']}")
    st.write(f"**Symboles :** {carte['symboles']}")
    st.write("**Texte de la carte :**")
    for t in carte["texte"]:
        st.write(f"- {t}")
    st.write(f"**Interprétation :** {carte['interpretation']}")


# -------------------------
# Tirage en 3 cartes
# -------------------------
st.header("Tirage en 3 cartes")
if st.button("Tirage 3 cartes"):
    positions = ["Situation actuelle", "Obstacle / dynamique cachée", "Résolution"]
    tirage = random.sample(range(1, 24), 3)
    for pos, num in zip(positions, tirage):
        c = cards[num]
        st.subheader(f"{pos} – Carte {num} : {c['nom']}")
        st.write(f"**Symboles :** {c['symboles']}")
        for t in c["texte"]:
            st.write(f"- {t}")
        st.write(f"**Interprétation :** {c['interpretation']}")


# -------------------------
# Tirage saisonnier (4 cartes)
# -------------------------
st.header("Tirage des 4 saisons")
if st.button("Tirage 4 saisons"):
    saisons = ["Printemps", "Été", "Automne", "Hiver"]
    tirage = random.sample(range(1, 24), 4)
    for saison, num in zip(saisons, tirage):
        c = cards[num]
        st.subheader(f"{saison} – Carte {num} : {c['nom']}")
        st.write(f"**Symboles :** {c['symboles']}")
        for t in c["texte"]:
            st.write(f"- {t}")
        st.write(f"**Interprétation :** {c['interpretation']}")
