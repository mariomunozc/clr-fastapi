from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import USUARIO, PASSWORD, MYSQL_HOST, MYSQL_PORT, DATABASE

URL_DATABASE = f'mysql+pymysql://{USUARIO}:{PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{DATABASE}'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()