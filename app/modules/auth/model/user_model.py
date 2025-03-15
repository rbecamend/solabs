from sqlmodel import SQLModel, Field, Relationship
from typing import Optional



class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str
    senha: str
    student_id: Optional[int] = Field(default=None, foreign_key="student.id", unique=True)
    student: Optional["Student"] = Relationship(back_populates="user")