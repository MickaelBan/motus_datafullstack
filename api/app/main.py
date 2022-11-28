from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import BaseSQL,engine
from routers import UserRouter,WordRouter
from typing import Optional


app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)
origins = [
    "http://localhost",    
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(UserRouter)
app.include_router(WordRouter)

@app.get("/")
def read_root():
    return {"api": "root"} 



@app.on_event("startup")
async def startup_event():
    BaseSQL.metadata.create_all(bind=engine)


