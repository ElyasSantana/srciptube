from fastapi import APIRouter
from models.papel import Papel


router = APIRouter()

banco_de_dados = []


@router.post("/")
def add_item(papel: Papel):
    banco_de_dados.append(papel)
    return papel


@router.get("/")
def list_item():
    return banco_de_dados
