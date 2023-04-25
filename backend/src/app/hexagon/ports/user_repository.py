from typing import NoReturn, Optional, Protocol

from hexagon.domain.user import User


class UserRepositoryProtocol(Protocol):
    def add_user(self, user: User) -> NoReturn:
        pass

    def get_user_by_email(self, email: str) -> Optional[User]:
        pass
