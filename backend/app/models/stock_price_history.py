# stores the history of stock prices for each stock, with timestamps. This allows us to track how the price of a stock has changed over time, which is essential for analyzing trends and making informed trading decisions.

from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.database import Base


class StockPriceHistory(Base):
    __tablename__ = "stock_price_history"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, nullable=False, index=True)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)