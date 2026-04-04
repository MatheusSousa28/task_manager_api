# Task Manager API (FastAPI + SQLAlchemy)

REST API for managing users and tasks with JWT authentication,
access control, and automated tests (unit, integration, and system).

Project developed with a focus on backend best practices, including
layer separation, security, and testability.

## Stack
- FastAPI
- SQLAlchemy ORM
- SQLite (local)
- Password authentication with hashing (Argon2 + Passlib)
- JWT with Python-JOSE
- Pytest

## How to run locally

### Linux/macOS
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

### Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

The API will run at `http://127.0.0.1:8000`, access `http://127.0.0.1:8000/docs` to view the routes.

## Database
By default, the local database is SQLite at `task_manager.db`.

You can override it with an environment variable:

``` bash
export DATABASE_URL="sqlite:///./task_manager.db"
```

## Security
- Passwords are stored using Argon2 hashing.
- Login generates a JWT `access_token` with expiration.
- `SECRET_KEY` and auth parameters are stored in the `.env` file.

## Main endpoints
- `POST /users/` (register)
- `GET /users/{user_id}`
- `GET /users/?user_email=...`
- `PATCH /users/{user_id}`
- `DELETE /users/{user_id}`
- `POST /auth/login` (returns JWT)
- `POST /tasks/`
- `GET /tasks/{task_id}`
- `GET /tasks/`
- `PATCH /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

## Tests (unit, integration, and system)
To run the tests:

``` bash
pytest -q
```

Test files:
- `tests/test_unit_schemas.py` (unit)
- `tests/test_unit_security.py` (unit)
- `tests/test_integration_crud.py` (integration)
- `tests/test_system_api.py` (system)

[Read this in Brazilian Portuguese](README.pt.md)