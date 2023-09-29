from sqlalchemy import Column, Integer, String
import db
from sqlalchemy.sql.schema import ForeignKey
from pydantic import BaseModel


class Medicamento(db.Base):
    __tablename__ = "medicamento"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    nombre = Column("nombre", String(255))
    codigo_isbn = Column("codigo_isbn", String(255))
    dosis_disponibles = Column("espcialidad", Integer)
    id_sucursal = Column(Integer, ForeignKey("sucursal.id"))


class MedicamentoIn(BaseModel):
    nombre: str
    codigo_isbn: str
    dosis_disponibles: int
    id_sucursal: int


class MedicamentoOut(BaseModel):
    id: int
    nombre: str
    codigo_isbn: str
    dosis_disponibles: int
    id_sucursal: int
