from fastapi import HTTPException, Depends
from typing import List
from app.api.posts.models import Post as PostModel  # Importa el modelo de datos necesario
from app.core.database import get_db  # Importa la instancia de base de datos (ejemplo ficticio)
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Annotated

db_dependency = Annotated[Session, Depends(get_db)]

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int


class PostService:
    
    async def create_post(self, post: PostBase, db: db_dependency) -> PostModel:
        db_post = PostModel(**post.model_dump())
        db.add(db_post)
        db.commit()
        return post.model_dump()
    
    async def read_post(self, post_id: int, db: db_dependency) -> PostModel:
        post = db.query(PostModel).filter(PostModel.id == post_id).first()
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        return post
    
    async def read_posts(self, db: db_dependency) -> List[PostModel]:
        posts = db.query(PostModel).all()
        return posts

    async def delete_post(self, post_id: int, db: db_dependency) -> PostModel:
        post = db.query(PostModel).filter(PostModel.id == post_id).first()
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        db.delete(post)
        db.commit()
        return post
    
    async def update_post(self, post_id: int, post: PostBase, db: db_dependency) -> PostModel:
        db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
        if db_post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        db_post.title = post.title
        db_post.content = post.content
        db_post.user_id = post.user_id
        db.commit()
        return post.model_dump()


# Instancia del servicio para ser utilizada en los routers
post_service = PostService
