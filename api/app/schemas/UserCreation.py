from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator
from uuid import uuid4
from typing_extensions import Annotated
import re

class UserCreation(BaseModel):
    id: Annotated[str, Field(default_factory=lambda: uuid4().hex)]
    first_name: str
    second_name: Optional[str]
    nickname: unic[str]
    password: str
    created_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]
    email: str
    best_score: Optional[int]

    @validator('first_name')
    def max_lenght_fn(cls, fn:str):
        if len(fn) > 40 : 
            raise ValueError("First name size must be less than 40")
        return fn
    
    @validator('second_name')
    def max_lenght_sn(cls, sn:str):
        if len(sn) > 40 : 
            raise ValueError("Second name size must be less than 40")
        return sn

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
    
    
    class Config:
        orm_mode = True
