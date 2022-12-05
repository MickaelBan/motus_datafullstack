from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
from schemas import Reponse, UserCreation, UserUpdate, UserLogin
from services import word as word_service

router = APIRouter(prefix="/word", tags=["users"])



@router.get("/health")
async def health():
    return Reponse(code=200, status="ok", message="Success").dict(exclude_none=True)


@router.get("/")
async def get_word():
    word = word_service.get_word()
    if not word :
        return Reponse(code=100, status="bad", message="any word",result=word).dict()
    return Reponse(code=200, status="ok", message="Success",result=word).dict()
