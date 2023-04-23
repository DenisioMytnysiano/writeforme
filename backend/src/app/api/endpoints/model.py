from api.schemas.model import GeneratePoemRequest, GeneratePoemResponse
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/generate", response_model=GeneratePoemResponse)
def generate_poem(generate_params: GeneratePoemRequest = Depends()):
    pass
