from pydantic import BaseModel, EmailStr, validator, constr
from typing import Optional
import datetime


class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    hashed_password: str
    created_at: datetime.datetime


class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)
    password_accepted: str

    @validator('password_accepted')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values["password"]:
            raise ValueError('passwords don\'t match')
        return v
