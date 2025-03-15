from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.modules.auth.dtos.login_dto import LoginDTO
from app.modules.auth.dtos.register_dto import RegisterDTO
from app.modules.auth.service.user_service import UserService
from app.modules.auth.repository.user_repository import UserRepository
from app.modules.student.repository.student_repository import StudentRepository
from app.database.db import get_session as get_db
from datetime import timedelta
from app.modules.auth.service.token_service import TokenService

router = APIRouter()

@router.post("/register")
def register_user(register_dto: RegisterDTO, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db), StudentRepository(db))
    try:
        user = user_service.register_user(register_dto)
        return {"message": "Usuario cadastrado com sucesso!!", "user": user}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.post("/login")
def login_user(login_dto: LoginDTO, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db), StudentRepository(db))
    user = user_service.login_user(login_dto)
    if user:
        access_token_expires = timedelta(minutes=TokenService.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = TokenService.create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Email invalido ou senha invalida")