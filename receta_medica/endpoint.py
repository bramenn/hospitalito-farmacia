from fastapi import APIRouter
from .consultas import (
    crear_receta_medica_db,
    obtener_receta_medica_id_db,
    entregar_receta_medica_cc_db,
)

from .modelo import RecetaMedicaIn, RecetaMedicaOut

router = APIRouter()


@router.get("/{id}", response_model=RecetaMedicaOut)
def obtener_receta_medica(id: str):
    receta_medica = obtener_receta_medica_id_db(id)
    return receta_medica


@router.post("/", response_model=RecetaMedicaOut)
def crear_receta_medica(nuevo_receta_medica: RecetaMedicaIn):
    receta_medica = crear_receta_medica_db(nuevo_receta_medica)
    return receta_medica


@router.put("/{cc}", response_model=RecetaMedicaOut)
def entregar_receta_medica(cc: str):
    receta_medica = entregar_receta_medica_cc_db(cc)
    return receta_medica
