from .. import db
from fastapi import status
from fastapi.exceptions import HTTPException
from .modelo import Medicamento, MedicamentoOut, MedicamentoIn


def obtener_medicamento_id_db(id: str) -> MedicamentoOut:
    medicamento = db.session.query(Medicamento).where(Medicamento.id == id).first()

    if not medicamento:
        print("Medicamento no encontrado")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Medicamento no econtrado"
        )

    return parsear_medicamento(medicamento)


def obtener_medicamento_isbn_db(isbn: str) -> MedicamentoOut:
    medicamento = (
        db.session.query(Medicamento).where(Medicamento.codigo_isbn == isbn).first()
    )

    if not medicamento:
        print("Medicamento no encontrado")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Medicamento no econtrado"
        )

    return parsear_medicamento(medicamento)


def obtener_medicamento_nombre_db(nombre: str) -> MedicamentoOut:
    medicamento = (
        db.session.query(Medicamento).where(Medicamento.nombre == nombre).first()
    )

    if not medicamento:
        print("Medicamento no encontrado")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Medicamento no econtrado"
        )

    return parsear_medicamento(medicamento)


def crear_medicamento_db(nuevo_medicamento: MedicamentoIn) -> MedicamentoOut:
    medicamento = Medicamento(
        nombre=nuevo_medicamento.nombre,
        codigo_isbn=nuevo_medicamento.codigo_isbn,
        dosis_disponibles=nuevo_medicamento.dosis_disponibles,
        id_sucursal=nuevo_medicamento.id_sucursal,
    )

    try:
        db.session.add(medicamento)
        db.session.commit()
        return parsear_medicamento(medicamento)
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado el medicamento",
        )


def actualizar_dosis_medicamento_id_db(
    id: str, dosis_entregadas: int
) -> MedicamentoOut:
    medicamento = db.session.query(Medicamento).where(Medicamento.id == id).first()
    medicamento.dosis_disponibles -= dosis_entregadas

    try:
        db.session.commit()
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha actualizado el stock del medicamento",
        )

    return obtener_medicamento_id_db(id)


def parsear_medicamento(medicamento: Medicamento) -> MedicamentoOut:
    return MedicamentoOut(
        id=medicamento.id,
        nombre=medicamento.nombre,
        codigo_isbn=medicamento.codigo_isbn,
        dosis_disponibles=medicamento.dosis_disponibles,
        id_sucursal=medicamento.id_sucursal,
    )
