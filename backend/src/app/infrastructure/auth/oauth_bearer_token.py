from typing import Dict, Optional

from fastapi import Depends, HTTPException, Request, status
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security import OAuth2
from fastapi.security.utils import get_authorization_scheme_param
from infrastructure.security.token_service import TokenService


class OAuth2PasswordBearerWithToken(OAuth2):
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
        access_token = self.get_access_token_from_header(request)
        tokenService.verify(access_token)
        return access_token

    def get_access_token_from_header(self, request: Request):
        authorization: str = request.headers.get("Authorization")
        scheme, access_token = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return access_token


jwtTokenBearer = OAuth2PasswordBearerWithToken(tokenUrl="/auth/login")
