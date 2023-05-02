from typing import Protocol

from hexagon.domain.rhyming_scheme import RhymingScheme


class ModelServiceProtocol(Protocol):
    def generate(self, rhyming: RhymingScheme, poem_prompt: str) -> str:
        pass
