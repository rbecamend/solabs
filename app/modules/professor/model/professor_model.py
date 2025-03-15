from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from app.modules.laboratory.model.laboratory_model import LaboratoryModel

class ProfessorModel(SQLModel, table=True):
    professor_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    laboratory_id: Optional[int] = Field(default=None, foreign_key="laboratorymodel.laboratory_id")
    laboratory: Optional[LaboratoryModel] = Relationship(back_populates="professors")