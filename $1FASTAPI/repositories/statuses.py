from .base import BaseRepository
from db.statuses import statuses
from models.statuses import Status, StatusCreate


class StatusRepository(BaseRepository):

    async def create(self, new_status: StatusCreate):
        status = Status(
                status_name=new_status.status_name,
                bool=new_status.bool,
                )

        values = {**status.dict()}
        values.pop("id", None)
        query = statuses.insert().values(**values)
        status.id = await self.database.execute(query)
        return status