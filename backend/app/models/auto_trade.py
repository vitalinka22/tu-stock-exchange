# stores automatic trading rules for users. 
# Each rule specifies a stock ticker, a target price, and an action (buy or sell). 

from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from datetime import datetime
from app.db.database import Base


class AutoTrade(Base):
    __tablename__ = "auto_trades"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    ticker = Column(String, nullable=False)
    trade_type = Column(String, nullable=False)  # buy or sell
    target_price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)