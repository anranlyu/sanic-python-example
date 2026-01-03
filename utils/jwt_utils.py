import jwt
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv('JWT_SECRET', 'your-secret-key-change-this-in-production')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')
JWT_EXPIRATION_HOURS = int(os.getenv('JWT_EXPIRATION_HOURS', '24'))

def generate_token(user_id):
    """
    Generate a JWT token for a user.
    
    Args:
        user_id: The user's ID to encode in the token
        
    Returns:
        str: The encoded JWT token
    """
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=JWT_EXPIRATION_HOURS),
        'iat': datetime.utcnow()
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def verify_token(token):
    """
    Verify and decode a JWT token.
    
    Args:
        token: The JWT token to verify
        
    Returns:
        dict: The decoded payload if valid, None otherwise
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.InvalidTokenError:
        # Token is invalid
        return None



