from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)  # Primary Key
    name = Column(String)                               # Student Name
    email = Column(String, unique=True, index=True)     # Unique Email
    age = Column(Integer)                               # Student Age
    course = Column(String)                             # Enrolled Course
