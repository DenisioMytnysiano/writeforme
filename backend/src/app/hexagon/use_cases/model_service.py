from app.hexagon.domain.rhyming_scheme import RhymingScheme
from app.hexagon.ports.model_service import ModelServiceProtocol

class ModelService(ModelServiceProtocol):

    def generate(rhyming: RhymingScheme, poem_prompt: str) -> str:
        pass