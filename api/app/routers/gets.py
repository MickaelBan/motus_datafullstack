from dataclasses import dataclass
from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/gets", tags=["gets"])

@router.get("/date")
async def getDate():
    now = datetime.now()
    strDate = now.strftime("%H:%M:%S")
    return {"Date" : strDate}

@router.get("/")
async def getRouter():
    return {"Health":"I'm in the get router"}
