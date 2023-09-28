from sqlalchemy import Column, Integer, String, DateTime, Boolean
import datetime
import db
from pydantic import BaseModel
from sqlalchemy.sql.schema import ForeignKey

from sucursal.modelo import SucursalOut
from medicamentos.modelo import MedicamentoOut, Medicamento


class RecetaMedica(db.Base):

    __tablename__ = "receta_medica"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    cedula_paciente = Column("cedula_paciente", String(255))
    nombre_paciente = Column("nombre_paciente", String(255))
    cedula_medico = Column("cedula_medico", String(255))
    nombre_medico = Column("nombre_medico", String(255))
    hospital = Column("hospital", String(255))
    date_received = Column(DateTime, default=datetime.datetime.utcnow)
    dosis = Column("dosis", String(255))
    frecuencia = Column("frecuencia", String(255))
    entregado = Column(Boolean, unique=False, default=False)

    id_medicamento = Column(Integer, ForeignKey("medicamento.id"))
    id_sucursal = Column(Integer, ForeignKey("medicamento.id"))


class RecetaMedicaIn(BaseModel):
    cedula_paciente: str
    nombre_paciente: str
    cedula_medico: str
    nombre_medico: str
    hospital: str
    dosis: str
    frecuencia: str
    medicamento: str
    id_sucursal: int


class RecetaMedicaOut(BaseModel):
    id: int
    cedula_paciente: str
    nombre_paciente: str
    cedula_medico: str
    nombre_medico: str
    hospital: str
    date_received: datetime.datetime
    dosis: str
    frecuencia: str
    entregado: bool
    medicamento: MedicamentoOut
    sucursal: SucursalOut
