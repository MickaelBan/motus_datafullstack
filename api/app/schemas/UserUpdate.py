from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator
from uuid import uuid4
from typing_extensions import Annotated


class UserUpdate(BaseModel):
    id: str
    first_name: Optional[str]
    second_name: Optional[str]
    birth_date: Optional[datetime]
    password: str
    password_new : Optional[str]

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

    @validator('password_new')
    def min_lenght_pw(cls, passw:str):
        if len(password_new) < 4 : 
            raise ValueError("Password size must be greater than 4")
        return passw

    class Config:
        orm_mode = True
