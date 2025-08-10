# My FastAPI Application

A simple FastAPI application for user registration and retrieval of registered users.

## Features

- **Register a user** with:
  - Username (min 3, max 50 characters)
  - Email (validated format)
  - Full Name (min 1, max 100 characters)
  - Password (min 6, max 100 characters)
- **List all registered users**
- **Validation** using Pydantic models
- **Error handling** for duplicate email registrations

---

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn
- typing
---

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/my-fastapi-app.git
    cd my-fastapi-app
    ```

2. **Create and activate a virtual environment**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate   # On Windows: .venv\Scripts\activate
    ```

3. **Install dependencies**
    ```bash
    pip install fastapi uvicorn
    ```

---

## Running the Application

Run the following command:

```bash
uvicorn main:app --reload
The app will be available at: http://127.0.0.1:8000

Interactive API docs will be available at:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

API Endpoints
1. Register User
POST /register

Request Body:

json
Copy
Edit
{
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "password": "securepassword"
}
Response:

json
Copy
Edit
{
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "registered": true
}
2. Get All Users
GET /users

Response:

json
Copy
Edit
[
  {
    "username": "john_doe",
    "email": "john@example.com",
    "full_name": "John Doe",
    "registered": true
  }
]
Notes
Data Storage: This app stores users in memory (registered_users list). All data will be lost when the server restarts.

Email Uniqueness: Duplicate email registrations are rejected.

Security: Passwords are stored in plain text for demonstration purposes. In a production environment:

Use password hashing (bcrypt or passlib).

Use a database for persistent storage.

Version Control
Version: 1.0.0
Author: Abhrajit Pal