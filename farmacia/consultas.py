from .modelo import Farmacia, FarmaciaIn, FarmaciaOut
from fastapi import status
from fastapi.exceptions import HTTPException
import db

from farmacia.modelo import FarmaciaOut, Farmacia


def obtener_farmacia_id_db(id: str) -> FarmaciaOut:
    farmacia = db.session.query(Farmacia).where(Farmacia.id == id).first()

    if not farmacia:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Farmacia no encontrada"
        )

    return parsear_farmacia(farmacia)


def crear_farmacia_db(nueva_farmacia: FarmaciaIn) -> FarmaciaOut:

    farmacia = Farmacia(nombre=nueva_farmacia.nombre)

    try:
        db.session.add(farmacia)
        db.session.commit()
        return parsear_farmacia(farmacia)
    except:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado la farmacia",
        )


def parsear_farmacia(farmacia: Farmacia) -> FarmaciaOut:
    return FarmaciaOut(id=farmacia.id, nombre=farmacia.nombre)
