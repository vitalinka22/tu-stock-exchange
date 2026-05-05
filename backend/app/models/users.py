from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password_hash = Column(String)
    balance = Column(Float, default=10000)
    is_defaulted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)