# Snapshot task to record daily net worth of users

from datetime import datetime, timedelta
from app import models
from app.db import database
from app.services.stock_price import get_current_price
from sqlalchemy.orm import Session
import redis
from app.services.redis_client import redis_client
from app.core.config import settings
from app.utils.logger import logger

def create_daily_snapshot():
    db = database.SessionLocal()
    try:
        users = db.query(models.User).filter(
            models.User.is_bankrupt == False
        ).all()
        
        if not users:
            logger.info("No active users found for snapshot")
            return
            
        for user in users:
            today = datetime.utcnow().date()
            existing = db.query(models.NetWorthHistory).filter(
                models.NetWorthHistory.user_id == user.id,
                models.NetWorthHistory.timestamp >= datetime.combine(today, datetime.min.time()),
                models.NetWorthHistory.timestamp < datetime.combine(today + timedelta(days=1), datetime.min.time())
            ).first()

            if existing:
                logger.debug(f"Snapshot already exists for user {user.id} today")
                continue

            net_worth = calculate_net_worth(db, user.id, redis_client)
            
            snapshot = models.NetWorthHistory(
                user_id=user.id,
                net_worth=net_worth,
                timestamp=datetime.utcnow()
            )
            db.add(snapshot)
            logger.info(f"Created snapshot for user {user.id}: ${net_worth:.2f}")
        
        db.commit()
        logger.info(f"Created {len(users)} net worth snapshots")
        
    except Exception as e:
        logger.error(f"Error creating net worth snapshots: {str(e)}", exc_info=True)
        db.rollback()
    finally:
        db.close()

def calculate_net_worth(db: Session, user_id: int, redis: redis.Redis) -> float:
    """Calculate current net worth (cash + holdings value)"""
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return 0.0

    holdings = db.query(models.Holding).filter(models.Holding.user_id == user_id).all()
    holdings_value = 0.0
    
    for holding in holdings:
        current_price = get_current_price(holding.ticker)
        if current_price is not None:
            holdings_value += holding.quantity * current_price

    return round(user.balance + holdings_value, 2)