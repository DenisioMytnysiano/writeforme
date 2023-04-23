from fastapi import APIRouter, Depends

from api.schemas.model import GeneratePoemRequest, GeneratePoemResponse

router = APIRouter()


@router.get("/generate", response_model=GeneratePoemResponse)
def generate_poem(generate_params: GeneratePoemRequest = Depends()):
    pass
