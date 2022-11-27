
from pydantic import BaseModel

class UserLogin(BaseModel):
    nickname: str   
    password: str

    
    class Config:
        orm_mode = True
