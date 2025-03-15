from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Student(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    curso: str
    matricula: str
    nome: str
    user: Optional["User"] = Relationship(back_populates="student")