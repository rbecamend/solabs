from http.client import HTTPException

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlmodel import Session

from database.db import get_session as get_db
from modules.auth.service.token_service import TokenService
from modules.laboratory.repository.laboratory_repository import LaboratoryRepository
from modules.laboratory.service.laboratory_service import LaboratoryService
from modules.llm.dtos.text_input_dto import TextInputDTO
from modules.llm.service.llm_service import ask_llm, InvalidTextException
from modules.researcher.repository.researcher_repository import ResearcherRepository
from modules.researcher.service.professor_service import ResearcherService

router = APIRouter()
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = TokenService.verify_token(token)
        return payload
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido.",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.post("/ask-llm", tags=["LLM"])
def recommend_laboratories(text: TextInputDTO, db: Session = Depends(get_db), token_data: str = Depends(verify_token)):
    try:
        recommendations = ask_llm(
            text,
            LaboratoryService(LaboratoryRepository(db)),
            ResearcherService(ResearcherRepository(db))
        )
        return {"recommendations": recommendations}
    except InvalidTextException as e:
        raise HTTPException(status_code=401, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao processar a recomendação.")