# app/api/Gtrack/routes.py

from fastapi import APIRouter, HTTPException, status
from app.api.gtrack.services import gtrack_service

router = APIRouter()

@router.get("/get_token/{endpoint}", status_code=status.HTTP_200_OK, tags=["GTrack"])
async def get_gtrack_token(endpoint: str):
    try:
        token = gtrack_service.obtener_token(endpoint)
        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
