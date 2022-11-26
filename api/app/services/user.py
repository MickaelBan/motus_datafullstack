from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas


def get_account_by_id(account_id: str, db: Session) -> models.user:
    record = db.query(models.user).filter(models.user.id == account_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Not Found") 
    return record

def get_account_by_nickname(nickname: str, db: Session) -> models.user:
    record = db.query(models.user).filter(models.user.nickename == nickname).first()
    if not record:
        raise HTTPException(status_code=404, detail="Not Found") 
    return record

def create_account(user: schemas.UserCreation, db: Session) -> models.user:
    record = db.query(models.user).filter(models.user.id == user.id).first()
    if record:
        raise HTTPException(status_code=409, detail="Already exists")
    db_user = models.user(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db_user.id = str(db_user.id)
    return db_user

def delete_user_by_id(account_id: str, db: Session) -> models.user:
    db_user = get_account_by_id(account_id = account_id, db=db)
    db.delete(db_user)
    db.commit()
    return db_user

def delete_user_by_nickname(nickname: str, db: Session) -> models.user:
    db_user = get_account_by_nickname(nickname = nickname, db=db)
    db.delete(db_user)
    db.commit()
    return db_user

def update_account_by_id(account_id, properties,new_value, db: Session) -> models.user:
    user = get_account_by_id(account_id,db)
    for c in user:
        if properties == c.__name__:
            user.c = new_value
            db.commit()

def authenticate_user(usernickname: str, password: str,db: Session):
    user = get_account_by_nickname(usernickname=usernickname,db=db)
    ##print(user)
    if not user:
        return False
    if not user.password == password:
        return False
    return user