from fastapi import APIRouter
from app.modules.auth.controller.auth_controller import router as auth_router
from app.modules.deepseek.controller.recommendation_controller import router as lab_recommendation

router = APIRouter()
router.include_router(auth_router, prefix="/auth")
router.include_router(lab_recommendation, prefix="/lab_recommendation")