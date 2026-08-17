from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os
app = Flask(__name__)
CORS(app)

# MySQL connection
db = mysql.connector.connect(
    host=os.getenv("DB_HOST", "mysql"),
    user=os.getenv("DB_USER", "webapp"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME", "userdb")
)



@app.route("/")
def home():
    return "Multi-Tier Application Backend is Running!"

@app.route("/health")
def health():
    return "OK"

@app.route("/hello")
def hello():
    return "Hello from Flask Backend!"

# Add user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    name = data["name"]
    email = data["email"]

    cursor = db.cursor()

    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(query, (name, email))

    db.commit()
    cursor.close()

    return jsonify({
        "message": "User added successfully"
    }), 201

# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    cursor.close()

    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)















