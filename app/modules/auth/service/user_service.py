
import bcrypt
from app.modules.auth.model.user_model import User
from app.modules.auth.repository.user_repository import UserRepository
from app.modules.student.repository.student_repository import StudentRepository
from app.modules.auth.dtos.register_dto import RegisterDTO
from app.modules.auth.dtos.login_dto import LoginDTO

from app.modules.student.model.student_model import Student


class UserService:

    def __init__(self, user_repository: UserRepository, student_repository: StudentRepository):
        self.user_repository = user_repository
        self.student_repository = student_repository

    def register_user(self, register_dto: RegisterDTO):

        if not self.student_repository.existy_by_matricula(register_dto.matricula):
            raise Exception(f"Não existe um estudante com matricula {register_dto.matricula} cadastrado no sistema")

        student = self.student_repository.create_student(
            Student(
                curso=register_dto.curso,
                matricula=register_dto.matricula,
                nome=register_dto.nome
            )
        )

        hashed_password =  bcrypt.hashpw(register_dto.senha.encode('utf-8'), bcrypt.gensalt())

        user = User(
            email=register_dto.email,
            senha=hashed_password,
            student_id=student.id
        )
        return self.user_repository.create_user(user)

    def login_user(self, login_dto: LoginDTO):
        user = self.user_repository.get_user_by_email(login_dto.email)
        if user and bcrypt.checkpw(login_dto.senha.encode('utf-8'), user.senha.encode('utf-8')):
            return user
        return None



