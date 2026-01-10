# AuthForge

**AuthForge** is a secure and scalable User Management & Authentication service built with **FastAPI**, **JWT**, and **PostgreSQL**.  
It provides authentication, authorization, and user management features suitable for web and mobile applications.

---

## Features

- User Registration & Login
- Password Hashing (bcrypt)
- JWT Authentication (Access & Refresh Tokens)
- Role-Based Access Control (RBAC)
- Password Reset via Email (Optional)
- Token Refresh & Logout
- PostgreSQL Integration
- Docker-ready setup (Optional)

---

## Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT
- **Password Security**: bcrypt
- **Testing**: Pytest
- **Containerization (optional)**: Docker

---

## Setup & Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/AuthForge.git
cd AuthForge


Create a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Create .env file with:

DATABASE_URL=postgresql://username:password@localhost:5432/authforge
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30


Run the application:

uvicorn main:app --reload


Open Swagger docs in browser:

http://127.0.0.1:8000/docs
```
