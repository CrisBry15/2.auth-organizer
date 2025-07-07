from flask import Blueprint, jsonify
from app.organizer_controller import register_organizer, login_organizer
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

# Definición del blueprint
organizer_bp = Blueprint('organizer', __name__)

# Ruta de prueba
@organizer_bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Auth Organizer Microservice funcionando correctamente"})

# Ruta para login
@organizer_bp.route('/login', methods=['POST'])
def login_route():
    return login_organizer()

# Ruta para registro
@organizer_bp.route('/register', methods=['POST'])
def register_route():
    return register_organizer()

# Ruta protegida
@organizer_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    claims = get_jwt()
    current_user = get_jwt_identity()
    return jsonify({
        "message": "Token válido",
        "organizer_id": current_user,
        "email": claims.get("email")
    }), 200
