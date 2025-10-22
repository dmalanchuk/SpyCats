from pydantic import BaseModel, Field
from typing import Optional


class CatCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    years_of_experience: int = Field(..., ge=0)
    breed: str = Field(min_length=1, max_length=50)
    salary: int


class CatUpdate(BaseModel):
    salary: int


class CatResponse(CatCreate):
    id: int
    mission_id: Optional[int] = None

    class Config:
        from_attributes = True
