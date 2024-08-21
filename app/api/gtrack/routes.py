# app/api/Gtrack/routes.py

from fastapi import APIRouter, HTTPException, status, Depends
from app.api.gtrack.services import gtrack_service
from app.core.security import basic_auth
from app.api.gtrack.models import Os  # Asegúrate de importar tu modelo Os
from sqlalchemy.orm import Session
from app.core.database import get_db
import datetime

router = APIRouter()

VALID_ENDPOINTS = ["Consultar_ViajeID", "Crear_Requerimiento", "Actualizar_ViajeID"]

@router.get("/get_token/{endpoint}", status_code=status.HTTP_200_OK, tags=["GTrack"])
async def get_gtrack_token(endpoint: str, authenticated: bool = Depends(basic_auth)):
    if endpoint not in VALID_ENDPOINTS:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Endpoint no válido")
    
    try:
        token = gtrack_service.obtener_token(endpoint)
        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/os/interpolar", tags=["OS"])
def get_os_interpolar(db: Session = Depends(get_db), authenticated: bool = Depends(basic_auth)):
    try:
        os_list = gtrack_service.obtener_os_interpolar(db)
        if not os_list:
            raise HTTPException(status_code=404, detail="No se encontraron órdenes de servicio.")
        return os_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/os/interpolar2", tags=["OS"])
def get_os_interpolar2(db: Session = Depends(get_db), authenticated: bool = Depends(basic_auth)):
    try:
        os_list = gtrack_service.obtener_os_interpolar2(db)
        if not os_list:
            raise HTTPException(status_code=404, detail="No se encontraron órdenes de servicio.")
        return os_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))