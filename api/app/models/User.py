from sqlalchemy import Column, String, DateTime, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from .database import BaseSQL


class User(BaseSQL):
    __tablename__ = "users"
    __table_arg__ = (
        CheckConstraint('leght(first_name)<40'),
        CheckConstraint('leght(second_name)<40'),
        CheckConstraint('leght(password)>4')
    )
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    first_name = Column(String())
    second_name = Column(String)
    created_at = Column(DateTime())
    get_at = Column(DateTime())
    password = str 
    
    

