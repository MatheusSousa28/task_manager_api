from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.database import get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=schemas.UserResponse, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return crud.create_user(db, user)


@router.get("/{user_id}", response_model=schemas.UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user


@router.get("/", response_model=schemas.UserResponse)
def get_user_by_email(user_email: EmailStr, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user_email)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user


@router.patch("/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user_in: schemas.UserPatch, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return crud.update_user(db, db_user, user_in)


@router.delete("/{user_id}", response_model=schemas.UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return crud.delete_user(db, db_user)
