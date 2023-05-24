from typing import Collection, NoReturn, Optional
from uuid import UUID

from fastapi import Depends
from sqlalchemy.orm import Session

from hexagon.domain.poem import Poem
from infrastructure.db.models.poem import Poem as PoemDB
from infrastructure.db.session import get_db


class PoemRepository:
    def __init__(self, db_session: Session = Depends(get_db)) -> None:
        super().__init__()
        self.__db_session = db_session

    def get_all_poems(self, page: int, items_per_page: int) -> Collection[Poem]:
        poems = (
            self.__db_session.query(PoemDB)
            .offset((page - 1) * items_per_page)
            .limit(items_per_page)
            .all()
        )
        return [
            Poem(poem_db.id, poem_db.title, poem_db.created_by, poem_db.text)
            for poem_db in poems
        ]

    def get_all_poems_by_user(
        self, created_by: str, page: int, items_per_page: int
    ) -> Collection[Poem]:
        poems = (
            self.__db_session.query(PoemDB)
            .where(PoemDB.created_by == created_by)
            .offset((page - 1) * items_per_page)
            .limit(items_per_page)
            .all()
        )

        return [
            Poem(poem_db.id, poem_db.title, poem_db.created_by, poem_db.text)
            for poem_db in poems
        ]

    def get_poem(self, id: UUID) -> Optional[Poem]:
        poem = self.__db_session.query(PoemDB).where(PoemDB.id == id).first()
        if poem:
            return Poem(poem.id, poem.title, poem.created_by, poem.text)
        return None

    def add_poem(self, poem: Poem) -> NoReturn:
        poem = PoemDB(
            id=poem.id, title=poem.title, text=poem.text, created_by=poem.created_by
        )
        self.__db_session.add(poem)
        self.__db_session.commit()

    def delete_poem(self, id: str) -> NoReturn:
        poem = self.__db_session.query(PoemDB).where(PoemDB.id == id)
        poem.delete()
        self.__db_session.commit()
