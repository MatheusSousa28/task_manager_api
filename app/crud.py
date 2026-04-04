"""Camada de acesso a dados (CRUD)."""

from pydantic import EmailStr
from sqlalchemy.orm import Session

from app import models, schemas
from app.security import hash_password


# Usuários

def create_user(db: Session, user: schemas.UserCreate):
    payload = user.model_dump()
    payload["password"] = hash_password(payload["password"])
    db_user = models.User(**payload)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_user_by_email(db: Session, email: EmailStr):
    return db.query(models.User).filter(models.User.email == str(email)).first()


def update_user(db: Session, db_user: models.User, user_in: schemas.UserPatch):
    patch_data = user_in.model_dump(exclude_unset=True)
    if "password" in patch_data:
        patch_data["password"] = hash_password(patch_data["password"])

    for field, value in patch_data.items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, db_user: models.User):
    db.delete(db_user)
    db.commit()
    return db_user


# Tarefas

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.task_id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Task).offset(skip).limit(limit).all()


def update_task(db: Session, db_task: models.Task, task_in: schemas.TaskPatch):
    for field, value in task_in.model_dump(exclude_unset=True).items():
        setattr(db_task, field, value)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, db_task: models.Task):
    db.delete(db_task)
    db.commit()
    return db_task
