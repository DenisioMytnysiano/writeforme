from typing import Collection, NoReturn, Protocol

from hexagon.domain.poem import Poem


class PoemServiceProtocol(Protocol):
    def get_all_poems(self, page: int, items_per_page: int) -> Collection[Poem]:
        pass

    def get_all_poems_by_user(
        self, created_by: str, page: int, items_per_page: int
    ) -> Collection[Poem]:
        pass

    def get_poem(self, identifier: str) -> Poem:
        pass

    def add_poem(self, poem: Poem) -> NoReturn:
        pass

    def delete_poem(self, identifier: str) -> NoReturn:
        pass
