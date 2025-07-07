import os
import mysql.connector
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

def test_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DB'),
            port=int(os.getenv('MYSQL_PORT'))
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL.")
            connection.close()
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")

if __name__ == "__main__":
    test_db_connection()