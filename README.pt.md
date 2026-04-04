# Task Manager API (FastAPI + SQLAlchemy)

API REST para gerenciamento de usuários e tarefas com autenticação JWT,
 controle de acesso e testes automatizados (unitários, de integração e de sistema).

Projeto desenvolvido com foco nas melhores práticas de backend, 
incluindo separação de camadas, segurança e testabilidade.

## Stack
- FastAPI
- SQLAlchemy ORM
- SQLite (local)
- Autenticação com senha hash (Argon2 + Passlib)
- JWT com Python-JOSE
- Pytest

## Como rodar localmente

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env  # no Windows: copy .env.example .env
uvicorn app.main:app --reload
```

A API sobe em `http://127.0.0.1:8000`, acesse `http://127.0.0.1:8000/docs` para visualizar as rotas.

## Banco de dados
Por padrão, o banco local é SQLite em `task_manager.db`.

Você pode sobrescrever com variável de ambiente:

```bash
export DATABASE_URL="sqlite:///./task_manager.db"
```

## Segurança
- Senhas são armazenadas com hash Argon2 (nunca em texto puro).
- Login gera `access_token` JWT com expiração.
- `SECRET_KEY` e parâmetros de auth ficam no `.env`.

## Rotas principais
- `POST /users/` (cadastro)
- `GET /users/{user_id}`
- `GET /users/?user_email=...`
- `PATCH /users/{user_id}`
- `DELETE /users/{user_id}`
- `POST /auth/login` (retorna JWT)
- `POST /tasks/`
- `GET /tasks/{task_id}`
- `GET /tasks/`
- `PATCH /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

## Testes (unitário, integração e sistema)
Para rodar os testes:
```bash
pytest -q
```

Arquivos de teste:
- `tests/test_unit_schemas.py` (unitário)
- `tests/test_unit_security.py` (unitário)
- `tests/test_integration_crud.py` (integração)
- `tests/test_system_api.py` (sistema)

[Leia isso em Inglês](README.md)