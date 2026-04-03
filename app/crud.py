"""
Data access layer (CRUD) responsável por encapsular
operações de persistência utilizando SQLAlchemy ORM.
Não contém lógica HTTP ou regras de negócio.
"""

from sqlalchemy.orm import Session
from app import models, schemas
from pydantic import EmailStr


#DOMINIO DE USUARIO

def create_user(db: Session, user: schemas.UserCreate):
    #Converte o schema Pydantic para dict e instancia o model ORM
    db_user = models.User(**user.model_dump())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)#Sincroniza o objeto com o estado real do banco
    return db_user


def get_user_by_id(db: Session, user_id: int):
    #Retorna None caso não encontrado (tratamento ocorre na camada de rota)
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_user_by_email(db: Session, email: EmailStr):
    return db.query(models.User).filter(models.User.email == email).first()


def update_user(db: Session, db_user: models.User, user_in: schemas.UserPatch):
    #Atualiza apenas os campos enviados (PATCH semantics)
    update_data = user_in.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, db_user: models.User):
    db.delete(db_user)
    db.commit()
    return db_user


#DOMINIO DE TAREFAS

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.model_dump())

    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.task_id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    #Paginação baseada em offset para controle de volume retornado
    return (
        db.query(models.Task)
        .offset(skip)
        .limit(limit)
        .all()
    )

def update_task(db: Session, db_task: models.Task, task_in: schemas.TaskPatch):
    #Atualização parcial preservando campos não enviados
    update_data = task_in.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_task, field, value)

    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, db_task: models.Task):
    db.delete(db_task)
    db.commit()
    return db_task