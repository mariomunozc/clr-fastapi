# app/api/Gtrack/routes.py

from fastapi import APIRouter, HTTPException, status, Depends
from app.api.gtrack.services import gtrack_service
from app.core.security import basic_auth

router = APIRouter()

@router.get("/get_token/{endpoint}", status_code=status.HTTP_200_OK, tags=["GTrack"])
async def get_gtrack_token(endpoint: str, authenticated: bool = Depends(basic_auth)):
    try:
        token = gtrack_service.obtener_token(endpoint)
        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
