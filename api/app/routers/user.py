from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
from schemas import Reponse, UserCreation
from services import user as user_service

router = APIRouter(prefix="/user", tags=["users"])


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
    return Reponse(code=200, status="ok", message="Success get user", result=user).dict()

@router.get("/{nickname}")
async def get_account(nickname: str, db: Session = Depends(models.get_db)):
    user = user_service.get_account_by_nickname(nickname=nickname, db=db)
    return Reponse(code=200, status="ok", message="Success get user", result=user).dict()



@router.get("/login")
async def user_connection(usernickname, password, db: Session = Depends(models.get_db)):
    user = user_service.login_user(usernickname, password)
    return RecursionError(code=200, status="ok", message="user log in successfully", result=user).dict(exclude_none=True)


@router.post("/create")
async def create_account(request: UserCreation, db: Session = Depends(models.get_db)):
    user = user_service.create_account(user=request, db=db)
    return Reponse(code=200, status="ok", message="user created successfully", result=user).dict(exclude_none=True)


@router.post("/update")
async def update_account_by_id(account_id: int, properties: str, new_value: str, db: Session = Depends(models.get_db)):
    user = user_service.update_account_by_id(
        account_id=account_id, field=properties, value=new_value, db=db)
    return Reponse(code=200, status="ok", message="Success update user", result=user).dict(exclude_none=True)




@router.delete("/profil")
async def delete_account_by_id(account_id: int, db: Session = Depends(models.get_db)):
    user_service.delete_user_by_id(account_id=account_id, db=db)
    return Reponse(code=200, status="ok", message="user deleted successfully").dict(exclude_none=True)


@router.delete("/profil")
async def delete_account_by_nickname(nickname: str, db: Session = Depends(models.get_db)):
    user_service.delete_user_by_nickname(nickname=nickname, db=db)
    return Reponse(code=200, status="ok", message="user created successfully").dict(exclude_none=True)
