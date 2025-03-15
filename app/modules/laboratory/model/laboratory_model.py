from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

class LaboratoryModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    descricao: str
    professores: List["Professor"] = Relationship(back_populates="laboratory")