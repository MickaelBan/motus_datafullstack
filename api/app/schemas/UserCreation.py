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
    
    class Config:
        orm_mode = True
