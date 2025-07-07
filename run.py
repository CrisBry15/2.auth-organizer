# run.py
from app.init import create_app
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
