# Task Manager API (FastAPI + SQLAlchemy)

API REST para gerenciamento de usuários e tarefas com autenticação JWT,  
controle de acesso e testes automatizados (unitários, integração e sistema).

Projeto desenvolvido com foco em boas práticas de backend, incluindo  
separação de camadas, segurança e testabilidade.

## 🚀 Diferenciais do projeto

- Arquitetura em camadas (routers, schemas, CRUD)
- Autenticação stateless com JWT
- Hash de senha com Argon2 (segurança moderna)
- Testes automatizados (unitário, integração e sistema)
- Configuração via variáveis de ambiente (.env)

## Stack
- FastAPI
- SQLAlchemy ORM
- SQLite (local)
- Autenticação com senha hash (Argon2 + Passlib)
- JWT com Python-JOSE
- Pytest

## Como rodar localmente

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

A API sobe em `http://127.0.0.1:8000`, acesse `http://127.0.0.1:8000/docs` para visualizar as rotas.

## Banco de dados
Por padrão, o banco local é SQLite em `task_manager.db`.

Você pode sobrescrever com variável de ambiente:

```bash
export DATABASE_URL="sqlite:///./task_manager.db"
```

## Segurança
- Senhas são armazenadas com hash Argon2.
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
