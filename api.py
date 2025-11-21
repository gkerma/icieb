from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import os
import random

# -----------------------------------------------------
# CONFIG
# -----------------------------------------------------

DATA_PATH = os.path.join("data", "cards.json")

if not os.path.exists(DATA_PATH):
    raise RuntimeError(f"Fichier de données introuvable : {DATA_PATH}")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    cards = json.load(f)  # dict avec clés "1"..."24"


# -----------------------------------------------------
# APP FASTAPI
# -----------------------------------------------------

api = FastAPI(
    title="Jeu Divinatoire – API",
    description="API REST pour les cartes, tirages et intégration externe.",
    version="1.0.0",
)

# CORS (pour consommer l’API depuis front JS, streamlit, etc.)
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # à restreindre si besoin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------------------------------
# FONCTIONS INTERNES
# -----------------------------------------------------

def get_card_or_404(card_id: int) -> dict:
    key = str(card_id)
    if key not in cards:
        raise HTTPException(status_code=404, detail="Carte introuvable")
    return cards[key]


def tirage_simple():
    return [random.randint(1, 24)]


def tirage_3():
    return random.sample(range(1, 25), 3)


def tirage_7():
    return random.sample(range(1, 25), 7)


def tirage_saisons():
    # 4 cartes génériques, votre logique peut être adaptée
    return random.sample(range(1, 25), 4)


def tirage_quotidien():
    # côté serveur : simple aléatoire
    # si vous voulez un tirage stable par jour, il faut ajouter une graine selon la date
    return tirage_simple()


# -----------------------------------------------------
# ENDPOINTS
# -----------------------------------------------------

@api.get("/api/cards")
def list_cards():
    """Retourne la liste complète des cartes."""
    # renvoyer une liste pour un format plus consommable
    return [{"id": int(k), **v} for k, v in cards.items()]


@api.get("/api/card/{card_id}")
def get_card(card_id: int):
    """Retourne une carte spécifique par son id (1–24)."""
    c = get_card_or_404(card_id)
    return {"id": card_id, **c}


@api.get("/api/tirage/simple")
def api_tirage_simple():
    """Tirage 1 carte."""
    tirage = tirage_simple()
    return {
        "type": "simple",
        "cartes": tirage,
    }


@api.get("/api/tirage/3")
def api_tirage_3():
    """Tirage 3 cartes (classique : situation / obstacle / résolution)."""
    tirage = tirage_3()
    return {
        "type": "3_cartes",
        "positions": ["situation", "obstacle", "resolution"],
        "cartes": tirage,
    }


@api.get("/api/tirage/7")
def api_tirage_7():
    """Grand tirage 7 cartes."""
    tirage = tirage_7()
    return {
        "type": "7_cartes",
        "cartes": tirage,
    }


@api.get("/api/tirage/saisons")
def api_tirage_saisons():
    """Tirage des 4 saisons."""
    tirage = tirage_saisons()
    return {
        "type": "saisons",
        "saisons": ["printemps", "ete", "automne", "hiver"],
        "cartes": tirage,
    }


@api.get("/api/tirage/quotidien")
def api_tirage_quotidien():
    """Tirage quotidien (1 carte)."""
    tirage = tirage_quotidien()
    return {
        "type": "quotidien",
        "date": str(__import__("datetime").date.today()),
        "cartes": tirage,
    }
