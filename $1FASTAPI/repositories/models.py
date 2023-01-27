from typing import List, Optional
from models.models import UserModel, UserModelInput
from .base import BaseRepository
from db.models import models
import datetime


class ModelRepository(BaseRepository):

    async def create(self, user_id: int, mod: UserModelInput) -> UserModel:
        model = UserModel(
            id=0,
            title=mod.title,
            user_id=user_id,
            created_at=datetime.datetime.utcnow(),
            )
        values = {**model.dict()}
        values.pop("id", None)
        query = models.insert().values(**values)
        model.id = await self.database.execute(query=query)

        return model

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[UserModel]:
        query = models.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query)


    async def delete(self, id: int):
        query = models.delete().where(models.c.id==id)
        return await self.database.execute(query)

    async def get_by_id(self, id: int) -> Optional[UserModel]:
        query = models.select().where(models.c.id==id)
        model = await self.database.fetch_one(query)
        if model is None:
            return None
        return UserModel.parse_obj(model)
