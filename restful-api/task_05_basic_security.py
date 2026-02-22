#!/usr/bin/python3
"""Flask API with Basic Auth and JWT security."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "supersecretkey"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "alice": {"password": generate_password_hash("alice123"), "role": "admin"},
    "bob": {"password": generate_password_hash("bob123"), "role": "user"}
}


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for basic auth."""
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Route protected with Basic Auth."""
    return jsonify({"message": f"Hello, {auth.current_user()}!"})


@app.route("/login", methods=["POST"])
def login():
    """Authenticate user and return JWT token."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    username = request.json.get("username")
    password = request.json.get("password")
    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 400
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad credentials"}), 401
    token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify({"token": token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Route protected with JWT token."""
    identity = get_jwt_identity()
    return jsonify({"message": f"Hello, {identity['username']}!", "role": identity["role"]})


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Route accessible only to admin role."""
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Forbidden"}), 403
    return jsonify({"message": f"Welcome admin {identity['username']}!"})


if __name__ == "__main__":
    app.run()