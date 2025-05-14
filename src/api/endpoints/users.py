from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.dependency import get_db
from src import crud, schemas

router=APIRouter()


@router.get("")
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@router.post("")
def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)  

@router.put("/{id}")
def update_users(id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db, id, user)


@router.delete("/{id}")
def delete_users(id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, id)