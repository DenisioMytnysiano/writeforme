from pydantic import BaseModel

from hexagon.domain.rhyming_scheme import RhymingScheme


class PoemResponse(BaseModel):
    title: str
    created_by: str
    text: str
    rhyming_scheme: RhymingScheme