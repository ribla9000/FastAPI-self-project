from pydantic import BaseModel


class Status(BaseModel):
    id: int = None
    status_name: str
    bool: bool


class StatusCreate(BaseModel):
    status_name: str
    bool: bool
