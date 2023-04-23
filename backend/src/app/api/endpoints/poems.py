from uuid import UUID
from fastapi import APIRouter, Depends

from api.schemas.common import PaginationParams
from api.schemas.poems import PoemResponse

router = APIRouter()


@router.get("/:id", response_model=PoemResponse)
def get_poem(id: UUID):
    pass

@router.get("/", response_model=list[PoemResponse])
def get_poems(paging: PaginationParams = Depends()):
    pass

@router.get("/mine", response_model=list[PoemResponse])
def get_my_poems(paging: PaginationParams = Depends()):
    pass

@router.delete("/:id")
def delete_poem(id: UUID):
    pass
