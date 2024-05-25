from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.v1 import deps
from app.crud import create
from app.schemas import ServiceRead, ServiceCreate

router = APIRouter()


@router.post("/", response_model=ServiceRead)
async def create_service(
        service: ServiceCreate, db: AsyncSession = Depends(deps.get_db)
):
    return await create.create_service(db=db, service=service)
