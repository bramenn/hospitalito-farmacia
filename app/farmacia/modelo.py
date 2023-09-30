from sqlalchemy import Column, Integer, String
from .. import db
from pydantic import BaseModel


class Farmacia(db.Base):
    __tablename__ = "farmacia"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    nombre = Column("nombre", String(255), unique=True)


class FarmaciaIn(BaseModel):
    nombre: str


class FarmaciaOut(BaseModel):
    id: int
    nombre: str
