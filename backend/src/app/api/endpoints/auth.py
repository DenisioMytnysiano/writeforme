from api.schemas.auth import LoginRequest, RefreshTokenRequest, RegisterRequest, TokenResponse
from fastapi import APIRouter, Depends, Response
from infrastructure.auth.auth_service import AuthService, AuthServiceProtocol
from infrastructure.auth.auth_token_pair import AuthTokenPair
from infrastructure.auth.oauth_bearer_cookie import jwtRefreshTokenBearer

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
def login(response: Response, user: LoginRequest, auth_service=Depends(AuthService)):
    token_pair = auth_service.login(user.email, user.password, user.fingerprint)
    response.set_cookie(
        key="refresh_token",
        value=f"Bearer {token_pair.refresh_token}",
        path="/auth",
        httponly=True,
    )
    return token_pair


@router.post("/register")
def register(
    user: RegisterRequest, auth_service: AuthServiceProtocol = Depends(AuthService)
):
    return auth_service.register(user.name, user.email, user.password)


@router.post("/refresh-token", response_model=TokenResponse)
def refresh_tokens(
    response: Response,
    refresh_request: RefreshTokenRequest,
    refresh_token: str = Depends(jwtRefreshTokenBearer),
    auth_service: AuthServiceProtocol = Depends(AuthService),
):
    token_pair = auth_service.refresh_token(refresh_token, refresh_request.fingerprint)
    response.set_cookie(
        key="refresh_token",
        value=f"Bearer {token_pair.refresh_token}",
        path="/auth",
        httponly=True,
    )
    return token_pair


@router.post("/logout")
def logout(
    tokens: AuthTokenPair = Depends(jwtRefreshTokenBearer),
    auth_service: AuthServiceProtocol = Depends(AuthService),
):
    return auth_service.logout(tokens)
