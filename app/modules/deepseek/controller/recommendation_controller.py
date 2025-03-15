from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.modules.laboratory.service.laboratory_service import LaboratoryService
from app.modules.laboratory.repository.laboratory_repository import LaboratoryRepository
from app.database.db import get_session as get_db

router = APIRouter()

@router.post("/recommendations")
def recommend_laboratories(preferences: str, db: Session = Depends(get_db)):
    laboratory_service = LaboratoryService(LaboratoryRepository(db))
    recommendations = laboratory_service.recommend_laboratories(preferences)
    return {"recommendations": recommendations}