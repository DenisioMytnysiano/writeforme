from typing import NoReturn, Collection
from app.hexagon.domain.poem import Poem
from app.hexagon.use_cases.poem_service import PoemServiceProtocol


class PoemService(PoemServiceProtocol):
    
    def get_all_poems(page: int, items_per_page: int) -> Collection[Poem]:
        pass

    def get_all_poems(created_by: str, page: int, items_per_page: int) -> Collection[Poem]:
        pass

    def get_poem(id: str) -> Poem:
        pass

    def delete_poem(id: str) -> NoReturn:
        pass


