from pydantic import BaseModel, Field
from typing import Literal

TargetStatus = Literal["Not Started", "In Progress", "Completed"]


class TargetCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=24)
    country: str = Field(..., min_length=1, max_length=24)


class TargetUpdateNotes(BaseModel):
    notes: str = Field(..., min_length=0, max_length=100)  # Дозволяємо пустий рядок


class TargetUpdateStatus(BaseModel):
    status: TargetStatus


class TargetResponse(TargetCreate):
    id: int
    notes: str
    mission_id: int
    status: TargetStatus = "Not Started"

    class Config:
        from_attributes = True
