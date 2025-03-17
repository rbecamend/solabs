
import bcrypt
from modules.auth.model.user_model import UserModel
from modules.auth.repository.user_repository import UserRepository
from modules.student.repository.student_repository import StudentRepository
from modules.auth.dtos.register_dto import RegisterDTO
from modules.auth.dtos.login_dto import LoginDTO

class UserService:

    def __init__(self, user_repository: UserRepository, student_repository: StudentRepository):
        self.user_repository = user_repository
        self.student_repository = student_repository

    def register_user(self, register_dto: RegisterDTO):

        self.validate_create_user(register_dto)
        student = self.student_repository.get_student_by_registration(register_dto.registration)
        hashed_password = bcrypt.hashpw(register_dto.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = UserModel(
            email=register_dto.email,
            password=hashed_password,
            student=student
        )
        return self.user_repository.create_user(user)

    def login_user(self, login_dto: LoginDTO):
        user = self.user_repository.get_user_by_email(login_dto.email)
        if user and bcrypt.checkpw(login_dto.password.encode('utf-8'), user.password.encode('utf-8')):
            return user
        return None


    def validate_create_user(self,register_dto: RegisterDTO):

        # if self.user_repository.exists_by_registration(register_dto.registration):
        #     raise Exception(f"Já existe um usuario com matricula {register_dto.registration}")

        if self.user_repository.exists_by_email(register_dto.email):
            raise Exception(f"Já existe um usuario com email {register_dto.email}")

        if not self.student_repository.get_student_by_registration(register_dto.registration):
            raise Exception(f"Estudante com matricula {register_dto.registration} não encontrado")


