from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator
from uuid import uuid4
from typing_extensions import Annotated
import re

class UserCreation(BaseModel):
    id: Annotated[str, Field(default_factory=lambda: uuid4().hex)]
    nickname: str
    first_name: str
    second_name: Optional[str]    
    created_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]
    password: str
    email: str
    best_score: Optional[int]
    status: Annotated[int, Field(default_factory=lambda: 0)]

    @validator('first_name')
    def check_fn(cls, fn:str):
        if len(fn) < 1 :
            raise ValueError("First name can't be null")
        if len(fn) > 40 : 
            raise ValueError("First name size must be less than 40")
        return fn
    
    @validator('second_name')
    def chek_sn(cls, sn:str):
        if len(sn) > 40 : 
            raise ValueError("Second name size must be less than 40")
        return sn

    @validator('nickname')
    def check_nn(cls, nn:str):
        if len(nn)<1:
            raise ValueError("First name can't be null")
        if len(nn) > 40 : 
            raise ValueError("First name size must be less than 40")
        return nn
     
    @validator('password')
    def check_password(passw:str):
        if not re.search(r"[\d]+",passw):
            raise ValueError("Password must contain at least one digit.")
        if not re.search(r"[A-Z]+", passw):
            raise ValueError("Password must contain at least one capital letter.")
        if not re.search(r"[a-z]+", passw):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r"[\/.*@&$€()\[\]]",passw):
            raise ValueError("Password must contain at least one special character: /.*@&$€()\[\]")
        if len(passw) < 6 : 
            raise ValueError("Password size must be greater than 6")
        if re.search(r"[!;,:\\,ù¨^#]",passw):
            raise ValueError("Password contain an illegal character: !;,:\\,ù¨^#")
        return passw
    
    class Config:
        orm_mode = True
