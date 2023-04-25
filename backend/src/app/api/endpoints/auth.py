from api.schemas.auth import LoginRequest, RegisterRequest, TokenResponse
from fastapi import APIRouter, Depends
from infrastructure.auth.auth_service import AuthService, AuthServiceProtocol
from infrastructure.auth.auth_token_pair import AuthTokenPair
from infrastructure.auth.oauth_bearer_cookie import jwtTokenBearer

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
def login(user: LoginRequest, auth_service=Depends(AuthService)):
    return auth_service.login(user.email, user.password)


@router.post("/register")
def register(
    user: RegisterRequest, auth_service: AuthServiceProtocol = Depends(AuthService)
):
    return auth_service.register(user.email, user.password)


@router.post("/refresh-token", response_model=TokenResponse)
def refresh_token(
    tokens: AuthTokenPair = Depends(jwtTokenBearer),
    auth_service: AuthServiceProtocol = Depends(AuthService),
):
    return auth_service.refresh_token(tokens)


@router.post("/logout")
def logout(
    tokens: AuthTokenPair = Depends(jwtTokenBearer),
    auth_service: AuthServiceProtocol = Depends(AuthService),
):
    return auth_service.logout(tokens)
