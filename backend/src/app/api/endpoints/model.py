from api.schemas.model import GeneratePoemRequest, GeneratePoemResponse
from fastapi import APIRouter, Depends
from infrastructure.auth.auth_token_pair import AuthTokenPair
from infrastructure.auth.oauth_bearer_cookie import jwtTokenBearer

router = APIRouter()


@router.get("/generate", response_model=GeneratePoemResponse)
def generate_poem(generate_params: GeneratePoemRequest = Depends(), tokens: AuthTokenPair = Depends(jwtTokenBearer)):
    pass
