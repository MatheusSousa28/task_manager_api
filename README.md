# Task Manager API (FastAPI + SQLAlchemy)

Projeto de portfólio com API REST para gestão de usuários e tarefas.

## Stack
- FastAPI
- SQLAlchemy ORM
- SQLite (local)
- Pytest

## Como rodar localmente

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

A API sobe em `http://127.0.0.1:8000`.

## Banco de dados
Por padrão, o banco local é SQLite em `task_manager.db`.

Você pode sobrescrever com variável de ambiente:

```bash
export DATABASE_URL="sqlite:///./task_manager.db"
```

## Rotas principais
- `POST /users/`
- `GET /users/{user_id}`
- `GET /users/?user_email=...`
- `PATCH /users/{user_id}`
- `DELETE /users/{user_id}`
- `POST /tasks/`
- `GET /tasks/{task_id}`
- `GET /tasks/`
- `PATCH /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

## Testes (unitário, integração e sistema)

```bash
pytest -q
```

Arquivos de teste:
- `tests/test_unit_schemas.py` (unitário)
- `tests/test_integration_crud.py` (integração)
- `tests/test_system_api.py` (sistema)
