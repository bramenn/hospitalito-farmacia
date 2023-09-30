from fastapi import FastAPI
import uvicorn

from .receta_medica import endpoint as receta_medica_endpoint
from .sucursal import endpoint as sucursal_endpoint
from .farmacia import endpoint as farmacia_endpoint
from .medicamentos import endpoint as medicamentos_endpoint

from .db import Base, conn

app = FastAPI()


app.include_router(
    receta_medica_endpoint.router, prefix="/v1/receta_medica", tags=["receta_medica"]
)
app.include_router(sucursal_endpoint.router, prefix="/v1/sucursal", tags=["sucursal"])
app.include_router(farmacia_endpoint.router, prefix="/v1/farmacia", tags=["farmacia"])

app.include_router(
    medicamentos_endpoint.router, prefix="/v1/medicamento", tags=["medicamento"]
)

if __name__ == "__main__":
    Base.metadata.create_all(conn)

    uvicorn.run(app="main:app", reload=True, port=8001)
