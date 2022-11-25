from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models,schemas
from services import user as user_service
 
router = APIRouter(prefix="/account", tags=["users"])

@router.get("/")
async def root():
    return {"Health":"account"}


@router.get("/{account_id}")
async def get_account(account_id: str, db: Session = Depends(models.get_db)):
    return user_service.get_account_by_id(account_id = account_id, db = db)

@router.post("/create_account")
async def create_account(user: schemas.UserCreation, db: Session = Depends(models.get_db)):
    return user_service.create_account(user = user, db = db)

@router.delete("/{account_id}")
async def delete_account_by_id(account_id, db: Session = Depends(models.get_db)):
    return user_service.delete_user_by_id(account_id = account_id, db = db)


@router.put("/{account_id}/{properties}/{new_alue}")
async def update_account_by_id(account_id, properties,new_value, db: Session = Depends(models.get_db)):
    return user_service.update_by_id(account_id = account_id, field = properties,value = new_value, db = db)

