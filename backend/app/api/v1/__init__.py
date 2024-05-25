from fastapi import APIRouter
from app.api.v1 import users, services, passwords

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(services.router, prefix="/services", tags=["services"])
api_router.include_router(passwords.router, prefix="/passwords", tags=["passwords"])
