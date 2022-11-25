from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas


def get_account_by_id(account_id: str, db: Session) -> models.User:
    record = db.query(models.User).filter(models.User.id == account_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Not Found") 
    record.id = str(record.id)
    return record

def create_account(user: schemas.UserCreation, db: Session) -> models.User:
    record = db.query(models.User).filter(models.User.id == user.id).first()
    if record:
        raise HTTPException(status_code=409, detail="Already exists")
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db_user.id = str(db_user.id)
    return db_user

def delete_user_by_id(account_id: str, db: Session) -> models.User:
    db_user = get_account_by_id(post_id=account_id, db=db)
    db.delete(db_user)
    db.commit()
    return db_user


def delete_all_users(db: Session) -> List[models.User]:
    records = db.query(models.User).filter()
    for record in records:
        db.delete(record)
    db.commit()
    return records
