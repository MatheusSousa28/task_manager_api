from app import crud, schemas
from app.security import verify_password


def test_crud_user_and_task_lifecycle(db_session):
    user = crud.create_user(
        db_session,
        schemas.UserCreate(name="João", email="joao@email.com", password="12345678"),
    )
    assert user.user_id is not None
    assert user.password != "12345678"
    assert verify_password("12345678", user.password) is True

    task = crud.create_task(
        db_session,
        schemas.TaskCreate(title="Estudar", description="SQLAlchemy", user_id=user.user_id),
    )
    assert task.task_id is not None
    assert task.completed is False

    updated = crud.update_task(db_session, task, schemas.TaskPatch(completed=True))
    assert updated.completed is True

    all_tasks = crud.get_tasks(db_session)
    assert len(all_tasks) == 1


def test_update_user_password_rehashes_value(db_session):
    user = crud.create_user(
        db_session,
        schemas.UserCreate(name="Lia", email="lia@email.com", password="12345678"),
    )
    old_hash = user.password

    updated = crud.update_user(db_session, user, schemas.UserPatch(password="87654321"))
    assert updated.password != old_hash
    assert verify_password("87654321", updated.password) is True
