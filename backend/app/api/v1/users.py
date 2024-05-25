from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.v1 import deps
from app.crud import read, create, base
from app.models.token import Token
from app.schemas import UserRead, UserCreate
from app.utils.jwt import create_access_token

router = APIRouter()


@router.post("/", response_model=UserRead)
async def create_user(
        user: UserCreate
):
    print(user)
    db_user = await read.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await create.create_user(user=user)


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(deps.get_db)
):
    user = await read.get_user_by_email(db, email=form_data.username)
    if not user or not base.BaseCrud().verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
