# app/api/Gtrack/services.py

from app.utils.token_utils import get_token

class GtrackService:
    
    def obtener_token(self, endpoint: str) -> str:
        return get_token(endpoint)

# Instancia del servicio para ser utilizada en los routers
gtrack_service = GtrackService()
