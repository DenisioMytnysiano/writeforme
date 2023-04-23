from hexagon.domain.rhyming_scheme import RhymingScheme
from pydantic import BaseModel


class PoemResponse(BaseModel):
    title: str
    created_by: str
    text: str
    rhyming_scheme: RhymingScheme
