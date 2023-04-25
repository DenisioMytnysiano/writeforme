from typing import NoReturn, Optional

from fastapi import Depends
from hexagon.domain.user import User
from infrastructure.db.models import User as UserDB
from infrastructure.db.session import get_db
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, db_session: Session = Depends(get_db)) -> None:
        super().__init__()
        self.__db_session = db_session

    def add_user(self, user: User) -> NoReturn:
        self.__db_session.add(user)
        self.__db_session.commit()

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.__db_session.query(UserDB).where(UserDB.email == email).first()
