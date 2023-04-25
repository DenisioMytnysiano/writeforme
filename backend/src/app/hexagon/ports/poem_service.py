from typing import Collection, NoReturn, Protocol

from app.hexagon.domain.poem import Poem


class PoemServiceProtocol(Protocol):
    def get_all_poems(self, page: int, items_per_page: int) -> Collection[Poem]:
        pass

    def get_all_poems(
        self, created_by: str, page: int, items_per_page: int
    ) -> Collection[Poem]:
        pass

    def get_poem(self, id: str) -> Poem:
        pass

    def delete_poem(self, id: str) -> NoReturn:
        pass
