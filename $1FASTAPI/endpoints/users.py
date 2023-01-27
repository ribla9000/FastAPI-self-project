from fastapi import APIRouter, Depends
from typing import List
from repositories.users import UserRepository
from .depends import get_user_repository, get_current_user
from pydantic import constr
from core.response import read_log
from models.users import User, UserRegister

router = APIRouter()


@router.get("/")
async def read_users(users: UserRepository = Depends(get_user_repository),
                     limit: int = 100, skip: int = 0) -> List[User]:
    result = await users.get_all(limit=limit, skip=skip)
    return read_log(result)


@router.post("/",)
async def create_user(user: UserRegister, users: UserRepository = Depends(get_user_repository)):
    result = await users.create(u=user)
    return read_log(result)


@router.put("/update_name")
async def update_name(name: str,
                      user: UserRepository = Depends(get_user_repository),
                      update: User = Depends(get_current_user)):
    result = await user.update_name(id=int(update.id), new_name=name, current_user=update)
    return read_log(result)


@router.put("/update_password")
async def update_password(new_password: constr(min_length=8),
                          password_accepted,
                          user: UserRepository = Depends(get_user_repository),
                          update: User = Depends(get_current_user)):
    result = await user.update_password(id=int(update.id), new_password=new_password, password_accepted=password_accepted)
    return read_log(result)
