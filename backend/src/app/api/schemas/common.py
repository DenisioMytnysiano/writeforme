from pydantic import BaseModel, NonNegativeInt


class PaginationParams(BaseModel):
    page: NonNegativeInt
    count: NonNegativeInt