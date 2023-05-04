from api.deps import get_authorized_user
from api.schemas.model import GeneratePoemRequest, GeneratePoemResponse
from fastapi import APIRouter, Depends
from hexagon.domain.user import User
from hexagon.ports.model_service import ModelServiceProtocol
from hexagon.use_cases.model_service import ModelService

router = APIRouter()


@router.post("/generate", response_model=GeneratePoemResponse)
def generate_poem(
    generate_params: GeneratePoemRequest,
     user: User = Depends(get_authorized_user), model_service: ModelServiceProtocol = Depends(ModelService)
):
    poem = model_service.generate(generate_params.rhyming_scheme, generate_params.text_prompt)
    return GeneratePoemResponse(poem=poem)
