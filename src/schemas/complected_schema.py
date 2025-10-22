from pydantic import BaseModel


class NotStarted(BaseModel):
    text: str = "Not started"


class InProgress(BaseModel):
    text: str = "In progress"


class Completed(BaseModel):
    text: str = "Completed"
