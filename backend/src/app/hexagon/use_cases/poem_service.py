from typing import Collection, NoReturn, Optional

from fastapi import Depends
from hexagon.domain.poem import Poem
from hexagon.ports.poem_repository import PoemRepositoryProtocol
from hexagon.use_cases.poem_service import PoemServiceProtocol
from infrastructure.repositories.poem_repository import PoemRepository


class PoemService(PoemServiceProtocol):
    def __init__(
        self, poem_repository: PoemRepositoryProtocol = Depends(PoemRepository)
    ):
        super.__init__()
        self.__poem_repository = poem_repository

    def get_all_poems(self, page: int, items_per_page: int) -> Collection[Poem]:
        return self.__poem_repository.get_all_poems(page, items_per_page)

    def get_all_poems(
        self, created_by: str, page: int, items_per_page: int
    ) -> Collection[Poem]:
        return self.__poem_repository.get_all_poems(created_by, page, items_per_page)

    def get_poem(self, id: str) -> Optional[Poem]:
        return self.__poem_repository.get_poem(id)

    def delete_poem(self, id: str) -> NoReturn:
        return self.__poem_repository.delete_poem(id)
