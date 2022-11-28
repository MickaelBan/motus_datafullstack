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
        return None
    return user

#Get user whith his nickname
def get_account_by_nickname(nickname: str, db: Session) -> models.user:
    user = db.query(models.user).filter(models.user.nickname == nickname).first()
    if not user:
        return user
    return user

#Creat a user account
def create_account(user: UserCreation, db: Session) -> int:
    _user = db.query(models.user).filter(models.user.nickname == user.nickname).first()
    if _user:
        return 0
    _user_ = db.query(models.user).filter(models.user.email == user.email).first()
    if _user_:
        return 2
    db_user = models.user(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return 1

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
def update(userID:str,request: UserUpdate, db: Session) -> int:
    user = get_account_by_id(userID, db)
    new_data = request.dict(exclude_unset=True)
    for key, value in new_data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return 1

#log in a user
def login_user(identifant: UserLogin, db: Session) -> int:
    user = get_account_by_nickname(nickname=identifant.nickname, db=db)
    print(user)
    if not user:
        return 0
    if  user.password != identifant.password:
        return 2
    user.status = 1  
    db.commit()
    db.refresh(user)
    return 1

def logout_user(nickname, db: Session) -> int:
    user = get_account_by_nickname(nickname=nickname, db=db)
    if not user:
        return 0
    if user.status != 1:
        return 2
    user.status = 0  
    db.commit()
    db.refresh(user)
    return 1