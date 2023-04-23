from api.schemas.auth import RegisterRequest, TokenResponse
from fastapi import APIRouter, Depends
from api.schemas.auth import LoginRequest
from infrastructure.auth.auth_token_pair import AuthTokenPair
from infrastructure.auth.oauth_bearer_cookie import jwtTokenBearer


router = APIRouter()


@router.post("/login", response_model=TokenResponse)
def login(user: LoginRequest):
    pass


@router.post("/register")
def register(user: RegisterRequest):
    pass


@router.post("/refresh-token", response_model=TokenResponse)
def refresh_token(tokens: AuthTokenPair = Depends(jwtTokenBearer)):
    pass


@router.post("/logout")
def logout(tokens: AuthTokenPair = Depends(jwtTokenBearer)):
    pass
