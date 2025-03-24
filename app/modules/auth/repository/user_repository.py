from typing import Type

from sqlmodel import Session, select
from modules.auth.model.user_model import UserModel
from modules.student.model.student_model import StudentModel


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user: UserModel):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_user_by_id(self, user_id: int)-> Type[UserModel] | None:
        return self.session.get(UserModel, user_id)

    def get_user_by_email(self, email: str)-> Type[UserModel] | None:
        statement = select(UserModel).where(UserModel.email == email)
        return self.session.exec(statement).first()

    def update_user(self, user: UserModel):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
        return user

    def exists_by_email(self, email: str)-> bool:
        statement = select(UserModel).where(UserModel.email == email)
        return self.session.exec(statement).first() is not None

    def exists_by_registration(self, registration: str)-> bool:
        statement = select(UserModel).join(StudentModel).where(StudentModel.registration == registration)
        return self.session.exec(statement).first() is not None