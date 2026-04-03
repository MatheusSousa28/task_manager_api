from fastapi import APIRouter, Depends, HTTPException
from core.database import get_db
import schemas
import crud
from sqlalchemy.orm import Session
from pydantic import EmailStr

router = APIRouter()

@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate ,db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return crud.create_user(db, user)

@router.get("/{user_id}", response_model=schemas.UserResponse)
def get_user_by_id(user_id: int ,db: Session = Depends(get_db)):
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
def update_user(user_in: schemas.UserPatch, user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    updated_user = crud.update_user(db, db_user, user_in)
    return updated_user

@router.delete("/{user_id}", response_model=schemas.UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    deleted_user = crud.delete_user(db, db_user)
    return deleted_user