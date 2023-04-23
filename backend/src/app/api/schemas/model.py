from uuid import UUID

from hexagon.domain.rhyming_scheme import RhymingScheme
from pydantic import BaseModel


class GeneratePoemRequest(BaseModel):
    rhyming_scheme: RhymingScheme
    text_prompt: str


class GeneratePoemResponse(BaseModel):
    poem_id: UUID
    poem: str
