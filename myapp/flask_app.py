import os
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default_secret_key")  # Secret key للجلسة

# تفعيل Prometheus metrics
metrics = PrometheusMetrics(app)

# قراءة username/password من الـ Secret (متغيرات البيئة)
FLASK_USER = os.getenv("FLASK_USER", "admin")
FLASK_PASSWORD = os.getenv("FLASK_PASSWORD", "admin123")

# تخزين المستخدم من Secret
users = {
    FLASK_USER: generate_password_hash(FLASK_PASSWORD)
}

@app.route("/")
def home():
    if "username" in session:
        return jsonify({"message": f"Welcome {session['username']}!"})
    return jsonify({"message": "You are not logged in"}), 401

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(users[username], password):
        session["username"] = username
        return jsonify({"message": "Login successful!"})
    return jsonify({"message": "Invalid credentials"}), 401

@app.route("/logout", methods=["POST"])
def logout():
    session.pop("username", None)
    return jsonify({"message": "Logged out"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
