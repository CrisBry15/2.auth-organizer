# este archivo se configuro para que este disponible en todo el microservicio.
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "organizer-secret")  
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")


    JWT_TOKEN_LOCATION = ["headers"]
    JWT_HEADER_NAME = "Authorization"
    JWT_HEADER_TYPE = "Bearer"