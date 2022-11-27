from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
from schemas import Reponse, UserCreation, UserUpdate, UserLogin
from services import user as user_service
from typing import List

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/health")
async def health():
    return Reponse(code=200, status="ok", message="Success").dict(exclude_none=True)


@router.get("/")
async def get_users(db: Session = Depends(models.get_db)):
    users = user_service.get_users(db=db)
    return Reponse(code=200, status="ok", message="Success",result=users).dict()


@router.get("/id_{account_id}")
async def get_account(account_id: str, db: Session = Depends(models.get_db)):
    user = user_service.get_account_by_id(account_id=account_id, db=db)
    if user == None:
        return Reponse(code=100, status="bad", message="user not found").dict()
    return Reponse(code=200, status="ok", message="Success get user").dict()

@router.get("/{nickname}")
async def get_account(nickname: str, db: Session = Depends(models.get_db)):
    user = user_service.get_account_by_nickname(nickname=nickname, db=db)
    if user == None:
        return Reponse(code=100, status="bad", message="user not found").dict()
    return Reponse(code=200, status="ok", message="Success get user", result=user).dict()



@router.post("/login")
async def login_user(identifants: UserLogin, db: Session = Depends(models.get_db)):
    login = user_service.login_user(identifant = identifants, db=db)
    if login == 1 :
        user = user_service.get_account_by_nickname(nickname=identifants.nickname,db=db)
        return Reponse(code=200, status="ok", message="user login successfully", result=user).dict(exclude_none=True)
    elif login == 0 :
        return Reponse(code=100, status="bad", message="incorrecte nickname").dict(exclude_none=True)
    elif login == 2 :
        return Reponse(code=100, status="bad", message="incorrecte password").dict(exclude_none=True)
         


@router.post("/logout/{nickename}")
async def logout_user(nickename: str, db: Session = Depends(models.get_db)):
    user = user_service.logout_user(nickname = nickename, db=db)
    if user == 1 :
        return Reponse(code=200, status="ok", message="user logout successfully").dict(exclude_none=True)
    elif user == 0 :
        return Reponse(code=100, status="bad", message="incorrecte nickname").dict(exclude_none=True)
    elif user == 2 :
        return Reponse(code=100, status="bad", message="use not connected").dict(exclude_none=True)
      

@router.post("/create")
async def create_account(request: UserCreation, db: Session = Depends(models.get_db)):
    user = user_service.create_account(user=request, db=db)
    if user == 1 :
        return Reponse(code=200, status="ok", message="user created successfully", result=user).dict(exclude_none=True)
    elif user == 0 :
        return Reponse(code=100, status="bad", message="nickname already exist", result=user).dict(exclude_none=True)
    elif user == 2 :
        return Reponse(code=101, status="bad", message="password already exist", result=user).dict(exclude_none=True)
    

@router.put("/id_{account_id}/update")
async def update_account_by_id(account_id: str, request: UserUpdate, db: Session = Depends(models.get_db) ):
    user = user_service.update(userID=account_id, request=request, db=db)
    if user == 1 :
        return Reponse(code=200, status="ok", message="Success update user", result=user).dict(exclude_none=True)
    return Reponse(code=100, status="bad", message="unknwow",result=user).dict()




@router.delete("/id_{account_id}")
async def delete_account_by_id(account_id: str, db: Session = Depends(models.get_db)):
    user_service.delete_user_by_id(account_id=account_id, db=db)
    return Reponse(code=200, status="ok", message="user deleted successfully").dict(exclude_none=True)


@router.delete("/{nickname}")
async def delete_account_by_nickname(nickname: str, db: Session = Depends(models.get_db)):
    user_service.delete_user_by_nickname(nickname=nickname, db=db)
    return Reponse(code=200, status="ok", message="user deleted successfully").dict(exclude_none=True)
