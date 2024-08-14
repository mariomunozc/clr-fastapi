from sqlalchemy import Column, Integer, String
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullName = Column(String(150), unique=True)
    email= Column(String(150), unique=True)
    department= Column(String(150))
    status= Column(String(1))

