from fastapi import APIRouter

router = APIRouter()


@router.post("/generate")
def generate_poem():
    pass
