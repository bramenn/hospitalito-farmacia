from .modelo import Sucursal, SucursalIn, SucursalOut
from fastapi import status
from fastapi.exceptions import HTTPException
import db

from sucursal.modelo import SucursalOut, Sucursal


def obtener_sucursal_id_db(id: str) -> SucursalOut:
    sucursal = db.session.query(Sucursal).where(Sucursal.id == id).first()

    if not sucursal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Sucursal no encontrada"
        )

    return parsear_sucursal(sucursal)


def crear_sucursal_db(nueva_sucursal: SucursalIn) -> SucursalOut:

    sucursal = Sucursal(
        nombre=nueva_sucursal.nombre,
        ubicacion=nueva_sucursal.ubicacion,
        telefono=nueva_sucursal.telefono,
        id_farmacia=nueva_sucursal.id_farmacia,
    )

    try:
        db.session.add(sucursal)
        db.session.commit()
        return parsear_sucursal(sucursal)
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado el sucursal",
        )


def parsear_sucursal(sucursal: Sucursal) -> SucursalOut:
    return SucursalOut(
        id=sucursal.id,
        nombre=sucursal.nombre,
        ubicacion=sucursal.ubicacion,
        telefono=sucursal.telefono,
        id_farmacia=sucursal.id_farmacia,
    )
