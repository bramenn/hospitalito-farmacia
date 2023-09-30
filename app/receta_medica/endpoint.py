import json
from fastapi import APIRouter, Request
from .consultas import (
    crear_receta_medica_db,
    obtener_receta_medica_id_db,
    entregar_receta_medica_cc_db,
)

from ..aws_client import enviar_evento_generar_pdf

from .modelo import RecetaMedicaIn, RecetaMedicaOut

router = APIRouter()


@router.get("/{id}", response_model=RecetaMedicaOut)
def obtener_receta_medica(id: str):
    receta_medica = obtener_receta_medica_id_db(id)
    return receta_medica


@router.post("/")
async def crear_receta_medica(request: Request):
    sns_request: dict = json.loads(await request.body())

    if sns_request.get("Type") == "SubscriptionConfirmation":
        print(
            "Debes aceptar la subcripción de la sns por: ",
            sns_request.get("SubscribeURL"),
        )
        return
    elif sns_request.get("Type") == "Notification":
        try:
            nuevo_receta_medica: dict = json.loads(sns_request.get("Message"))
            nuevo_receta_medica = RecetaMedicaIn(**nuevo_receta_medica)
        except Exception as e:
            print("Receta no cumple con el formato esperado:", e)
            return

    return crear_receta_medica_db(nuevo_receta_medica)


@router.put("/{cc}", response_model=RecetaMedicaOut)
def entregar_receta_medica(cc: str):
    
    receta_medica = entregar_receta_medica_cc_db(cc)

    try:
        enviar_evento_generar_pdf(receta_medica.model_dump(mode="json"))
    except Exception as e:
        print("Error enviando evento para generar PDF: ", e)

    return receta_medica
