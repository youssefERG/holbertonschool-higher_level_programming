#!/usr/bin/python3
"""Simple API using Flask framework."""

from flask import Flask, jsonify, request, abort

app = Flask(__name__)
users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint returning welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_data():
    """Return all usernames in JSON format."""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """Return API status."""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return user data by username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user via POST request."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify(users[username]), 201


if __name__ == "__main__":
    app.run()