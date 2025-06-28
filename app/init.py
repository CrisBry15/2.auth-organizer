from flask import Flask
from config import Config
from app.routes import organizer_bp

from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar JWT
    jwt = JWTManager(app)

    # Registrar blueprint
    app.register_blueprint(organizer_bp, url_prefix='/organizer')

    return app
