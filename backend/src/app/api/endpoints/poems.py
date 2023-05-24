import uuid
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from api.deps import get_authorized_user
from api.schemas.common import PaginationParams
from api.schemas.poems import PoemResponse, PoemSaveRequest
from hexagon.domain.poem import Poem
from hexagon.domain.user import User
from hexagon.ports.poem_service import PoemServiceProtocol
from hexagon.use_cases.poem_service import PoemService

router = APIRouter()


@router.get("/mine", response_model=List[PoemResponse])
def get_my_poems(
    paging: PaginationParams = Depends(),
    user: User = Depends(get_authorized_user),
    poem_service: PoemServiceProtocol = Depends(PoemService),
):
    return poem_service.get_all_poems_by_user(user.id, paging.page, paging.count)


@router.get("/{identifier}", response_model=PoemResponse)
def get_poem(
    identifier: UUID, poem_service: PoemServiceProtocol = Depends(PoemService)
):
    poem = poem_service.get_poem(identifier)
    if not poem:
        raise HTTPException(status_code=404)
    return poem


@router.get("/", response_model=List[PoemResponse])
def get_poems(
    paging: PaginationParams = Depends(),
    poem_service: PoemServiceProtocol = Depends(PoemService),
):
    return poem_service.get_all_poems(paging.page, paging.count)


@router.post("/save", response_model=PoemResponse)
def save_poem(
    poem_request: PoemSaveRequest,
    user: User = Depends(get_authorized_user),
    poem_service: PoemServiceProtocol = Depends(PoemService),
):
    poem = Poem(
        id=uuid.uuid4(),
        created_by=user.id,
        title=poem_request.title,
        text=poem_request.text,
    )
    poem_service.add_poem(poem)
    return poem


@router.delete("/{identifier}")
def delete_poem(
    identifier: UUID,
    user: User = Depends(get_authorized_user),
    poem_service: PoemServiceProtocol = Depends(PoemService),
):
    poem = poem_service.get_poem(identifier)
    if poem and poem.created_by == user.id:
        poem_service.delete_poem(identifier)
    else:
        raise HTTPException(status_code=403)
