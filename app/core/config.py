import os
from dotenv import load_dotenv

load_dotenv()

USUARIO= os.getenv("USUARIO")
PASSWORD= os.getenv("PASSWORD")
MYSQL_HOST= os.getenv("MYSQL_HOST")
MYSQL_PORT= os.getenv("MYSQL_PORT")
DATABASE= os.getenv("DATABASE")
GT_USER = os.getenv('GT_USER')
GT_PASSWORD = os.getenv('GT_PASSWORD')