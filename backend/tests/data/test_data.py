from datetime import datetime, timedelta
from typing import List, Dict

def create_leaderboard_test_data(db):
    # [code to create leaderboard test data]
    return db

def create_leaderboard_history_test_data(db):
    # [code to create leaderboard history test data]
    return db

def create_test_users(db) -> List[Dict]:
    """Create test users and return their data"""
    users = [
        {
            "id": 1,
            "username": "user1",
            "email": "user1@example.com",
            "password_hash": "hash1",
            "balance": 10000.0,
            "is_bankrupt": False,
            "registered_at": datetime.utcnow()
        },
        {
            "id": 2,
            "username": "user2",
            "email": "user2@example.com",
            "password_hash": "hash2",
            "balance": 5000.0,
            "is_bankrupt": False,
            "registered_at": datetime.utcnow()
        },
        {
            "id": 3,
            "username": "user3",
            "email": "user3@example.com",
            "password_hash": "hash3",
            "balance": 2000.0,
            "is_bankrupt": False,
            "registered_at": datetime.utcnow()
        },
        {
            "id": 4,
            "username": "user4",
            "email": "user4@example.com",
            "password_hash": "hash4",
            "balance": 4000.0,
            "is_bankrupt": False,
            "registered_at": datetime.utcnow()
        },
        {
            "id": 5,
            "username": "user5",
            "email": "user5@example.com",
            "password_hash": "hash5",
            "balance": 3000.0,
            "is_bankrupt": False,
            "registered_at": datetime.utcnow()
        },
        {
            "id": 6,
            "username": "bankrupt_user",
            "email": "bankrupt@example.com",
            "password_hash": "hash6",
            "balance": 0.0,
            "is_bankrupt": True,
            "registered_at": datetime.utcnow()
        },
    ]
    
    for user in users:
        db.execute(
            """
            INSERT INTO users (id, username, email, password_hash, balance, is_bankrupt, registered_at)
            VALUES (:id, :username, :email, :password_hash, :balance, :is_bankrupt, :registered_at)
            """,
            user
        )
    
    db.commit()
    return users

def create_test_holdings(db, users: List[Dict]):
    """Create test holdings for users"""
    holdings = [
        {"user_id": 1, "ticker": "AAPL", "quantity": 10, "average_buy_price": 150.0, "updated_at": datetime.utcnow()},
        {"user_id": 2, "ticker": "TSLA", "quantity": 5, "average_buy_price": 250.0, "updated_at": datetime.utcnow()},
        {"user_id": 3, "ticker": "MSFT", "quantity": 8, "average_buy_price": 300.0, "updated_at": datetime.utcnow()},
        {"user_id": 1, "ticker": "GOOG", "quantity": 2, "average_buy_price": 1200.0, "updated_at": datetime.utcnow()},
    ]
    
    for holding in holdings:
        db.execute(
            """
            INSERT INTO holdings (user_id, ticker, quantity, average_buy_price, updated_at)
            VALUES (:user_id, :ticker, :quantity, :average_buy_price, :updated_at)
            """,
            holding
        )
    
    db.commit()

def create_test_stock_prices(db):
    """Create test stock prices"""
    stock_prices = [
        {"ticker": "AAPL", "price": 155.0, "timestamp": datetime.utcnow()},
        {"ticker": "TSLA", "price": 260.0, "timestamp": datetime.utcnow()},
        {"ticker": "MSFT", "price": 310.0, "timestamp": datetime.utcnow()},
        {"ticker": "GOOG", "price": 1250.0, "timestamp": datetime.utcnow()},
    ]
    
    for price in stock_prices:
        db.execute(
            """
            INSERT INTO stock_price_history (ticker, price, timestamp)
            VALUES (:ticker, :price, :timestamp)
            """,
            price
        )
    
    db.commit()

def create_test_net_worth_history(db, days: int = 3):
    """Create test net worth history for leaderboard history tests"""
    now = datetime.utcnow()
    users = db.execute("SELECT id FROM users").fetchall()
    
    # Create history for multiple days
    for day in range(days):
        timestamp = now - timedelta(days=day)
        
        for user in users:
            # Calculate net worth based on user id
            base_value = 10000 - (user.id * 1000)
            net_worth = base_value + (day * 500)
            
            db.execute(
                """
                INSERT INTO net_worth_history (user_id, net_worth, timestamp)
                VALUES (:user_id, :net_worth, :timestamp)
                """,
                {
                    "user_id": user.id,
                    "net_worth": net_worth,
                    "timestamp": timestamp
                }
            )
    
    db.commit()

    