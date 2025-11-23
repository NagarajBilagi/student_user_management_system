
from sqlalchemy import Column, Integer, String
from .db import Base

class Student(Base):
    __tablename__ = "students_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    selected_interest = Column(String(100), nullable=True)


class InterestResource(Base):
    __tablename__ = "interest_resources"

    id = Column(Integer, primary_key=True, index=True)
    interest_tag = Column(String(100), unique=True, nullable=False)
    workshops = Column(String(1000))
    training = Column(String(1000))
    event = Column(String(1000))
