from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

if TYPE_CHECKING:
    from app.modules.student.model.student_model import StudentModel


class UserModel(SQLModel, table=True):
    __tablename__ = "tb_user"

    user_id: int = Field(default=None, primary_key=True)
    email: str
    password: str
    student_id: Optional[int] = Field(default=None, foreign_key="tb_student.student_id", unique=True)

    student: Optional["StudentModel"] = Relationship(back_populates="user")