import streamlit as st, random, os

st.set_page_config(page_title='Jeu Divinatoire', layout='wide')
IMAGE_PATH='images'
cards = {1: {'nom': 'Source', 'symboles': 'Montagnes, spirales, étoile colorée.', 'texte': ['Le retour aux origines', 'Les sagesses ancestrales', 'Les connaissances anciennes'], 'interpretation': 'Racines, fondation, vérité première.', 'image': 'carte_01.png'}, 2: {'nom': 'Cycles', 'symboles': 'Cercle lunaire.', 'texte': ['Les phases de la lune', 'Le cycle des saisons', 'Les boucles sans fin'], 'interpretation': 'Rythmes, répétition, apprentissage.', 'image': 'carte_02.png'}, 3: {'nom': 'Surprise', 'symboles': 'Jaillissement lumineux.', 'texte': ['Les directions de la vie', 'Les images des rêves', 'Le souvenir des merveilles'], 'interpretation': 'Éveil soudain, synchronicité.', 'image': 'carte_03.png'}, 4: {'nom': 'Réalisation', 'symboles': 'Oiseau/origami.', 'texte': ['Le hasard des mélanges', 'Les découvertes humaines', 'Les inventions technologiques'], 'interpretation': 'Création, invention, construction.', 'image': 'carte_04.png'}, 5: {'nom': 'Battement', 'symboles': 'Cœur stylisé.', 'texte': ['Les rythmes invisibles', 'Les sourires cachés', 'Le reflet caché'], 'interpretation': 'Sensibilité, intuition émotionnelle.', 'image': 'carte_05.png'}, 6: {'nom': 'Souffle', 'symboles': 'Papillon.', 'texte': ['Les mouvements de la vie', 'Les échanges invisibles', 'Le sourire annoncé'], 'interpretation': 'Légèreté, message subtil.', 'image': 'carte_06.png'}, 7: {'nom': 'Passé', 'symboles': 'Strates bleues.', 'texte': ['Les civilisations perdues', 'Les 7 merveilles du Monde', 'Le temps perdu'], 'interpretation': 'Mémoire, histoire profonde.', 'image': 'carte_07.png'}, 8: {'nom': 'Maintenant', 'symboles': 'Étoile.', 'texte': ['Le joker', 'Les matins ensoleillés', 'Les instants présents'], 'interpretation': 'Action immédiate.', 'image': 'carte_08.png'}, 9: {'nom': 'Séduction', 'symboles': 'Fleur.', 'texte': ['Le plaisir de l’enfance', 'Les jeux de société', 'Les musiques de la nature'], 'interpretation': 'Joie, charme.', 'image': 'carte_09.png'}, 10: {'nom': 'Espoirs', 'symboles': 'Bulbe lumineux.', 'texte': ['Les projets d’avenir', 'Les clés de la réussite', 'Le plaisir de l’inconnu'], 'interpretation': 'Confiance, futur ouvert.', 'image': 'carte_10.png'}, 11: {'nom': 'Oubli', 'symboles': 'Nuage.', 'texte': ['Les douleurs du passé', 'Les événements tragiques', 'Le désir de l’enfance'], 'interpretation': 'Lâcher prise.', 'image': 'carte_11.png'}, 12: {'nom': 'Secret', 'symboles': 'Figure méditative.', 'texte': ['Les autres', 'Les échanges discrets', 'Le monde personnel'], 'interpretation': 'Intériorité, mystère.', 'image': 'carte_12.png'}, 13: {'nom': 'Enfant', 'symboles': 'Visage rond.', 'texte': ['Les projets d’avenir', 'Les sourires de demain', 'Le bonheur de la jeunesse'], 'interpretation': 'Renouveau.', 'image': 'carte_13.png'}, 14: {'nom': 'Mère', 'symboles': 'Oiseau sacré.', 'texte': ['Les origines du Monde', 'Les remèdes ancestraux', 'Le souvenir de la douceur'], 'interpretation': 'Protection, soin.', 'image': 'carte_14.png'}, 15: {'nom': 'Père', 'symboles': 'Figure rouge.', 'texte': ['Les sources d’inspiration', 'Les recettes anciennes', 'Le pouvoir de la famille'], 'interpretation': 'Structure, transmission.', 'image': 'carte_15.png'}, 16: {'nom': 'Avatar', 'symboles': 'Masques.', 'texte': ['Les costumes de la vie', 'Les ombres et lumières', 'Le parcours discret'], 'interpretation': 'Rôle, identité mouvante.', 'image': 'carte_16.png'}, 17: {'nom': 'Dieu', 'symboles': 'Goutte + ailes.', 'texte': ['Les croyances personnelles', 'Les sociétés secrètes', 'Le souvenir d’un faiseur'], 'interpretation': 'Foi, création.', 'image': 'carte_17.png'}, 18: {'nom': 'Labyrinthe', 'symboles': 'Spirale + pointe.', 'texte': ['Le parcours initiatique', 'Les chemins de traverse', 'Les portes dérobées'], 'interpretation': 'Quête, choix.', 'image': 'carte_18.png'}, 19: {'nom': 'Ève', 'symboles': 'Féminin.', 'texte': ['Les mères des mères', 'Les femmes du monde', 'Le premier pas'], 'interpretation': 'Intuition, douceur.', 'image': 'carte_19.png'}, 20: {'nom': 'Adam', 'symboles': 'Masculin.', 'texte': ['Les pères des anciens', 'Les premiers hommes', 'Le premier voyageur'], 'interpretation': 'Élan, décision.', 'image': 'carte_20.png'}, 21: {'nom': 'Automne', 'symboles': 'Arbre fruité.', 'texte': ['Le temps d’après', 'Les fins de cycles', 'Les souvenirs de demain'], 'interpretation': 'Transition, récolte.', 'image': 'carte_21.png'}, 22: {'nom': 'Hiver', 'symboles': 'Arbre gelé.', 'texte': ['Les fins des temps', 'Les réserves de froid', 'Le blanc immaculé'], 'interpretation': 'Pause, purification.', 'image': 'carte_22.png'}, 23: {'nom': 'Printemps', 'symboles': 'Spirale verte.', 'texte': ['Le début de la route', 'Les premiers amusements', 'Les parfums floraux'], 'interpretation': 'Renaissance.', 'image': 'carte_23.png'}, 24: {'nom': 'Été', 'symboles': 'Foudre.', 'texte': ['Les fruits et saveurs', 'Les réserves de chaleur', 'Le temps des jeux'], 'interpretation': 'Abondance.', 'image': 'carte_24.png'}}


