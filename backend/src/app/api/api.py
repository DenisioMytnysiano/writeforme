from api.endpoints import auth, model, poems, user
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(model.router, prefix="/model", tags=["model"])
api_router.include_router(poems.router, prefix="/poems", tags=["poems"])
api_router.include_router(user.router, prefix="/users", tags=["users"])