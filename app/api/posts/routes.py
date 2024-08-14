from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated, List
import app.api.posts.models as PostModel
from app.core.database import engine, connect_database
from sqlalchemy.orm import Session
from app.api.posts.services import PostBase, post_service
import requests
import base64

router = APIRouter()
security = HTTPBasic()

allowed_users = {
    "user1": "password1",
    "user2": "password2"
}


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    if username not in allowed_users:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"}
        )
    return username

PostModel.Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(connect_database)]

@router.post("/posts/", status_code=status.HTTP_201_CREATED, tags=["Post"], response_model=PostBase)
async def create_post(post: PostBase, db: db_dependency):
    post_created = await post_service.create_post(self= post_service, post= post, db=db)
    return post_created

@router.get("/post/{post_id}", status_code=status.HTTP_200_OK, tags=["Post"], response_model=PostBase)
async def read_post(post_id: int, db: db_dependency):
    post = await post_service.read_post(post_service, post_id, db)
    return post

@router.get("/posts", status_code=status.HTTP_200_OK, tags=["Post"], response_model=List[PostBase])
async def read_posts(db: db_dependency):
    posts = await post_service.read_posts(post_service, db)
    return posts

@router.delete("/post/{post_id}", status_code=status.HTTP_200_OK, tags=["Post"], response_model=PostBase)
async def delete_post(post_id: int, db: db_dependency):
    post = await post_service.delete_post(post_service, post_id, db)
    return post

@router.put("/post/{post_id}", status_code=status.HTTP_200_OK, tags=["Post"], response_model=PostBase)
async def update_post(post_id: int, post: PostBase, db: db_dependency):
    post_updated = await post_service.update_post(post_service, post_id, post, db)
    return post_updated

@router.get('/privatePost', status_code=status.HTTP_200_OK, tags=["Private Post"])
def private_post(username: str = Depends(get_current_username)):
    return [{"item": "Foo", "owner": username}, {"item": "Bar", "owner": username}]

@router.get("/api_data", status_code=status.HTTP_200_OK, tags=["API Data"])
async def get_api_data(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to fetch API data",
        )


@router.get("/protected_api", status_code=status.HTTP_200_OK, tags=["Protected API Basic Auth"])
async def get_protected_api_data(url: str, credentials: HTTPBasicCredentials = Depends(security)):
    headers = {
        "Authorization": f"Basic {base64.b64encode(f'{credentials.username}:{credentials.password}'.encode()).decode()}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to fetch protected API data",
        )
    


@router.get("/get_bearer_api_no_data", status_code=status.HTTP_200_OK, tags=["Bearer API"])
async def get_bearer_api_no_data(token: str):
    url = "https://api.example.com/data"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to fetch bearer API data",
        )


@router.post("/post_bearer_api_json_data", status_code=status.HTTP_200_OK, tags=["Bearer API"])
async def post_bearer_api_json_data(url: str, token: str, payload: dict):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to fetch bearer API data",
        )
    

@router.post("/post_bearer_api_form_data", status_code=status.HTTP_200_OK, tags=["Bearer API"])
async def post_bearer_api_form_data(url: str, token: str, fecha_1: str, fecha_2: str):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "fecha_1": fecha_1,
        "fecha_2": fecha_2
    }
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to fetch bearer API data",
        )


@router.get("/obtener_token_extra_costos", status_code=status.HTTP_200_OK, tags=["GTrack Extra Costo"])
async def obtener_token_extra_costos(url: str, credentials: HTTPBasicCredentials = Depends(security)):
    headers = {
        "Authorization": f"Basic {base64.b64encode(f'{credentials.username}:{credentials.password}'.encode()).decode()}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to fetch protected API data",
        )
    
@router.post("/obtener_extra_costos", status_code=status.HTTP_200_OK, tags=["GTrack Extra Costo"])
async def obtener_extra_costos(url: str, token: str, fecha_1: str, fecha_2: str):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "fecha_1": fecha_1,
        "fecha_2": fecha_2
    }
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to fetch bearer API data",
        )
