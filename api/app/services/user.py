from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException
import models
from schemas import UserCreation,Reponse,UserUpdate,UserLogin


#Get users
def get_users(db: Session,offset: int=0, limit: int =100 ) -> models.user:
    return db.query(models.user).offset(offset=offset).limit(limit=limit).all()
    
#Get user whith his ID
def get_account_by_id(account_id: str, db: Session) -> models.user:
    user = db.query(models.user).filter(models.user.id == account_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Not Found")
    return user

#Get user whith his nickname
def get_account_by_nickname(nickname: str, db: Session) -> models.user:
    user = db.query(models.user).filter(
        models.user.nickname == nickname).first()
    if not user:
        raise HTTPException(status_code=404, detail="Not Found")
    return user

#Creat a user account
def create_account(user: UserCreation, db: Session) -> models.user:
    _user = db.query(models.user).filter(models.user.nickname == user.nickname).first()
    if _user:
        return Reponse(code=409,status="bad",message="nickname already exists").dict(exclude_none=True)
    _user = db.query(models.user).filter(models.user.email == user.email).first()
    if _user:
        raise HTTPException(status_code=409, detail="email already exists")
    db_user = models.user(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#Delete a user account whith his ID
def delete_user_by_id(account_id: str, db: Session):
    db_user = get_account_by_id(account_id=account_id, db=db)
    db.delete(db_user)
    db.commit()

#Delete a user account whith his nickname
def delete_user_by_nickname(nickname: str, db: Session):
    db_user = get_account_by_nickname(nickname=nickname, db=db)
    db.delete(db_user)
    db.commit()

#Update a user account whith his nickname
def update(userID:str,request: UserUpdate, db: Session) -> models.user:
    user = get_account_by_id(userID, db)
    new_data = request.dict(exclude_unset=True)
    for key, value in new_data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

#log in a user
def login_user(identifant: UserLogin, db: Session) -> models.user:
    user = get_account_by_nickname(nickname=identifant.nickname, db=db)
    if not user:
        raise HTTPException(status_code=409, detail="user ivalid")
    if  user.password != identifant.password:
        raise HTTPException(status_code=409, detail="password invalid")
    return user
