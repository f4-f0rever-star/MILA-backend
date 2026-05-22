# MILA-BACKEND
MILA is a cultural learning platform API built with Flask.
It provides country culture data, traditions, cuisine, history, and user authentication endpoints.

## Features
- Flask application factory pattern
- CORS enabled for frontend intergration
- JWT authentication
- SQLAlchemy database support
- Flask-Migrate for migrations
- REST API structure for cultures, auth, and user data

## Tech Stack
- Python
- Flask
- Flask-CORS
- Flask-JWT-Extended
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt
- PostgreSQL

## Project Structure
```text
MILA-backend/
    app/
        __init__.py
        config.py
        extensions.py
        models/
        routes/
        services/
    migrations/
    requirements.txt
    main.py
```

## INSTALLATION
1. Clone the repository
  - https://github.com/f4-f0rever-star/MILA-backend
2. Create and activate a virtual environment
  - python3 -m venv .venv
  - source .venv/bin/activate
3. Install dependencies
  - pip install -r requirements.txt

## Environment variables
- Create a .env file if needed:
  SECRET_KEY=your-secret-key
  JWT_SECRET_KEY=your-jwt-secret
  DATABASE_URL=sqlite:///mila.db

## Running the backend
```text
python3 main.py or flask run
```

# API ROUTES
## Auth
- POST /api/auth/signup
- POST /api/auth/login

## Cultures
- GET /api/cultures/
- GET /api/cultures/<culture_id>

## Users
- GET /api/user/profile
- GET /api/user/progress

## CORS
CORS is enabled in the Flask app so that the React frontend can call the API from a different port during development

## JWT Authentication
Protected routes require a Bearer token:
```text
Authorization: Bearer <token>
```

##Notes
- Use flask db init, flask db migrate, and flask db upgrade if you are using migrations
- Update the database URI in config.py for your environment
