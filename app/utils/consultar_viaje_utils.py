# utils/consultar_viaje_utils.py

import requests

def consultar_viaje(id_viaje: int, token: str) -> dict:
    """
    Consulta la información de un viaje en la API externa usando el id_viaje.

    Args:
        id_viaje (int): El identificador del viaje a consultar.
        token (str): El token de autenticación para la API externa.

    Returns:
        dict: La respuesta de la API externa en formato JSON.
    
    Raises:
        Exception: Si la API externa devuelve un error.
    """

    url = "https://gtrack.cl/Consultar_ViajeID/"
    
    headers = {
        "Authorization": f"Bearer {token}",
    }

    # Enviar datos como form-data
    data = {
        "id_viaje": str(id_viaje)  # Asegúrate de que sea una cadena, ya que form-data generalmente usa cadenas
    }

    # Realizar la solicitud POST usando form-data
    response = requests.post(url, data=data, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error al consultar el viaje {id_viaje}: {response.status_code} - {response.text}")

    return response.json()
