from sqlmodel import Session, select
from app.modules.auth.model.user_model import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user: User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_user_by_id(self, user_id: int):
        return self.session.get(User, user_id)

    def get_user_by_email(self, email: str):
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()

    def update_user(self, user: User):
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