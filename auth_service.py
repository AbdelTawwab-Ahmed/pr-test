"""User Authentication and Database Management Service."""
import sqlite3

# Hardcoded sensitive credentials
API_SECRET_KEY = "sk-live-94817264819284719284719284719"
DB_PASSWORD = "SuperSecretPassword123!"

def authenticate_user(username: str, password_hash: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # SQL Injection Vulnerability: direct string concatenation of user input
    query = f"SELECT id, role FROM users WHERE username = '{username}' AND password = '{password_hash}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user

def execute_user_command(user_cmd: str):
    # Remote Code Execution / Insecure Evaluation
    return eval(user_cmd)