# ------------------------------------------------------------
#  FONCTION D’AFFICHAGE AVEC COLONNES
# ------------------------------------------------------------

def afficher_carte(num, container=None):
    """Affiche une carte dans un conteneur (colonne)"""
    c = cards[num]
    if container:
        cont = container
    else:
        cont = st

    cont.markdown(f"### Carte {num} – {c['nom']}")
    img = os.path.join(IMAGE_PATH, c["image"])
    if os.path.exists(img):
        cont.image(img, width=240)

    cont.markdown(f"**Symboles :** {c['symboles']}")
    cont.markdown("**Texte inscrit :**")
    for t in c["texte"]:
        cont.markdown(f"- {t}")
    cont.markdown(f"**Interprétation :** {c['interpretation']}")


# ------------------------------------------------------------
#  INTERPRÉTATION GÉNÉRATIVE (sans IA externe)
# ------------------------------------------------------------

def interpretation_generale(tirage):
    """Produit une interprétation synthétique et narrative du tirage."""
    themes = []
    energies = []
    cycles = 0

    for num in tirage:
        c = cards[num]

        # détecter certains motifs narratifs
        if "origine" in c["interpretation"].lower() or "racine" in c["interpretation"].lower():
            themes.append("origines")
        if "cycle" in c["interpretation"].lower():
            cycles += 1
            themes.append("cycle")
        if "éveil" in c["interpretation"].lower() or "intuition" in c["interpretation"].lower():
            themes.append("intuition")
        if "renaissance" in c["interpretation"].lower():
            themes.append("renaissance")
        if "protection" in c["interpretation"].lower():
            themes.append("protection")
        if "action" in c["interpretation"].lower():
            energies.append("action")
        if "abondance" in c["interpretation"].lower():
            energies.append("abondance")

    # Synthèse narrative
    texte = "### Interprétation générale du tirage\n"

    # Energies
    if cycles > 1:
        texte += "- Le tirage montre **une dynamique cyclique forte**, indiquant une situation qui se répète ou se transforme lentement.\n"
    if "action" in energies:
        texte += "- Une **énergie d'action immédiate** est présente : un mouvement ou une décision est favorisé(e).\n"
    if "abondance" in energies:
        texte += "- Une **expansion positive** ou une période d’opportunités est suggérée.\n"

    # Thèmes
    if "intuition" in themes:
        texte += "- L’**intuition** joue un rôle central : écoutez vos ressentis subtils.\n"
    if "origines" in themes:
        texte += "- Retour aux **fondations**, aux motivations profondes.\n"
    if "renaissance" in themes:
        texte += "- Une **renaissance** est en cours : nouveau départ ou régénération interne.\n"
    if "protection" in themes:
        texte += "- Une énergie de **soin** et de protection entoure ce tirage.\n"

    # Conclusion automatique
    if texte.strip() == "### Interprétation générale du tirage":
        texte += "\nLe tirage ne montre pas de tendance explicite : la situation semble neutre ou en attente d’un déclencheur."
    else:
        texte += "\n**Synthèse :** Ce tirage révèle un ensemble d’énergies cohérentes : il met en avant un fil directeur reliant les cartes, qu’il s’agisse de cycles, d’intuition ou d’un renouveau actif."

    return texte


# ------------------------------------------------------------
#  TIRAGE SIMPLE
# ------------------------------------------------------------

st.header("Tirage simple (1 carte)")

if st.button("Tirer 1 carte"):
    n = random.randint(1, 24)
    afficher_carte(n)
    st.markdown(interpretation_generale([n]))


# ------------------------------------------------------------
#  TIRAGE 3 CARTES (EN COLONNES)
# ------------------------------------------------------------

st.header("Tirage en 3 cartes")

if st.button("Tirer 3 cartes"):
    tirage = random.sample(range(1, 25), 3)
    positions = ["Situation actuelle", "Obstacle / dynamique cachée", "Résolution"]

    col1, col2, col3 = st.columns(3)
    colonnes = [col1, col2, col3]

    for pos, num, col in zip(positions, tirage, colonnes):
        col.markdown(f"## {pos}")
        afficher_carte(num, container=col)

    st.markdown(interpretation_generale(tirage))


# ------------------------------------------------------------
#  TIRAGE DES 4 SAISONS (EN COLONNES)
# ------------------------------------------------------------

st.header("Tirage des 4 saisons")

if st.button("Tirage saisonnier"):
    tirage = random.sample(range(1, 25), 4)
    saisons = ["Printemps", "Été", "Automne", "Hiver"]

    col1, col2, col3, col4 = st.columns(4)
    colonnes = [col1, col2, col3, col4]

    for saison, num, col in zip(saisons, tirage, colonnes):
        col.markdown(f"## {saison}")
        afficher_carte(num, container=col)

    st.markdown(interpretation_generale(tirage))

