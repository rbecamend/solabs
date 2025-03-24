from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from modules.auth.dtos.login_dto import LoginDTO
from modules.auth.dtos.register_dto import RegisterDTO
from modules.auth.service.user_service import UserService, InvalidFieldException, UserAlreadyExistsException, \
    StudentNotFoundException, UserNotFoundException, InvalidCredentialsException
from modules.auth.repository.user_repository import UserRepository
from modules.student.repository.student_repository import StudentRepository
from database.db import get_session as get_db
from datetime import timedelta
from modules.auth.service.token_service import TokenService

router = APIRouter()

@router.post("/register", tags=["User"])
def register_user(register_dto: RegisterDTO, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db), StudentRepository(db))
    try:
        user = user_service.register_user(register_dto)
        return {"message": "Usuario cadastrado com sucesso!!", "user": user}
    except (InvalidFieldException, UserAlreadyExistsException, StudentNotFoundException) as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Erro inesperado ao registrar usuário.")


@router.post("/login", tags=["User"])
def login_user(login_dto: LoginDTO, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db), StudentRepository(db))
    try:
        user = user_service.login_user(login_dto)
        access_token_expires = timedelta(minutes=TokenService.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = TokenService.create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except (InvalidFieldException, UserNotFoundException, InvalidCredentialsException) as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro inesperado ao fazer login.")