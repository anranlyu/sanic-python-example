
# 🚀 Sanic CRUD API Example

A simple CRUD API built with [Sanic](https://sanic.dev/) for practicing the basics of building high-performance web APIs in Python. This project includes a modular structure with controllers, models, database seeding, and runs easily with Docker.

Ideal for developers looking to explore Sanic’s asynchronous capabilities, request handling, and best practices for structuring a web API.

---

## 📦 Features

✅ Fully asynchronous API with Sanic  
✅ JWT-based authentication with user registration and login  
✅ Protected CRUD endpoints for a single entity (`Item`)  
✅ Modular structure with controllers and models  
✅ Database migration and seed scripts  
✅ Docker & Docker Compose support for easy setup  
✅ Ready-to-use environment for experimenting with Sanic

---

## 🗂️ Project Structure


.
├── app/
│   ├── controllers/       # Route handlers (controllers)
│   ├── models/            # Database models
│   ├── seeds/             # Seed scripts for database population
│   └── main.py            # Entry point for the Sanic app
├── database/
│   ├── migrate.py         # Migration script
│   └── seed.py            # Seed script
├── Dockerfile             # Docker image definition
├── docker-compose.yml     # Docker Compose services configuration
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/guduchango/sanic-python-example.git
cd sanic-python-example
```

---

## 🐳 Running with Docker

Build the Docker image:

```bash
docker-compose build
```

Start the containers:

```bash
docker-compose up
```

---

## 🐳 MySQL in Docker + Web app on your host (recommended for development)

If you want to keep running the Sanic app in your local virtualenv (fast iteration), but run **only MySQL** in Docker:

1) Start only the MySQL container:

```bash
docker compose up -d db
```

2) Create a local `.env` file (copy `env.example`) and make sure it contains:

```bash
MYSQL_HOST=localhost
MYSQL_PORT=3320
MYSQL_USER=app
MYSQL_PASSWORD=app_password
MYSQL_DATABASE=test_db
JWT_SECRET=your-secret-key-change-this-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
```

3) Run migrations + seed from your venv (host):

```bash
python -m database.migrate
python -m database.seed --count 10
```

4) Start the API locally:

```bash
python app.py
```

5) Test:

```bash
curl http://localhost:8000/items
```

Notes:
- If you previously ran MySQL with a different password, reset the Docker DB volume: `docker compose down -v` then `docker compose up -d db`.
- The Docker MySQL is exposed on **host port 3320**, mapped to the container’s internal **3306**.

---

## 🛠️ Database Migrations & Seeding

Run database migrations:

```bash
docker-compose run web python database/migrate.py
```

Seed the database with initial data:

```bash
docker-compose run web python database/seed.py
```

---

## 📚 API Endpoints

Once the app is running on **http://localhost:8000**, the following routes are available:

### Authentication Endpoints (Public)

| Method | Route        | Description                    |
|--------|--------------|--------------------------------|
| POST   | `/register`  | Register a new user            |
| POST   | `/login`     | Login and receive JWT token    |

### Item Endpoints (Protected - Requires JWT)

| Method | Route                 | Description               |
|--------|-----------------------|---------------------------|
| GET    | `/`                   | Health check/test route   |
| GET    | `/items`              | List all items            |
| GET    | `/items/<item_id>`    | Retrieve an item by ID    |
| POST   | `/items`              | Create a new item         |
| PUT    | `/items/<item_id>`    | Update an existing item   |
| DELETE | `/items/<item_id>`    | Delete an existing item   |

---

## ✅ Example Requests with curl

### Authentication Flow

**1. Register a new user**
```bash
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "secure_password123"
  }'
```

**2. Login to get JWT token**
```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "secure_password123"
  }'
```

Response will include a JWT token:
```json
{
  "message": "Login successful",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  }
}
```

### Protected Item Endpoints

**Note:** All item endpoints require authentication. Include the JWT token in the `Authorization` header as `Bearer <token>`.

**List all items**
```bash
curl -X GET http://localhost:8000/items \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

**Get a specific item**
```bash
curl -X GET http://localhost:8000/items/1 \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

**Create a new item**
```bash
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "name": "New Item",
    "description": "A new item added to the database",
    "price": 29.99
  }'
```

**Update an item**
```bash
curl -X PUT http://localhost:8000/items/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "name": "Updated Item",
    "description": "Updated description",
    "price": 39.99
  }'
```

**Delete an item**
```bash
curl -X DELETE http://localhost:8000/items/1 \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

---

## 🔗 Access the API

Once running, your API will be available at:

```
http://localhost:8000
```

---

## 📝 Prerequisites

- Docker
- Docker Compose

---

## 📄 License

MIT License.

---

## 🙌 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.
