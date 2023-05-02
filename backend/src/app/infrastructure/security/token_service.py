from datetime import datetime, timedelta
from typing import Optional, Protocol

from infrastructure.auth.auth_token_pair import AuthTokenPair
from infrastructure.config import config
from jose import JWTError, jwt


class TokenServiceProtocol(Protocol):
    def generate(self, payload: dict, exp: Optional[int]) -> str:
        pass

    def verify(self, token: str) -> bool:
        pass

    def payload(self, token: str) -> dict:
        pass


class TokenService:
    def generate(self, payload: dict, exp: Optional[int]) -> str:
        to_encode = payload.copy()
        expire = datetime.utcnow() + timedelta(minutes=exp)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode,
            config.JWT_SETTINGS.SECRET_KEY,
            algorithm=config.JWT_SETTINGS.JWT_ALGORITHM,
        )
        return encoded_jwt

    def verify(self, token: str) -> bool:
        try:
            jwt.decode(
                token, config.JWT_SETTINGS.SECRET_KEY, config.JWT_SETTINGS.JWT_ALGORITHM
            )
            return True
        except JWTError:
            return False

    def payload(self, token: str) -> str:
        return jwt.decode(token, config.JWT_SETTINGS.SECRET_KEY, config.JWT_SETTINGS.JWT_ALGORITHM)
