
# 🚀 Sanic CRUD API Example

A simple CRUD API built with [Sanic](https://sanic.dev/) for practicing the basics of building high-performance web APIs in Python. This project includes a modular structure with controllers, models, database seeding, and runs easily with Docker.

Ideal for developers looking to explore Sanic’s asynchronous capabilities, request handling, and best practices for structuring a web API.

---

## 📦 Features

✅ Fully asynchronous API with Sanic  
✅ CRUD endpoints for a single entity (`Item`)  
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

Once the app is running on **http://localhost:8000**, the following CRUD routes are available:

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

**List all items**
```bash
curl -X GET http://localhost:8000/items
```

**Get a specific item**
```bash
curl -X GET http://localhost:8000/items/1
```

**Create a new item**
```bash
curl -X POST http://localhost:8000/items -H "Content-Type: application/json" -d '{"name": "New Item", "description": "A new item added to the database"}'
```

**Update an item**
```bash
curl -X PUT http://localhost:8000/items/1 -H "Content-Type: application/json" -d '{"name": "Updated Item", "description": "Updated description"}'
```

**Delete an item**
```bash
curl -X DELETE http://localhost:8000/items/1
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
