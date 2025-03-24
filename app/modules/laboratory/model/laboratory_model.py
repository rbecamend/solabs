from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

class LaboratoryModel(SQLModel, table=True):
    __tablename__ = "tb_laboratory"
    laboratory_id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str = Field()

    researcher: List["ResearcherModel"] = Relationship(back_populates="laboratory")
