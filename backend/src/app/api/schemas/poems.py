from uuid import UUID
from hexagon.domain.rhyming_scheme import RhymingScheme
from pydantic import BaseModel
from uuid import UUID


class PoemResponse(BaseModel):
    id: UUID
    title: str
    created_by: UUID
    text: str

class PoemSaveRequest(BaseModel):
    title: str
    text: str

