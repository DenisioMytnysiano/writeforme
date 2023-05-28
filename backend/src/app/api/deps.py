from fastapi import Depends, HTTPException
from hexagon.domain.user import User
from hexagon.ports.user_service import UserServiceProtocol
from hexagon.use_cases.user_service import UserService
from infrastructure.auth.oauth_bearer_token import jwtTokenBearer
from infrastructure.security.token_service import TokenService, TokenServiceProtocol


def get_authorized_user(
    access_token: str = Depends(jwtTokenBearer),
    token_service: TokenServiceProtocol = Depends(TokenService),
    user_service: UserServiceProtocol = Depends(UserService),
) -> User:
    if token_service.verify(access_token):
        email = token_service.payload(access_token)["sub"]
        return user_service.get_user_by_email(email)
    raise HTTPException(status_code=401)
