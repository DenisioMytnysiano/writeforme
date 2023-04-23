from uuid import UUID

from api.schemas.common import PaginationParams
from api.schemas.poems import PoemResponse
from fastapi import APIRouter, Depends
from infrastructure.auth.auth_token_pair import AuthTokenPair
from infrastructure.auth.oauth_bearer_cookie import jwtTokenBearer

router = APIRouter()


@router.get("/:id", response_model=PoemResponse)
def get_poem(id: UUID):
    pass


@router.get("/", response_model=list[PoemResponse])
def get_poems(paging: PaginationParams = Depends()):
    pass


@router.get("/mine", response_model=list[PoemResponse])
def get_my_poems(
    paging: PaginationParams = Depends(),
    tokens: AuthTokenPair = Depends(jwtTokenBearer),
):
    pass


@router.delete("/:id")
def delete_poem(id: UUID, tokens: AuthTokenPair = Depends(jwtTokenBearer)):
    pass
