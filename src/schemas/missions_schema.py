from pydantic import BaseModel, Field
from typing import Optional

from src.schemas.targets_schema import TargetCreate, TargetResponse


class MissionCreate(BaseModel):
    targets: list[TargetCreate] = Field(..., min_length=1, max_length=3)


class MissionAssignCat(BaseModel):
    cat_id: int = Field(..., gt=0, description="ID кота, який призначається на місію.")


class MissionResponse(BaseModel):
    id: int
    cat_id: Optional[int] = None

    is_complete: bool = False
    targets: list[TargetResponse]

    class Config:
        from_attributes = True
