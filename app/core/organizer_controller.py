from flask import request, jsonify
from config import Config
from app.utils import hash_password, validate_password
import mysql.connector
from flask_jwt_extended import create_access_token

# Registro de organizador
def register_organizer():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    phone = data.get("phone", "")
    status = data.get("status", "activo")

    if not name or not email or not password:
        return jsonify({"error": "Name, email and password are required"}), 400

    try:
        conn = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB,
            port=Config.MYSQL_PORT
        )
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM organizers WHERE email = %s", (email,))
        if cursor.fetchone():
            return jsonify({"error": "Email already registered"}), 409

        hashed_pwd = hash_password(password)
        cursor.execute(
            "INSERT INTO organizers (name, email, password, phone, status) VALUES (%s, %s, %s, %s, %s)",
            (name, email, hashed_pwd, phone, status)
        )
        conn.commit()

        return jsonify({"message": "Organizer registered successfully"}), 201

    except mysql.connector.Error as err:
        return jsonify({"error": f"MySQL error: {err}"}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# Login de organizador
def login_organizer():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Request body must be in JSON format"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    try:
        conn = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB,
            port=Config.MYSQL_PORT
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, email, password FROM organizers WHERE email = %s", (email,))
        organizer = cursor.fetchone()

        if not organizer or not validate_password(password, organizer["password"]):
            return jsonify({"error": "Invalid email or password"}), 401

        token = create_access_token(identity=str(organizer["id"]), additional_claims={"email": organizer["email"]})

        return jsonify({"token": token}), 200

    except mysql.connector.Error as err:
        return jsonify({"error": f"MySQL error: {err}"}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
