from api.schemas.auth import LoginRequest, RegisterRequest, TokenResponse
from fastapi import APIRouter

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
def login(user: LoginRequest):
    pass


@router.post("/register")
def register(user: RegisterRequest):
    pass


@router.post("/refresh-token", response_model=TokenResponse)
def refresh_token():
    pass


@router.post("/logout")
def logout():
    pass
