from fastapi import APIRouter, Depends
from sqlmodel import Session

from modules.laboratory.service.laboratory_service import LaboratoryService
from modules.laboratory.repository.laboratory_repository import LaboratoryRepository
from database.db import get_session as get_db
from modules.llm.service.llm_service import ask_llm
from modules.llm.dtos.text_input_dto import TextInputDTO
from modules.professor.repository.professor_repository import ProfessorRepository
from modules.professor.service.professor_service import ProfessorService

router = APIRouter()

@router.post("/ask-llm")
def recommend_laboratories(text: TextInputDTO, db: Session = Depends(get_db)):
    recommendations = ask_llm(
        text,
        LaboratoryService(
            LaboratoryRepository(db)
        ),
        ProfessorService(
            ProfessorRepository(db)
        )
    )
    return {"recommendations": recommendations}