from sqlalchemy import Column, Integer, String, Float
from src.db.database import Base

class User(Base):
    __tablename__='users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    password = Column(String, nullable=False)

