# app/api/Gtrack/services.py

from app.utils.token_utils import get_token
from app.utils.consultar_viaje_utils import consultar_viaje
from sqlalchemy.orm import Session
from sqlalchemy import and_, func
from app.api.gtrack.models import Os  # Asegúrate de importar tu modelo Os

class GtrackService:
    
    def obtener_token(self, endpoint: str) -> str:
        return get_token(endpoint)
    
    def obtener_os_interpolar(self, db: Session):
        """Obtiene las órdenes de servicio (OS) para hoy donde transporte es 'Interpolar',
        interpolar_id no es nulo y patente es nulo.
        """

        os_list = db.query(
            Os.os_id,
            Os.os_num,
            Os.interpolar_id,
            Os.fecha
        ).filter(
            and_(
                Os.fecha == func.curdate(),
                Os.transporte == "Interpolar",
                Os.interpolar_id.isnot(None),
                # Os.patente.is_(None),
                # Os.os_estado.is_(None),
                # Os.status.is_(None)
            )
        ).all()

        result = [
            {
                "os_id": os.os_id,
                "os_num": os.os_num,
                "interpolar_id": int(os.interpolar_id) if os.interpolar_id is not None else None,
                "fecha": os.fecha,
            }
            for os in os_list
        ]

        return result
    
    def obtener_os_interpolar2(self, db: Session) -> list:

        os_list = db.query(
            Os.os_id,
            Os.os_num,
            Os.interpolar_id,
            Os.fecha,
            Os.patente
        ).filter(
            and_(
                Os.fecha == func.curdate(),
                Os.transporte == "Interpolar",
                Os.interpolar_id.isnot(None),
                # Os.patente.is_(None),
                # Os.os_estado.is_(None),
                # Os.status.is_(None)
            )
        ).all()

        token = self.obtener_token("Consultar_ViajeID")  # Reemplaza "your_endpoint" con el endpoint adecuado

        result = []

        for os in os_list:
            interpolar_id = int(os.interpolar_id) if os.interpolar_id is not None else None

            if interpolar_id is not None:
                try:
                    # Llamar a la API externa para obtener la información del viaje
                    external_data = consultar_viaje(interpolar_id, token)
                    
                    # Agregar la información obtenida al resultado final
                    result.append({
                        "os_id": os.os_id,
                        "os_num": os.os_num,
                        "interpolar_id": interpolar_id,
                        "fecha": os.fecha,
                        "patente": os.patente,
                        "external_data": external_data  # Información real obtenida de la API externa
                    })
                except Exception as e:
                    # Manejar errores en caso de que la API externa falle
                    # Agregamos un log detallado para capturar el error exacto
                    print(f"Error processing OS with interpolar_id {interpolar_id}: {e}")
                    result.append({
                        "os_id": os.os_id,
                        "os_num": os.os_num,
                        "interpolar_id": interpolar_id,
                        "fecha": os.fecha,
                        "error": str(e)
                    })

        # Verificación adicional para asegurar que no se intenta acceder a un índice que no existe
        if not result:
            return {"detail": "No OS available or all external API calls failed"}

        # Retorna el array con toda la información de las OS y sus viajes obtenidos de la API externa
        return result
    
# Instancia del servicio para ser utilizada en los routers
gtrack_service = GtrackService()
