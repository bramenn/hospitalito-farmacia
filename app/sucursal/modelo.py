from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from .. import db
from ..farmacia.modelo import Farmacia
from ..medicamentos.modelo import Medicamento


class Sucursal(db.Base):
    __tablename__ = "sucursal"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    nombre = Column("nombre", String(255))
    ubicacion = Column("ubicacion", String(255))
    telefono = Column("telefono", String(255))
    id_farmacia = Column(Integer, ForeignKey("farmacia.id"))

    medicamentos = relationship(Medicamento)


class SucursalIn(BaseModel):
    nombre: str
    ubicacion: str
    telefono: str
    id_farmacia: int


class SucursalOut(BaseModel):
    id: int
    nombre: str
    ubicacion: str
    telefono: str
    id_farmacia: int
