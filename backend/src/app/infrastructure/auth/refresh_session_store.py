from typing import NoReturn, Optional, Protocol

from fastapi import Depends
from infrastructure.db.models.refresh_session import RefreshSession
from infrastructure.db.session import get_db
from sqlalchemy.orm import Session


class RefreshSessionStoreProtocol(Protocol):
    def add_session(self, session: RefreshSession) -> NoReturn:
        pass

    def get_session_for_user(
        self, email: str, fingerprint: str
    ) -> Optional[RefreshSession]:
        pass

    def delete_and_get_session(self, refresh_token: str) -> Optional[RefreshSession]:
        pass


class RefreshSessionStore:
    def __init__(self, db_session: Session = Depends(get_db)) -> None:
        super().__init__()
        self.__db_session = db_session

    def add_session(self, session: RefreshSession) -> NoReturn:
        self.__db_session.add(session)
        self.__db_session.commit()

    def get_session_for_user(
        self, email: str, fingerprint: str
    ) -> Optional[RefreshSession]:
        return (
            self.__db_session.query(RefreshSession)
            .where(
                RefreshSession.email == email
                and RefreshSession.fingerprint == fingerprint
            )
            .first()
        )

    def delete_and_get_session(self, refresh_token: str) -> Optional[RefreshSession]:
        session = (
            self.__db_session.query(RefreshSession)
            .where(RefreshSession.refresh_token == refresh_token)
            .first()
        )

        self.__db_session.delete(session)
        self.__db_session.commit()
        return session
