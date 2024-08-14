import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

USUARIO= os.getenv("USUARIO")
PASSWORD= os.getenv("PASSWORD")
MYSQL_HOST= os.getenv("MYSQL_HOST")
MYSQL_PORT= os.getenv("MYSQL_PORT")
DATABASE= os.getenv("DATABASE")