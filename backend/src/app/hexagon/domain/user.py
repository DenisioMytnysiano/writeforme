from dataclasses import dataclass
from uuid import UUID


@dataclass
class User:
    id: UUID
    name: str
    email: str
    hashed_pasword: str
