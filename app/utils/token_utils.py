# utils/token_utils.py

import requests
import base64
from app.core.config import GT_USER, GT_PASSWORD

def get_token(endpoint: str) -> str:

    url = f'https://gtrack.cl/Obtener_Token/{endpoint}/'

    auth_str = f"{GT_USER}:{GT_PASSWORD}"

    b64_auth_str = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')

    headers = {
        "Authorization": f"Basic {b64_auth_str}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error al obtener el token desde {url}: {response.status_code} - {response.text}")

    rest = response.text
    new_token = rest.split(':')[1].strip().strip('"').strip("'")

    return new_token