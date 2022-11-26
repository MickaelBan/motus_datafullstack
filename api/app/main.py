from fastapi import FastAPI
from models import BaseSQL,engine
from routers import UserRouter
from typing import Optional


app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)

app.include_router(UserRouter)


@app.get("/")
def read_root():
    return {"api": "root"} 



@app.on_event("startup")
async def startup_event():
    BaseSQL.metadata.create_all(bind=engine)


