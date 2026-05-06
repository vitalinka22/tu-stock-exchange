# current portfolio of the user, which is updated after each trade
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime
from app.db.database import Base


class Holding(Base):
    __tablename__ = "holdings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    ticker = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    average_buy_price = Column(Float, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow)