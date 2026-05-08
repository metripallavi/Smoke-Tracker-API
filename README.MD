# Smoking Tracker API

A FastAPI-based backend project for tracking cigarette smoking activity per user. The API supports user registration, JWT-based authentication, protected log management, daily log filtering, and summary statistics.

## Author

**Pallavi Metri**  
Backend Developer / DevOps

## Live API

- Render URL: https://smoke-tracker-api-3skh.onrender.com
- Swagger Docs: https://smoke-tracker-api-3skh.onrender.com/docs
- Health Check: https://smoke-tracker-api-3skh.onrender.com/health
## Overview

Smoking Tracker API is a backend service built with FastAPI, SQLAlchemy, and PostgreSQL. It allows users to register, log in securely, add smoking logs, view their logs, filter logs for the current day, delete logs, and view summary counts.

This project was designed as a clean, modular backend API with authentication, database integration, and automated testing.

## Features

- User registration
- JWT-based login authentication
- Get current logged-in user
- List all registered users
- Add smoking log entries
- View all logs for the authenticated user
- View only today's logs
- Delete a smoking log
- Get smoking log summary
- Interactive Swagger UI documentation
- Automated API tests using pytest

## Tech Stack

- **Backend Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Authentication:** OAuth2 Password Flow with JWT Bearer Token
- **Testing:** Pytest, FastAPI TestClient
- **ASGI Server:** Uvicorn

## Project Structure

```text
smoking-tracker-api/
├── app/
│   ├── api/
│   │   ├── auth.py
│   │   ├── cigarette_logs.py
│   │   └── users.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── crud/
│   │   └── cigarette_log.py
│   ├── db/
│   │   ├── base.py
│   │   ├── deps.py
│   │   └── session.py
│   ├── models/
│   │   ├── cigarette_log.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── cigarette_log.py
│   │   └── user.py
│   └── main.py
├── tests/
│   └── test_api.py
├── README.md
└── requirements.txt
```

## API Endpoints

### Default

- `GET /` - Root endpoint
- `GET /health` - Health check

### Users

- `POST /users/register` - Register a new user
- `GET /users` - List all users
- `GET /users/me` - Get current authenticated user

### Auth

- `POST /auth/login` - Login and get JWT access token

### Logs

- `POST /logs/` - Add a smoking log
- `GET /logs/` - List all logs for the current user
- `GET /logs/today` - List today's logs for the current user
- `GET /logs/summary` - Get summary of total logs and today's logs
- `DELETE /logs/{log_id}` - Delete a specific log

## Authentication Flow

This API uses JWT Bearer token authentication.

### Login

Send credentials to:

```http
POST /auth/login
```

Use form data:

- `username`
- `password`

### Response

```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

### Use the token

For protected endpoints, include the token in the Authorization header:

```http
Authorization: Bearer your_jwt_token
```

## Sample Log Summary Response

```json
{
  "total_logs": 5,
  "today_logs": 3
}
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd smoking-tracker-api
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add your configuration values.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/smoking_tracker
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
APP_NAME=Smoking Tracker API
APP_VERSION=0.1.0
```

## Run the Application

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- App: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- OpenAPI JSON: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

## Running Tests

Run the test suite with:

```bash
PYTHONPATH=. pytest -q
```

## Example Workflow

1. Register a user with `POST /users/register`
2. Login with `POST /auth/login`
3. Copy the returned JWT token
4. Authorize in Swagger UI using `Bearer <token>`
5. Add logs using `POST /logs/`
6. View logs using `GET /logs/`
7. View today's logs using `GET /logs/today`
8. View counts using `GET /logs/summary`
9. Delete a log using `DELETE /logs/{log_id}`

## Current Status

This project currently includes a working MVP backend with:

- Authentication
- User management
- Cigarette log tracking
- Daily log filtering
- Summary endpoint
- Delete support
- Automated tests

## Future Improvements

- Dedicated test database
- Update/edit log endpoint
- Weekly and monthly summary stats
- Docker support
- CI/CD pipeline
- Deployment configuration
- Pagination for logs

## License

This project is for learning and development purposes.
