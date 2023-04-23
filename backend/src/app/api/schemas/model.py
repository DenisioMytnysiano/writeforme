from uuid import UUID
from pydantic import BaseModel
from hexagon.domain.rhyming_scheme import RhymingScheme


class GeneratePoemRequest(BaseModel):
    rhyming_scheme: RhymingScheme
    text_prompt: str

class GeneratePoemResponse(BaseModel):
    poem_id: UUID
    poem: str
    