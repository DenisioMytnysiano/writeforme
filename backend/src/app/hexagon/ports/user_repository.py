from typing import NoReturn, Optional, Protocol
from uuid import UUID

from hexagon.domain.user import User


class UserRepositoryProtocol(Protocol):
    def add_user(self, user: User) -> NoReturn:
        pass

    def get_user_by_email(self, email: str) -> Optional[User]:
        pass

    def get_user_by_id(self, id: UUID) -> Optional[User]:
        pass
