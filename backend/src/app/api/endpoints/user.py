from uuid import UUID
from fastapi import APIRouter, Depends
from api.schemas.user import UserInfo
from hexagon.ports.user_service import UserServiceProtocol
from hexagon.use_cases.user_service import UserService

router = APIRouter()


@router.get("/{identifier}", response_model=UserInfo)
def get_user(
    identifier: UUID, user_repository: UserServiceProtocol = Depends(UserService)
):
    return user_repository.get_user_by_id(identifier)


@router.get("/by-email/{email}", response_model=UserInfo)
def get_user_by_email(
    email: str, user_repository: UserServiceProtocol = Depends(UserService)
):
    return user_repository.get_user_by_email(email)
