from typing import Optional
from sqlmodel import Field, Relationship, SQLModel

class ResearcherModel(SQLModel, table=True):
    __tablename__ = "tb_researcher"
    researcher_id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(index=True)
    laboratory_id: Optional[int] = Field(default=None, foreign_key="tb_laboratory.laboratory_id")

    laboratory: Optional["LaboratoryModel"] = Relationship(back_populates="researcher")