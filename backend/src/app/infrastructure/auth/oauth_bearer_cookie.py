from typing import Dict, Optional

from fastapi import Depends, HTTPException, Request, status
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security import OAuth2
from fastapi.security.utils import get_authorization_scheme_param
from infrastructure.security.token_service import TokenService


class OAuth2PasswordBearerWithCookie(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(
        self, request: Request, tokenService: TokenService = Depends(TokenService)
    ) -> str:
        refresh_token = self.get_refresh_token_from_cookie(request)
        tokenService.verify(refresh_token)
        return refresh_token

    def get_refresh_token_from_cookie(self, request: Request):
        authorization: str = request.cookies.get("refresh_token")
        scheme, refresh_token = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return refresh_token


jwtRefreshTokenBearer = OAuth2PasswordBearerWithCookie(tokenUrl="/auth/login")
