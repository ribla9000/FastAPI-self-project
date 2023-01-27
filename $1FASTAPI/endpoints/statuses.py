from fastapi import APIRouter, Depends
from endpoints.depends import get_status_repository
from repositories.statuses import StatusRepository
from core.response import read_log
from models.statuses import StatusCreate

router = APIRouter()


@router.post("/")
async def create_status(status: StatusCreate, status_repository: StatusRepository = Depends(get_status_repository)):
    result = await status_repository.create(new_status=status)
    return read_log(result)
