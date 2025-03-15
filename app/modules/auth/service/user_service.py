
import bcrypt
from app.modules.auth.model.user_model import UserModel
from app.modules.auth.repository.user_repository import UserRepository
from app.modules.student.repository.student_repository import StudentRepository
from app.modules.auth.dtos.register_dto import RegisterDTO
from app.modules.auth.dtos.login_dto import LoginDTO



class UserService:

    def __init__(self, user_repository: UserRepository, student_repository: StudentRepository):
        self.user_repository = user_repository
        self.student_repository = student_repository

    def register_user(self, register_dto: RegisterDTO):

        student = self.student_repository.get_student_by_registration(register_dto.registration)
        if not student:
            raise Exception("Estudante não encontrado")
        hashed_password =  bcrypt.hashpw(register_dto.password.encode('utf-8'), bcrypt.gensalt())
        user = UserModel(
            email=register_dto.email,
            password=hashed_password,
            student=student
        )
        return self.user_repository.create_user(user)

    def login_user(self, login_dto: LoginDTO):
        user = self.user_repository.get_user_by_email(login_dto.email)
        if user and bcrypt.checkpw(login_dto.senha.encode('utf-8'), user.senha.encode('utf-8')):
            return user
        return None



