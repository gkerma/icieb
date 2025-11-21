import streamlit as st
import random

# Définition des cartes
cards = {
    1: ("Source", "Retour aux origines, sagesse ancienne, fondement."),
    2: ("Cycles", "Répétition, apprentissage, mouvements lunaires."),
    3: ("Surprise", "Révélation, intuition, émergence soudaine."),
    4: ("Réalisation", "Ingéniosité, création, découverte humaine."),
    5: ("Battement", "Rythmes invisibles, émotions fines, écoute intérieure."),
    6: ("Souffle", "Souhait, échange, légèreté."),
    7: ("Passé", "Ancêtres, mémoire, civilisations perdues."),
    8: ("Maintenant", "Présence, décision immédiate, instant vécu."),
    9: ("Séduction", "Joie, enfance, attraction naturelle."),
    10: ("Espoirs", "Futur, confiance, plaisir de l’inconnu."),
    11: ("Oubli", "Lâcher prise, trauma, dissolution."),
    12: ("Secret", "Intériorité, monde personnel, discrétion."),
    13: ("Enfant", "Renouveau, spontanéité, projets futurs."),
    14: ("Mère", "Protection, soin, remèdes ancestraux."),
    15: ("Père", "Ancrage, modèle, force constructive."),
    16: ("Avatar", "Identité, rôle, masques de la vie."),
    17: ("Dieu", "Foi, absolu, création personnelle."),
    18: ("Labyrinthe", "Quête, choix, chemins complexes."),
    19: ("Ève", "Origine féminine, douceur, intuition."),
    20: ("Adam", "Origine masculine, voyage, décision."),
    21: ("Automne", "Transition, bilan, fin de cycle."),
    22: ("Hiver", "Pause, purification, silence."),
    23: ("Printemps", "Début, floraison, départ."),
    24: ("Été", "Puissance, chaleur, mouvement.")
}

st.title("Tirage Divinatoire – Jeu des 24 Cartes")

tirage = st.button("Tirer une carte")

if tirage:
    n = random.randint(1, 24)
    name, meaning = cards[n]
    st.subheader(f"Carte {n} : {name}")
    st.write(meaning)