from pydantic import BaseModel
from src.schemas.complected_schema import Completed, InProgress, NotStarted
from src.schemas.targets_schema import TargetsSchema


class MissionSchema(BaseModel):
    cats_id: int
    targets: TargetsSchema
    completed: NotStarted | InProgress | Completed