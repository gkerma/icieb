import streamlit as st, random, os

st.set_page_config(page_title='Jeu Divinatoire', layout='wide')
IMAGE_PATH='images'
cards = {1: {'nom': 'Source', 'symboles': 'Montagnes, spirales, étoile colorée.', 'texte': ['Le retour aux origines', 'Les sagesses ancestrales', 'Les connaissances anciennes'], 'interpretation': 'Racines, fondation, vérité première.', 'image': 'carte_01.png'}, 2: {'nom': 'Cycles', 'symboles': 'Cercle lunaire.', 'texte': ['Les phases de la lune', 'Le cycle des saisons', 'Les boucles sans fin'], 'interpretation': 'Rythmes, répétition, apprentissage.', 'image': 'carte_02.png'}, 3: {'nom': 'Surprise', 'symboles': 'Jaillissement lumineux.', 'texte': ['Les directions de la vie', 'Les images des rêves', 'Le souvenir des merveilles'], 'interpretation': 'Éveil soudain, synchronicité.', 'image': 'carte_03.png'}, 4: {'nom': 'Réalisation', 'symboles': 'Oiseau/origami.', 'texte': ['Le hasard des mélanges', 'Les découvertes humaines', 'Les inventions technologiques'], 'interpretation': 'Création, invention, construction.', 'image': 'carte_04.png'}, 5: {'nom': 'Battement', 'symboles': 'Cœur stylisé.', 'texte': ['Les rythmes invisibles', 'Les sourires cachés', 'Le reflet caché'], 'interpretation': 'Sensibilité, intuition émotionnelle.', 'image': 'carte_05.png'}, 6: {'nom': 'Souffle', 'symboles': 'Papillon.', 'texte': ['Les mouvements de la vie', 'Les échanges invisibles', 'Le sourire annoncé'], 'interpretation': 'Légèreté, message subtil.', 'image': 'carte_06.png'}, 7: {'nom': 'Passé', 'symboles': 'Strates bleues.', 'texte': ['Les civilisations perdues', 'Les 7 merveilles du Monde', 'Le temps perdu'], 'interpretation': 'Mémoire, histoire profonde.', 'image': 'carte_07.png'}, 8: {'nom': 'Maintenant', 'symboles': 'Étoile.', 'texte': ['Le joker', 'Les matins ensoleillés', 'Les instants présents'], 'interpretation': 'Action immédiate.', 'image': 'carte_08.png'}, 9: {'nom': 'Séduction', 'symboles': 'Fleur.', 'texte': ['Le plaisir de l’enfance', 'Les jeux de société', 'Les musiques de la nature'], 'interpretation': 'Joie, charme.', 'image': 'carte_09.png'}, 10: {'nom': 'Espoirs', 'symboles': 'Bulbe lumineux.', 'texte': ['Les projets d’avenir', 'Les clés de la réussite', 'Le plaisir de l’inconnu'], 'interpretation': 'Confiance, futur ouvert.', 'image': 'carte_10.png'}, 11: {'nom': 'Oubli', 'symboles': 'Nuage.', 'texte': ['Les douleurs du passé', 'Les événements tragiques', 'Le désir de l’enfance'], 'interpretation': 'Lâcher prise.', 'image': 'carte_11.png'}, 12: {'nom': 'Secret', 'symboles': 'Figure méditative.', 'texte': ['Les autres', 'Les échanges discrets', 'Le monde personnel'], 'interpretation': 'Intériorité, mystère.', 'image': 'carte_12.png'}, 13: {'nom': 'Enfant', 'symboles': 'Visage rond.', 'texte': ['Les projets d’avenir', 'Les sourires de demain', 'Le bonheur de la jeunesse'], 'interpretation': 'Renouveau.', 'image': 'carte_13.png'}, 14: {'nom': 'Mère', 'symboles': 'Oiseau sacré.', 'texte': ['Les origines du Monde', 'Les remèdes ancestraux', 'Le souvenir de la douceur'], 'interpretation': 'Protection, soin.', 'image': 'carte_14.png'}, 15: {'nom': 'Père', 'symboles': 'Figure rouge.', 'texte': ['Les sources d’inspiration', 'Les recettes anciennes', 'Le pouvoir de la famille'], 'interpretation': 'Structure, transmission.', 'image': 'carte_15.png'}, 16: {'nom': 'Avatar', 'symboles': 'Masques.', 'texte': ['Les costumes de la vie', 'Les ombres et lumières', 'Le parcours discret'], 'interpretation': 'Rôle, identité mouvante.', 'image': 'carte_16.png'}, 17: {'nom': 'Dieu', 'symboles': 'Goutte + ailes.', 'texte': ['Les croyances personnelles', 'Les sociétés secrètes', 'Le souvenir d’un faiseur'], 'interpretation': 'Foi, création.', 'image': 'carte_17.png'}, 18: {'nom': 'Labyrinthe', 'symboles': 'Spirale + pointe.', 'texte': ['Le parcours initiatique', 'Les chemins de traverse', 'Les portes dérobées'], 'interpretation': 'Quête, choix.', 'image': 'carte_18.png'}, 19: {'nom': 'Ève', 'symboles': 'Féminin.', 'texte': ['Les mères des mères', 'Les femmes du monde', 'Le premier pas'], 'interpretation': 'Intuition, douceur.', 'image': 'carte_19.png'}, 20: {'nom': 'Adam', 'symboles': 'Masculin.', 'texte': ['Les pères des anciens', 'Les premiers hommes', 'Le premier voyageur'], 'interpretation': 'Élan, décision.', 'image': 'carte_20.png'}, 21: {'nom': 'Automne', 'symboles': 'Arbre fruité.', 'texte': ['Le temps d’après', 'Les fins de cycles', 'Les souvenirs de demain'], 'interpretation': 'Transition, récolte.', 'image': 'carte_21.png'}, 22: {'nom': 'Hiver', 'symboles': 'Arbre gelé.', 'texte': ['Les fins des temps', 'Les réserves de froid', 'Le blanc immaculé'], 'interpretation': 'Pause, purification.', 'image': 'carte_22.png'}, 23: {'nom': 'Printemps', 'symboles': 'Spirale verte.', 'texte': ['Le début de la route', 'Les premiers amusements', 'Les parfums floraux'], 'interpretation': 'Renaissance.', 'image': 'carte_23.png'}, 24: {'nom': 'Été', 'symboles': 'Foudre.', 'texte': ['Les fruits et saveurs', 'Les réserves de chaleur', 'Le temps des jeux'], 'interpretation': 'Abondance.', 'image': 'carte_24.png'}}


def afficher_carte(num):
    c = cards[num]
    st.markdown(f"## Carte {num} – {c['nom']}")
    img = os.path.join(IMAGE_PATH, c["image"])
    if os.path.exists(img):
        st.image(img, width=300)
    st.markdown(f"**Symboles :** {c['symboles']}")
    st.markdown("**Texte :**")
    for t in c["texte"]:
        st.markdown(f"- {t}")
    st.markdown(f"**Interprétation :** {c['interpretation']}")

st.title("Jeu Divinatoire des 24 Cartes – Version Complète Illustrée")

col1, col2 = st.columns(2)
with col1:
    if st.button("Tirage simple"):
        afficher_carte(random.randint(1,24))

with col2:
    if st.button("Tirage 3 cartes"):
        tirage = random.sample(range(1,25),3)
        noms = ["Situation","Obstacle","Résolution"]
        for lbl, num in zip(noms, tirage):
            st.subheader(lbl)
            afficher_carte(num)

st.header("Tirage des 4 saisons")
if st.button("Tirage saisonnier"):
    tirage = random.sample(range(1,25),4)
    saisons = ["Printemps","Été","Automne","Hiver"]
    for s, num in zip(saisons, tirage):
        st.subheader(s)
        afficher_carte(num)
