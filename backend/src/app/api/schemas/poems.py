from uuid import UUID

from pydantic import BaseModel


class PoemResponse(BaseModel):
    id: UUID
    title: str
    created_by: UUID
    text: str


class PoemSaveRequest(BaseModel):
    title: str
    text: str
