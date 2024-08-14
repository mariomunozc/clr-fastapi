from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from app.core.database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(150))
    content = Column(String(250))
    published = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
