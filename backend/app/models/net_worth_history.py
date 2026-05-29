# net worth = balance + current value of holdings
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from datetime import datetime
from app.db.database import Base


class NetWorthHistory(Base):
    __tablename__ = "net_worth_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    net_worth = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)