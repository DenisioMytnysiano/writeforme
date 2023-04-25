from typing import NoReturn, Protocol

from fastapi import Depends
from infrastructure.db.models.user import User
from infrastructure.security.hasher import Hasher
from infrastructure.security.token_service import TokenService, TokenServiceProtocol
from infrastructure.auth.auth_token_pair import AuthTokenPair
from infrastructure.repositories.user_repository import UserRepository, UserRepositoryProtocol
from infrastructure.config import config

class AuthServiceProtocol(Protocol):

    def register(self, email: str, password: str) -> NoReturn:
        pass

    def login(self, email: str, password: str) -> AuthTokenPair:
        pass

    def refresh_token(self, tokens: AuthTokenPair) -> AuthTokenPair:
        pass

    def logout(self, tokens: AuthTokenPair) -> NoReturn:
        pass

class AuthService:

    def __init__(self, 
                 user_repository: UserRepositoryProtocol = Depends(UserRepository),
                 hasher: Hasher = Depends(Hasher),
                 token_service: TokenServiceProtocol = Depends(TokenService)) -> None:
        super().__init__()
        self.__user_repository = user_repository
        self.__hasher = hasher
        self.__token_service = token_service

    def register(self, email: str, password: str) -> NoReturn:
        is_registered = self.__user_repository.get_user_by_email(email)
        if is_registered:
            raise Exception("User already registered with email.")
        hashed_password = self.__hasher.hash(password)
        self.__user_repository.add_user(User(email=email, name="test", hashed_password=hashed_password))

    def login(self, email: str, password: str) -> AuthTokenPair:
        user = self.__user_repository.get_user_by_email(email)
        if not user:
            raise Exception("User is not registered with email.")
        self.__hasher.verify(password, user.hashed_password)
        access_token = self.__token_service.generate({"sub": email}, int(config.JWT_SETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES))
        refresh_token = self.__token_service.generate({"sub": email}, int(config.JWT_SETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES))
        return AuthTokenPair(access_token, refresh_token)

    def refresh_token(self, tokens: AuthTokenPair) -> AuthTokenPair:
        pass

    def logout(self, tokens: AuthTokenPair) -> NoReturn:
        pass