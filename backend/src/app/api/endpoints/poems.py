from fastapi import APIRouter


router = APIRouter()

@router.get("/:id")
def get_poem(id: str):
    pass

@router.get("/mine")
def get_my_poems():
    pass

@router.delete("/:id")
def delete_poem():
    pass