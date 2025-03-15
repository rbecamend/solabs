from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from app.modules.laboratory.model.laboratory_model import LaboratoryModel

class ProfessorModel(SQLModel, table=True):
    __tablename__ = "tb_professor"
    professor_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    laboratory_id: Optional[int] = Field(default=None, foreign_key="tb_laboratory.laboratory_id")
    laboratory: Optional["LaboratoryModel"] = Relationship(back_populates="professors")