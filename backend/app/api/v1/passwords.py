from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, crud
from app.api.v1 import deps
from app.crud import create, read
from app.schemas import PasswordRead, PasswordCreate

router = APIRouter()


@router.post("/", response_model=PasswordRead)
async def create_password(
        password: PasswordCreate, db: AsyncSession = Depends(deps.get_db)
):
    return await create.create_password(db=db, password=password)


@router.get("/", response_model=list[PasswordRead])
async def read_passwords(
        master_password: str = Body(...), db: AsyncSession = Depends(deps.get_db), user_id: int = 1
):
    db_passwords = await read.get_passwords(db=db, user_id=user_id)
    for password in db_passwords:
        password.encrypted_password = password.decrypt_password(master_password)
    return db_passwords
