from fastapi import APIRouter


router = APIRouter()

@router.post("/login")
def login():
    pass

@router.post("/register")
def register():
    pass

@router.post("/refresh-token")
def refresh_token():
    pass

