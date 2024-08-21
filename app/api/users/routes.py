from fastapi import APIRouter, Depends, status
from typing import Annotated, List
import app.api.users.models as UserModel
from app.core.database import engine, get_db
from sqlalchemy.orm import Session
from app.api.users.services import UserBase, user_service

router = APIRouter()

UserModel.Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/user/", status_code=status.HTTP_201_CREATED, tags=["User"], response_model=UserBase)
async def create_user(user: UserBase, db: db_dependency):
    user_created = await user_service.create_user(user_service, user, db)
    return user_created

@router.get("/user/{user_id}", status_code=status.HTTP_200_OK, tags=["User"], response_model=UserBase)
async def read_user(user_id: int, db: db_dependency):
    user = await user_service.read_user(user_service, user_id, db)
    return user

@router.get("/users", status_code=status.HTTP_200_OK, tags=["User"])
async def read_users(db: db_dependency):
    users = await user_service.read_users(user_service, db)
    return users

@router.delete("/user/{user_id}", status_code=status.HTTP_200_OK, tags=["User"], response_model=UserBase)
async def delete_user(user_id: int, db: db_dependency):
    user = await user_service.delete_user(user_service, user_id, db)
    return user

@router.put("/user/{user_id}", status_code=status.HTTP_200_OK, tags=["User"], response_model=UserBase)
async def update_user(user_id: int, user: UserBase, db: db_dependency):
    user_updated = await user_service.update_user(user_service, user_id, user, db)
    return user_updated

