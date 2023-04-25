from typing import Collection, NoReturn
from uuid import UUID

from fastapi import Depends
from hexagon.domain.poem import Poem
from hexagon.ports.poem_repository import PoemRepositoryProtocol
from infrastructure.db.models.poem import Poem as PoemDB
from infrastructure.db.session import get_db
from sqlalchemy.orm import Session


class PoemRepository(PoemRepositoryProtocol):
    def __init__(self, db_session: Session = Depends(get_db)) -> None:
        super().__init__()
        self.__db_session = db_session

    def get_all_poems(self, page: int, items_per_page: int) -> Collection[Poem]:
        return self.__db_session.query(PoemDB).offset(page).limit(items_per_page).all()

    def get_all_poems(
        self, created_by: str, page: int, items_per_page: int
    ) -> Collection[Poem]:
        return (
            self.__db_session.query(PoemDB)
            .where(PoemDB.created_by == created_by)
            .offset(page)
            .limit(items_per_page)
            .all()
        )

    def get_poem(self, id: UUID) -> Optional[Poem]:
        return self.__db_session.query(PoemDB).where(PoemDB.id == id).first()

    def delete_poem(self, id: str) -> NoReturn:
        poem = self.__db_session.query(PoemDB).where(PoemDB.id == id)
        poem.delete()
        self.__db_session.commit()
