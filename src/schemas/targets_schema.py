from pydantic import BaseModel
from src.schemas.complected_schema import Completed, InProgress, NotStarted


class TargetsSchema(BaseModel):
    name: str
    country: str
    notes: str
    completed: NotStarted | InProgress | Completed