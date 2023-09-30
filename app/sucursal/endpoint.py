from fastapi import APIRouter
from .consultas import crear_sucursal_db, obtener_sucursal_id_db

from .modelo import SucursalIn, SucursalOut

router = APIRouter()


@router.get("/{id}", response_model=SucursalOut)
def obtener_sucursal(id: str):
    sucursal = obtener_sucursal_id_db(id)
    return sucursal


@router.post("/", response_model=SucursalOut)
def crear_sucursal(nuevo_sucursal: SucursalIn):
    sucursal = crear_sucursal_db(nuevo_sucursal)
    return sucursal
