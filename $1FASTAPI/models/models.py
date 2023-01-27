from pydantic import BaseModel
import datetime


class UserModelBase(BaseModel):
    title: str


class UserModel(UserModelBase):
    id: int
    user_id: int
    created_at: datetime.datetime


class UserModelInput(UserModelBase):
    pass

