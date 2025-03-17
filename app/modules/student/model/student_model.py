from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

if TYPE_CHECKING:
    from app.modules.auth.model.user_model import UserModel

class StudentModel(SQLModel, table=True):
    __tablename__ = "tb_student"

    student_id: int = Field(default=None, primary_key=True)
    degree: str
    registration: str
    name: str

    user: Optional["UserModel"] = Relationship(back_populates="student")