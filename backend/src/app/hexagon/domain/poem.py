from dataclasses import dataclass
from uuid import UUID


@dataclass
class Poem:
    id: UUID
    title: str
    created_by: UUID
    text: str
