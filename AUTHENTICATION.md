# JWT Authentication Guide

## Overview

This Sanic application now includes JWT-based authentication. All `/items` endpoints are protected and require a valid JWT token.

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Copy `env.example` to `.env` and update the JWT secret:

```bash
cp env.example .env
```

Edit `.env` and change the `JWT_SECRET` to a secure random string for production.

### 3. Run Database Migration

```bash
python -m database.migrate
```

This will create both the `items` and `users` tables.

### 4. Start the Application

```bash
python app.py
```

The API will be available at `http://localhost:8000`

## Authentication Flow

### Step 1: Register a User

```bash
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123"
  }'
```

**Response:**
```json
{
  "message": "User registered successfully",
  "user_id": 1,
  "username": "testuser"
}
```

### Step 2: Login to Get JWT Token

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "password123"
  }'
```

**Response:**
```json
{
  "message": "Login successful",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "user": {
    "id": 1,
    "username": "testuser",
    "email": "test@example.com"
  }
}
```

### Step 3: Use the Token to Access Protected Endpoints

Copy the token from the login response and use it in the `Authorization` header:

```bash
curl -X GET http://localhost:8000/items \
  -H "Authorization: Bearer YOUR_JWT_TOKEN_HERE"
```

## Architecture

### New Files Created

1. **`models/user_model.py`** - User database operations
   - `create_user()` - Register new users with bcrypt password hashing
   - `get_user_by_username()` - Fetch user for login
   - `get_user_by_id()` - Fetch user for token validation
   - `verify_password()` - Verify password against hash

2. **`utils/jwt_utils.py`** - JWT token management
   - `generate_token()` - Create JWT tokens with 24-hour expiration
   - `verify_token()` - Validate and decode JWT tokens

3. **`utils/auth_decorator.py`** - Authentication decorator
   - `@protected()` - Decorator to protect routes with JWT authentication

4. **`controllers/auth_controller.py`** - Authentication endpoints
   - `register()` - Handle user registration
   - `login()` - Handle user login and token generation

5. **`routes/auth_routes.py`** - Authentication routes blueprint
   - POST `/register`
   - POST `/login`

### Modified Files

1. **`requirements.txt`** - Added `PyJWT` dependency
2. **`env.example`** - Added JWT configuration variables
3. **`database/migrate.py`** - Added `users` table creation
4. **`controllers/item_controller.py`** - Added `@protected()` decorator to all item endpoints
5. **`app.py`** - Registered `auth_bp` blueprint
6. **`README.md`** - Updated with authentication documentation

## Security Features

- **Password Hashing**: Passwords are hashed using bcrypt before storage
- **JWT Tokens**: Stateless authentication with configurable expiration
- **Protected Routes**: All item endpoints require valid JWT tokens
- **Token Validation**: Tokens are verified on each request to protected endpoints

## Configuration

JWT settings in `.env`:

```
JWT_SECRET=your-secret-key-change-this-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
```

- **JWT_SECRET**: Secret key for signing tokens (change in production!)
- **JWT_ALGORITHM**: Algorithm for JWT encoding (HS256 recommended)
- **JWT_EXPIRATION_HOURS**: Token validity period in hours

## Error Responses

### 400 Bad Request
- Missing required fields
- Invalid input validation

### 401 Unauthorized
- Missing Authorization header
- Invalid or expired token
- Invalid credentials

### 409 Conflict
- Username already exists
- Email already exists

## Testing with Postman or Insomnia

1. Create a POST request to `/register` with JSON body
2. Create a POST request to `/login` with JSON body
3. Copy the token from the login response
4. For protected endpoints, add header: `Authorization: Bearer <token>`

## Database Schema

### Users Table

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Next Steps

- Consider adding refresh tokens for better security
- Implement role-based access control (RBAC)
- Add email verification for new users
- Implement password reset functionality
- Add rate limiting to prevent brute force attacks



