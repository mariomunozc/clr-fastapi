from fastapi import HTTPException, Depends
from typing import List
from app.api.users.models import User as UserModel  # Importa el modelo de datos necesario
from app.core.database import get_db  # Importa la instancia de base de datos (ejemplo ficticio)
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Annotated, Optional
import random

db_dependency = Annotated[Session, Depends(get_db)]
class UserBase(BaseModel):
    id: Optional[int]
    fullName: str
    email: str
    department: Optional[str]
    status: str


class UserService:

    async def create_user(self, user: UserBase, db: db_dependency) -> UserModel:
        user.id = random.randint(1, 100)
        db_user = UserModel(**user.model_dump())
        db.add(db_user)
        db.commit()
        return user.model_dump()
    
    async def read_user(self, user_id: int, db: db_dependency) -> UserModel:
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
    async def read_users(self, db: db_dependency) -> List[UserModel]:
        users = db.query(UserModel).all()
        return users
    
    async def delete_user(self, user_id: int, db: db_dependency) -> UserModel:
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        db.delete(user)
        db.commit()
        return user

    async def update_user(self, user_id: int, user: UserBase, db: db_dependency) -> UserModel:
        db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        db_user.fullName = user.fullName
        db_user.email = user.email
        db_user.department = user.department
        db_user.status = user.status
        db.commit()
        return user.model_dump()


# Instancia del servicio para ser utilizada en los routers
user_service = UserService