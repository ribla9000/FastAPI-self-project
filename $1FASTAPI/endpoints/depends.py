from fastapi import Depends, HTTPException, status
from repositories.users import UserRepository
from repositories.models import ModelRepository
from repositories.statuses import StatusRepository
from models.users import User
from core.security import JWTBearer, decode_access_token
from db.base import database


def get_status_repository() -> StatusRepository:
    return StatusRepository(database)


def get_user_repository() -> UserRepository:
    return UserRepository(database)


def get_model_repository() -> ModelRepository:
    return ModelRepository(database)


async def get_current_user(
        users: UserRepository = Depends(get_user_repository),
        token: str = Depends(JWTBearer()),) -> User:
    credential_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Credential exception')
    payload = decode_access_token(token)
    if payload is None:
        raise credential_exception

    email: str = payload.get("sub")
    if email is None:
        raise credential_exception

    user = await users.get_by_email(email=email)
    if user is None:
        return credential_exception

    return user