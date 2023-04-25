from typing import Collection, NoReturn, Optional, Protocol

from app.hexagon.domain.poem import Poem


class PoemRepositoryProtocol(Protocol):
    def get_all_poems(self, page: int, items_per_page: int) -> Collection[Poem]:
        pass

    def get_all_poems(
        self, created_by: str, page: int, items_per_page: int
    ) -> Collection[Poem]:
        pass

    def get_poem(self, id: str) -> Optional[Poem]:
        pass

    def delete_poem(self, id: str) -> NoReturn:
        pass
