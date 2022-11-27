from sqlalchemy import Column, String, Integer , DateTime, CheckConstraint, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from .database import BaseSQL


class User(BaseSQL):
    __tablename__ = "user"
    __table_arg__ = (
        CheckConstraint('length(first_name)<40'),
        CheckConstraint('length(second_name)<40'),
        CheckConstraint('length(password)>6'),
        CheckConstraint('length(first_name)>0'),
        CheckConstraint('length(second_name)>0')
    )
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False,unique=True)
    nickname = Column(String(),ForeignKey("user.nickname"), nullable=False,unique=True )
    first_name = Column(String())
    second_name = Column(String())
    created_at = Column(DateTime(),nullable = False)
    password = Column(String(),nullable = False) 
    email = Column(String(),ForeignKey("user.email"), nullable=False,unique=True)
    best_score = Column(Integer())
    status = Column(Integer())

    
    

