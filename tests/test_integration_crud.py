from app import crud, schemas


def test_crud_user_and_task_lifecycle(db_session):
    user = crud.create_user(
        db_session,
        schemas.UserCreate(name="João", email="joao@email.com", password="12345678"),
    )
    assert user.user_id is not None

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
