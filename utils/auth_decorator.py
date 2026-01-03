from functools import wraps
from sanic.response import json
from utils.jwt_utils import verify_token
from models.user_model import get_user_by_id

def protected():
    """
    Decorator to protect routes with JWT authentication.
    
    Usage:
        @protected()
        async def my_protected_route(request):
            user = request.ctx.user
            return json({"message": f"Hello {user['username']}"})
    """
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            # Extract token from Authorization header
            auth_header = request.headers.get('Authorization')
            
            if not auth_header:
                return json(
                    {"error": "Authorization header missing"},
                    status=401
                )
            
            # Check if it's a Bearer token
            parts = auth_header.split()
            if len(parts) != 2 or parts[0].lower() != 'bearer':
                return json(
                    {"error": "Invalid authorization header format. Use: Bearer <token>"},
                    status=401
                )
            
            token = parts[1]
            
            # Verify the token
            payload = verify_token(token)
            if not payload:
                return json(
                    {"error": "Invalid or expired token"},
                    status=401
                )
            
            # Get user from database
            user_id = payload.get('user_id')
            user = get_user_by_id(user_id)
            
            if not user:
                return json(
                    {"error": "User not found"},
                    status=401
                )
            
            # Attach user to request context
            request.ctx.user = user
            
            # Call the actual route handler
            response = await f(request, *args, **kwargs)
            return response
        
        return decorated_function
    return decorator



