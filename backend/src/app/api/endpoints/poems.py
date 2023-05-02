from uuid import UUID
import uuid
from api.deps import get_authorized_user

from api.schemas.common import PaginationParams
from api.schemas.poems import PoemResponse, PoemSaveRequest
from fastapi import APIRouter, Depends, HTTPException
from hexagon.domain.poem import Poem
from hexagon.domain.user import User
from hexagon.ports.poem_service import PoemServiceProtocol
from hexagon.ports.user_service import UserServiceProtocol
from hexagon.use_cases.poem_service import PoemService
from hexagon.use_cases.user_service import UserService

router = APIRouter()

@router.get("/mine", response_model=list[PoemResponse])
def get_my_poems(paging: PaginationParams = Depends(), user: User = Depends(get_authorized_user), poem_service: PoemServiceProtocol = Depends(PoemService)):
    return poem_service.get_all_poems_by_user(user.id, paging.page, paging.count)

@router.get("/{id}", response_model=PoemResponse)
def get_poem(id: UUID, poem_service: PoemServiceProtocol = Depends(PoemService), user_service: UserServiceProtocol = Depends(UserService)):
    poem = poem_service.get_poem(id)
    if not poem:
        raise HTTPException(status_code=404)
    return poem

@router.get("/", response_model=list[PoemResponse])
def get_poems(paging: PaginationParams = Depends(), poem_service: PoemServiceProtocol = Depends(PoemService)):
    return poem_service.get_all_poems(paging.page, paging.count)

@router.post("/save", response_model=PoemResponse)
def save_poem(poem_request: PoemSaveRequest, user: User = Depends(get_authorized_user), poem_service: PoemServiceProtocol = Depends(PoemService)):
    poem = Poem(id= uuid.uuid4(), created_by=user.id, title=poem_request.title, text=poem_request.text)
    poem_service.add_poem(poem)
    return poem

@router.delete("/{id}")
def delete_poem(id: UUID, user: User = Depends(get_authorized_user), poem_service: PoemServiceProtocol = Depends(PoemService)):
    poem = poem_service.get_poem(id)
    if poem and poem.created_by == user.id:
        poem_service.delete_poem(id)
    else:
        raise HTTPException(status_code=403)

