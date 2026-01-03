from sanic.response import json
from models.user_model import create_user, get_user_by_username, get_user_by_email, verify_password
from utils.jwt_utils import generate_token
from sanic.log import logger

async def register(request):
    """
    Register a new user.
    
    Expected JSON body:
    {
        "username": "string",
        "email": "string",
        "password": "string"
    }
    """
    try:
        data = request.json
        
        # Validate required fields
        if not data or not all(k in data for k in ['username', 'email', 'password']):
            return json(
                {"error": "Missing required fields: username, email, password"},
                status=400
            )
        
        username = data['username']
        email = data['email']
        password = data['password']
        
        # Validate field lengths
        if len(username) < 3:
            return json(
                {"error": "Username must be at least 3 characters long"},
                status=400
            )
        
        if len(password) < 6:
            return json(
                {"error": "Password must be at least 6 characters long"},
                status=400
            )
        
        # Check if username already exists
        existing_user = get_user_by_username(username)
        if existing_user:
            return json(
                {"error": "Username already exists"},
                status=409
            )
        
        # Check if email already exists
        existing_email = get_user_by_email(email)
        if existing_email:
            return json(
                {"error": "Email already exists"},
                status=409
            )
        
        # Create the user
        user_id = create_user(username, email, password)
        
        logger.info(f"New user registered: {username} (ID: {user_id})")
        
        return json(
            {
                "message": "User registered successfully",
                "user_id": user_id,
                "username": username
            },
            status=201
        )
        
    except Exception as e:
        logger.error(f"Error during registration: {str(e)}")
        return json(
            {"error": "An error occurred during registration"},
            status=500
        )

async def login(request):
    """
    Login a user and return a JWT token.
    
    Expected JSON body:
    {
        "username": "string",
        "password": "string"
    }
    """
    try:
        data = request.json
        
        # Validate required fields
        if not data or not all(k in data for k in ['username', 'password']):
            return json(
                {"error": "Missing required fields: username, password"},
                status=400
            )
        
        username = data['username']
        password = data['password']
        
        # Get user from database
        user = get_user_by_username(username)
        if not user:
            return json(
                {"error": "Invalid username or password"},
                status=401
            )
        
        # Verify password
        if not verify_password(password, user['password_hash']):
            return json(
                {"error": "Invalid username or password"},
                status=401
            )
        
        # Generate JWT token
        token = generate_token(user['id'])
        
        logger.info(f"User logged in: {username} (ID: {user['id']})")
        
        return json(
            {
                "message": "Login successful",
                "token": token,
                "user": {
                    "id": user['id'],
                    "username": user['username'],
                    "email": user['email']
                }
            },
            status=200
        )
        
    except Exception as e:
        logger.error(f"Error during login: {str(e)}")
        return json(
            {"error": "An error occurred during login"},
            status=500
        )



