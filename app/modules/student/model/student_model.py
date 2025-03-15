from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class StudentModel(SQLModel, table=True):
    __tablename__ = "tb_student"
    student_id: int = Field(default=None, primary_key=True)
    degree: str
    registration: str
    name: str
    user: Optional["UserModel"] = Relationship(back_populates="student")