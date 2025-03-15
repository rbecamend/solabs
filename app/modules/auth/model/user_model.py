from sqlmodel import SQLModel, Field, Relationship
from typing import Optional



class UserModel(SQLModel, table=True):
    user_id: int = Field(default=None, primary_key=True)
    email: str
    password: str
    student_id: Optional[int] = Field(default=None, foreign_key="studentmodel.student_id", unique=True)
    student: Optional["StudentModel"] = Relationship(back_populates="user")