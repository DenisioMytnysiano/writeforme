from typing import Collection, NoReturn, Protocol
from app.hexagon.domain.poem import Poem

class PoemRepositoryProtocol(Protocol):

    def get_all_poems(page: int, items_per_page: int) -> Collection[Poem]:
        pass

    def get_all_poems(created_by: str, page: int, items_per_page: int) -> Collection[Poem]:
        pass

    def get_poem(id: str) -> Poem:
        pass

    def delete_poem(id: str) -> NoReturn:
        pass