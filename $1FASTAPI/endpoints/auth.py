from fastapi import APIRouter, HTTPException, status, Depends
from models.token import Token, Login
from repositories.users import UserRepository
from core.security import verify_password, create_access_token
from core.response import read_log
from .depends import get_user_repository

router = APIRouter()


@router.post("/")
async def login(login: Login, users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_email(login.email)
    error_not_exist = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect email or password')
    token = Token(
        access_token=create_access_token({"sub": user.email}),
        token_type="Bearer",
        )
    if user is None or not verify_password(login.password, user.hashed_password):
        return {"error": error_not_exist, "status": False, "payload": []}

    return read_log(token)
