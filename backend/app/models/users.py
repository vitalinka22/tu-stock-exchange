from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    
    email = Column(String, unique=True)
    password_hash = Column(String)
    balance = Column(Float, default=10000) # initial balance for new users
    is_bankrupt = Column(Boolean, default=False)
    registered_at = Column(DateTime, default=datetime.utcnow)
    
    holdings = relationship("Holding", back_populates="user")