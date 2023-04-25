from typing import NoReturn, Optional, Protocol

from fastapi import Depends
from infrastructure.db.session import get_db
from infrastructure.db.models import User as UserDB
from hexagon.domain.user import User
from sqlalchemy.orm import Session

class UserRepositoryProtocol(Protocol):

    def add_user(self, user: UserDB) -> NoReturn:
        pass

    def get_user_by_email(self, email: str) -> Optional[UserDB]:
        pass

class UserRepository:

    def __init__(self, db_session: Session = Depends(get_db)) -> None:
        super().__init__()
        self.__db_session = db_session

    def add_user(self, user: UserDB) -> NoReturn:
        self.__db_session.add(user)
        self.__db_session.commit()

    def get_user_by_email(self, email: str) -> Optional[UserDB]:
        return self.__db_session \
                   .query(UserDB) \
                   .where(UserDB.email == email) \
                   .first()