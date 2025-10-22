from pydantic import BaseModel, Field
from typing import Optional

from src.schemas.targets_schema import TargetCreate, TargetResponse
from src.schemas.cats_schema import CatResponse


class MissionCreate(BaseModel):
    targets: list[TargetCreate] = Field(..., min_length=1, max_length=3)


class MissionAssignCat(BaseModel):
    cat_id: int = Field(..., gt=0, description="ID cats for executed mission")


class MissionResponse(BaseModel):
    id: int
    cat: Optional[CatResponse] = None

    is_complete: bool = False
    targets: list[TargetResponse]

    class Config:
        from_attributes = True
