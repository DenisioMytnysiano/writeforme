from typing import Protocol

from app.hexagon.domain.rhyming_scheme import RhymingScheme


class ModelServiceProtocol(Protocol):

    def generate(rhyming: RhymingScheme, poem_prompt: str) -> str:
        pass