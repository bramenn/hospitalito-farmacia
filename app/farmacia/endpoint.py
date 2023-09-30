from fastapi import APIRouter

from .consultas import crear_farmacia_db, obtener_farmacia_id_db
from .modelo import FarmaciaIn, FarmaciaOut

router = APIRouter()


@router.get("/{id}", response_model=FarmaciaOut)
def obtener_farmacia(id: str):
    farmacia = obtener_farmacia_id_db(id)
    return farmacia


@router.post("/", response_model=FarmaciaOut)
def crear_farmacia(nuevo_farmacia: FarmaciaIn):
    farmacia = crear_farmacia_db(nuevo_farmacia)
    return farmacia
