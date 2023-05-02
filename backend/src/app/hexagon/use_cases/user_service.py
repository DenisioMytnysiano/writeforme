from typing import NoReturn, Optional
from uuid import UUID

from fastapi import Depends

from hexagon.domain.user import User
from hexagon.ports.user_repository import UserRepositoryProtocol
from infrastructure.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, user_repository: UserRepositoryProtocol = Depends(UserRepository)) -> None:
        super().__init__()
        self.__user_repository = user_repository

    def add_user(self, user: User) -> NoReturn:
        self.__user_repository.add_user(user)

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.__user_repository.get_user_by_email(email)
        
    def get_user_by_id(self, id: UUID) -> Optional[User]:
        return self.__user_repository.get_user_by_id(id)