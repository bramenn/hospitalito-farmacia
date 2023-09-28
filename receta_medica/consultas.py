from .modelo import RecetaMedica, RecetaMedicaIn, RecetaMedicaOut
from fastapi import status
from fastapi.exceptions import HTTPException
import db

from medicamentos.modelo import MedicamentoOut
from medicamentos.consultas import (
    obtener_medicamento_nombre_db,
    obtener_medicamento_id_db,
    actualizar_dosis_medicamento_id_db,
)
from sucursal.modelo import SucursalOut
from sucursal.consultas import obtener_sucursal_id_db


def obtener_receta_medica_id_db(id: str) -> RecetaMedicaOut:
    receta_medica = db.session.query(RecetaMedica).where(RecetaMedica.id == id).first()

    medicamento = obtener_medicamento_id_db(receta_medica.id_medicamento)
    sucursal = obtener_sucursal_id_db(receta_medica.id_sucursal)

    if not receta_medica:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="RecetaMedica no encontrado"
        )

    return parsear_receta_medica(receta_medica, medicamento, sucursal)


def crear_receta_medica_db(nuevo_receta_medica: RecetaMedicaIn) -> RecetaMedicaOut:
    medicamento = obtener_medicamento_nombre_db(nuevo_receta_medica.medicamento)
    sucursal = obtener_sucursal_id_db(nuevo_receta_medica.id_sucursal)

    receta_medica = RecetaMedica(
        cedula_paciente=nuevo_receta_medica.cedula_paciente,
        nombre_paciente=nuevo_receta_medica.nombre_paciente,
        cedula_medico=nuevo_receta_medica.cedula_medico,
        nombre_medico=nuevo_receta_medica.nombre_medico,
        hospital=nuevo_receta_medica.hospital,
        dosis=nuevo_receta_medica.dosis,
        frecuencia=nuevo_receta_medica.frecuencia,
        id_sucursal=nuevo_receta_medica.id_sucursal,
        id_medicamento=medicamento.id,
    )

    try:
        db.session.add(receta_medica)
        db.session.commit()
        return parsear_receta_medica(
            receta_medica, medicamento=medicamento, sucursal=sucursal
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado la receta medica",
        )


def entregar_receta_medica_cc_db(cc: str) -> RecetaMedicaOut:
    receta_medica = (
        db.session.query(RecetaMedica)
        .where(RecetaMedica.cedula_paciente == cc and RecetaMedica.entregado == False)
        .first()
    )

    if not receta_medica:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="RecetaMedica no encontrado"
        )

    actualizar_dosis_medicamento_id_db(
        receta_medica.id_medicamento, int(receta_medica.dosis)
    )

    return obtener_receta_medica_id_db(receta_medica.id)


def parsear_receta_medica(
    receta_medica: RecetaMedica, medicamento: MedicamentoOut, sucursal: SucursalOut
) -> RecetaMedicaOut:
    return RecetaMedicaOut(
        id=receta_medica.id,
        cedula_paciente=receta_medica.cedula_paciente,
        nombre_paciente=receta_medica.nombre_paciente,
        cedula_medico=receta_medica.cedula_medico,
        nombre_medico=receta_medica.nombre_medico,
        hospital=receta_medica.hospital,
        date_received=receta_medica.date_received,
        dosis=receta_medica.dosis,
        frecuencia=receta_medica.frecuencia,
        medicamento=medicamento,
        sucursal=sucursal,
        entregado=receta_medica.entregado,
    )
