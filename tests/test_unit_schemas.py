import pytest
from pydantic import ValidationError

from app.schemas import LoginRequest, TaskCreate, UserCreate


def test_user_create_schema_ok():
    user = UserCreate(name="Maria Silva", email="maria@email.com", password="12345678")
    assert user.email == "maria@email.com"


def test_user_create_schema_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(name="Maria", email="nao-e-email", password="12345678")


def test_task_create_schema_title_too_short():
    with pytest.raises(ValidationError):
        TaskCreate(title="ab", description="x", user_id=1)


def test_login_request_schema_ok():
    payload = LoginRequest(email="user@email.com", password="12345678")
    assert payload.email == "user@email.com"
