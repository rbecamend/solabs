from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.modules.deepseek.dto.text_input_dto import TextInputDTO
from app.modules.laboratory.service.laboratory_service import LaboratoryService
from app.modules.laboratory.repository.laboratory_repository import LaboratoryRepository
from app.database.db import get_session as get_db


from  app.modules.deepseek.service.deepseek_service import DeepSeekService
router = APIRouter()

@router.post("/recommendations")
def recommend_laboratories(data: TextInputDTO, db: Session = Depends(get_db)):
    recommendations = DeepSeekService(LaboratoryService(LaboratoryRepository(db))).get_lab_recommendations(data.text)
    return {"recommendations": recommendations}