from fastapi import APIRouter
from modules.auth.controller.auth_controller import router as auth_router
from modules.llm.controller.llm_controller import  router as llm_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth")
router.include_router(llm_router, prefix="/lab_recommendation")