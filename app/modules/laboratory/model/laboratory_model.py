from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

class LaboratoryModel(SQLModel, table=True):
    laboratory_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    professors: List["ProfessorModel"] = Relationship(back_populates="laboratory")