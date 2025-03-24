import bcrypt
from modules.auth.model.user_model import UserModel
from modules.auth.repository.user_repository import UserRepository
from modules.student.repository.student_repository import StudentRepository
from modules.auth.dtos.register_dto import RegisterDTO
from modules.auth.dtos.login_dto import LoginDTO

class InvalidFieldException(Exception):
    pass

class UserAlreadyExistsException(Exception):
    pass

class StudentNotFoundException(Exception):
    pass

class UserNotFoundException(Exception):
    pass

class InvalidCredentialsException(Exception):
    pass

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
        for field_name, value in vars(login_dto).items():
            #if not isinstance(value, str):
                #raise InvalidFieldException(f"O campo '{field_name}' deve ser uma string.")
            if value.strip() == "":
                raise InvalidFieldException(f"O campo '{field_name}' não pode estar em branco ou conter apenas espaços.")
        if not user:
            raise UserNotFoundException(f"Usuário com email '{login_dto.email}' não encontrado.")
        if not bcrypt.checkpw(login_dto.password.encode('utf-8'), user.password.encode('utf-8')):
            raise InvalidCredentialsException("Senha incorreta.")

        return user

    def validate_create_user(self,register_dto: RegisterDTO):
        allowed_domains = ["@gmail.com", "@hotmail.com", "@icen.ufpa.br", "@outlook.com", "@yahoo.com"]

        for field_name, value in vars(register_dto).items():
            #if not isinstance(value, str):
                #raise InvalidFieldException(f"O campo '{field_name}' deve ser uma string.")
            if value.strip() == "":
                raise InvalidFieldException(f"O campo '{field_name}' não pode estar em branco ou conter apenas espaços.")

        if not any(register_dto.email.endswith(domain) for domain in allowed_domains):
            raise InvalidFieldException("O email deve ser válido (ex: @gmail.com, @hotmail.com, @icen.ufpa.br, e @yahoo.com).")

        if self.user_repository.exists_by_registration(register_dto.registration):
            raise UserAlreadyExistsException(f"Já existe um usuario com matricula {register_dto.registration}")

        if self.user_repository.exists_by_email(register_dto.email):
            raise UserAlreadyExistsException(f"Já existe um usuario com email {register_dto.email}")

        if not self.student_repository.get_student_by_registration(register_dto.registration):
            raise StudentNotFoundException(f"Estudante com matricula {register_dto.registration} não encontrado")
