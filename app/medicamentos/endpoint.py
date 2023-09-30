from fastapi import APIRouter

from .consultas import crear_medicamento_db, obtener_medicamento_nombre_db
from .modelo import MedicamentoIn, MedicamentoOut

router = APIRouter()


@router.get("/{nombre}", response_model=MedicamentoOut)
def obtener_medicamento(nombre: str):
    medicamento = obtener_medicamento_nombre_db(nombre)
    return medicamento


@router.post("/", response_model=MedicamentoOut)
def crear_medicamento(nuevo_medicamento: MedicamentoIn):
    medicamento = crear_medicamento_db(nuevo_medicamento)
    return medicamento
