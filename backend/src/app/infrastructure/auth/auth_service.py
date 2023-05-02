from datetime import datetime
from typing import NoReturn, Protocol

from fastapi import Depends
from hexagon.domain.user import User
from hexagon.ports.user_service import UserServiceProtocol
from hexagon.use_cases.user_service import UserService
from infrastructure.db.models.refresh_session import RefreshSession
from infrastructure.auth.refresh_session_store import RefreshSessionStore
from infrastructure.auth.refresh_session_store import RefreshSessionStoreProtocol
from infrastructure.auth.auth_token_pair import AuthTokenPair
from infrastructure.config import config
from infrastructure.security.hasher import Hasher
from infrastructure.security.token_service import TokenService, TokenServiceProtocol


class AuthServiceProtocol(Protocol):
    def register(self, email: str, password: str) -> NoReturn:
        pass

    def login(self, email: str, password: str, fingerprint: str) -> AuthTokenPair:
        pass

    def refresh_token(self, tokens: AuthTokenPair, fingerprint: str) -> AuthTokenPair:
        pass

    def logout(self, tokens: AuthTokenPair) -> NoReturn:
        pass


class AuthService:
    def __init__(
        self,
        user_repository: UserServiceProtocol = Depends(UserService),
        hasher: Hasher = Depends(Hasher),
        token_service: TokenServiceProtocol = Depends(TokenService),
        refresh_session_store: RefreshSessionStoreProtocol = Depends(
            RefreshSessionStore)
    ) -> None:
        super().__init__()
        self.__user_repository = user_repository
        self.__hasher = hasher
        self.__token_service = token_service
        self.__refresh_session_store = refresh_session_store

    def register(self, email: str, password: str) -> NoReturn:
        is_registered = self.__user_repository.get_user_by_email(email)
        if is_registered:
            raise Exception("User already registered with email.")
        hashed_password = self.__hasher.hash(password)
        self.__user_repository.add_user(
            User(email=email, name="test", hashed_password=hashed_password)
        )

    def login(self, email: str, password: str, fingerprint: str) -> AuthTokenPair:
        user = self.__user_repository.get_user_by_email(email)
        if not user:
            raise Exception("User is not registered with email.")
        self.__hasher.verify(password, user.hashed_password)
        access_token = self.__token_service.generate(
            {"sub": email}, int(
                config.JWT_SETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        refresh_token = self.__token_service.generate(
            {"sub": email}, int(
                config.JWT_SETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        self.__refresh_session_store.add_session(session=RefreshSession(email=email, refresh_token=refresh_token, fingerprint=fingerprint))
        return AuthTokenPair(access_token, refresh_token)

    def refresh_token(self, tokens: AuthTokenPair, fingerprint: str) -> AuthTokenPair:
        session = self.__refresh_session_store.delete_and_get_session(
            tokens.refresh_token)
        if not session or session.fingerprint != fingerprint:
            raise Exception("Session not found")
        email = self.__token_service.payload(tokens.access_token)["sub"]
        access_token = self.__token_service.generate( {"sub": email}, int(config.JWT_SETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES))
        refresh_token = self.__token_service.generate({"sub": email}, int(config.JWT_SETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES))
        self.__refresh_session_store.add_session(session=RefreshSession(email=email, refresh_token=refresh_token, fingerprint=fingerprint))
        return AuthTokenPair(access_token, refresh_token)

    def logout(self, tokens: AuthTokenPair) -> NoReturn:
        session = self.__refresh_session_store.delete_and_get_session(tokens.refresh_token)
        if not session:
            raise Exception("Session not found")
