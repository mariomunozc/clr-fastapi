import os
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

# Configuramos el esquema de autenticación básica
security = HTTPBasic()

class BasicAuthService:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def authenticate(self, credentials: HTTPBasicCredentials):
        if credentials.username == self.username and credentials.password == self.password:
            return True
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

# Cargamos las credenciales desde las variables de entorno
def get_basic_auth_service() -> BasicAuthService:
    username = os.getenv("API_USER_1", "")
    password = os.getenv("API_PASSWORD_1", "")
    return BasicAuthService(username, password)

# Dependencia que se usará en los endpoints
def basic_auth(credentials: HTTPBasicCredentials = Depends(security), auth_service: BasicAuthService = Depends(get_basic_auth_service)):
    if auth_service.authenticate(credentials):
        return True
    raise HTTPException(status_code=401, detail="Autenticación fallida")
