from typing import List
from core.response import read_log
from fastapi import APIRouter, Depends
from models.users import User
from models.models import UserModel, UserModelInput
from .depends import get_model_repository, get_current_user
from repositories.models import ModelRepository


router = APIRouter()


@router.get("/")
async def read_models(limit: int = 100,
                      skip: int = 0,
                      models: ModelRepository = Depends(get_model_repository)):
    result = await models.get_all(limit=limit, skip=skip)
    return read_log(result)


@router.post("/")
async def create_models(user_models: UserModelInput, models: ModelRepository = Depends(get_model_repository),
                        current_user: User = Depends(get_current_user)):
    result = await models.create(user_id=current_user.id, mod=user_models)
    return read_log(result)


@router.delete("/")
async def delete_models(id: int, models: ModelRepository = Depends(get_model_repository),
                        current_user: User = Depends(get_current_user)):
    model = await models.get_by_id(id=id)
    result = await models.delete(id=id)
    if model is None or model.user_id != int(current_user.id):
        return {"error": "404 Not found", "status": False, "payload": result}
    return read_log(result)