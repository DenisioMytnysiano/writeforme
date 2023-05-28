from typing import Collection, NoReturn, Optional

from fastapi import Depends
from hexagon.domain.poem import Poem
from hexagon.ports.poem_repository import PoemRepositoryProtocol
from infrastructure.repositories.poem_repository import PoemRepository


class PoemService:
    def __init__(
        self, poem_repository: PoemRepositoryProtocol = Depends(PoemRepository)
    ):
        self.__poem_repository = poem_repository

    def get_all_poems(self, page: int, items_per_page: int) -> Collection[Poem]:
        return self.__poem_repository.get_all_poems(page, items_per_page)

    def get_all_poems_by_user(
        self, created_by: str, page: int, items_per_page: int
    ) -> Collection[Poem]:
        return self.__poem_repository.get_all_poems_by_user(
            created_by, page, items_per_page
        )

    def get_poem(self, identifier: str) -> Optional[Poem]:
        return self.__poem_repository.get_poem(identifier)

    def add_poem(self, poem: Poem) -> NoReturn:
        self.__poem_repository.add_poem(poem)

    def delete_poem(self, identifier: str) -> NoReturn:
        return self.__poem_repository.delete_poem(identifier)
