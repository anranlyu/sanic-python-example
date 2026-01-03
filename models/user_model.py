from database.db import get_connection
from passlib.hash import bcrypt

def create_user(username, email, password):
    """
    Create a new user with hashed password.
    """
    password_hash = bcrypt.hash(password)
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, password_hash)
        )
        conn.commit()
        return cursor.lastrowid

def get_user_by_username(username):
    """
    Retrieve a user by username.
    """
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, username, email, password_hash, created_at FROM users WHERE username = %s",
            (username,)
        )
        return cursor.fetchone()

def get_user_by_email(email):
    """
    Retrieve a user by email.
    """
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, username, email, password_hash, created_at FROM users WHERE email = %s",
            (email,)
        )
        return cursor.fetchone()

def get_user_by_id(user_id):
    """
    Retrieve a user by ID.
    """
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, username, email, created_at FROM users WHERE id = %s",
            (user_id,)
        )
        return cursor.fetchone()

def verify_password(password, password_hash):
    """
    Verify a password against its hash.
    """
    return bcrypt.verify(password, password_hash)



