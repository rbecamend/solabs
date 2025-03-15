from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.modules.auth.dtos.login_dto import LoginDTO
from app.modules.auth.dtos.register_dto import RegisterDTO
from app.modules.auth.service.user_service import UserService
from app.modules.auth.repository.user_repository import UserRepository
from app.modules.student.repository.student_repository import StudentRepository
from app.database.db import get_session as get_db

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
        return {"message": "Login successful", "user": user}
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")