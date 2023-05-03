from typing import NoReturn, Optional
from uuid import UUID

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
        db_user = UserDB(id=user.id, name=user.name, email=user.email, hashed_password=user.hashed_pasword)
        self.__db_session.add(db_user)
        self.__db_session.commit()

    def get_user_by_email(self, email: str) -> Optional[User]:
        user = self.__db_session.query(UserDB).where(UserDB.email == email).first()
        if user:
            return User(user.id, user.name, user.email, user.hashed_password)

    def get_user_by_id(self, id: UUID) -> Optional[User]:
        user = self.__db_session.query(UserDB).where(UserDB.id == id).first()
        if user:
            return User(user.id, user.name, user.email, user.hashed_password)