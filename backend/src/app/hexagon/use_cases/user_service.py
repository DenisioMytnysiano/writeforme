from typing import NoReturn, Optional

from hexagon.domain.user import User
from hexagon.ports.user_service import UserServiceProtocol


class UserService(UserServiceProtocol):
    def add_user(self, user: User) -> NoReturn:
        pass

    def get_user_by_email(self, email: str) -> Optional[User]:
        pass
