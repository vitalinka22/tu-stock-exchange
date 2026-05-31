#!/usr/bin/env python3
import os
import time
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

def wait_for_db():
    """Wait for the database to be ready before proceeding"""
    max_attempts = 30
    attempt = 0
    
    while attempt < max_attempts:
        try:
            engine = create_engine(settings.database_url)
            connection = engine.connect()
            connection.close()
            print("Database is ready")
            return True
        except Exception as e:
            print(f"Database not ready yet (attempt {attempt + 1}/{max_attempts}): {str(e)}")
            attempt += 1
            time.sleep(2)
    
    raise Exception("Database connection timed out")

def populate_data():
    """Populate the database with mock data"""
    try:
        # Create database engine
        engine = create_engine(settings.database_url)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        
        db = SessionLocal()
        try:
            # Insert users
            users = [
                (1, 'trader_john', 'john@example.com', 15000.50, False, '2023-01-15 10:30:00'),
                (2, 'finance_wiz', 'wiz@example.com', 12500.75, False, '2023-01-16 14:22:00'),
                (3, 'market_guru', 'guru@example.com', 9800.25, False, '2023-01-18 09:15:00'),
                (4, 'stock_master', 'master@example.com', 14500.00, False, '2023-01-20 16:45:00'),
                (5, 'crypto_bull', 'bull@example.com', 10000.00, False, '2023-01-22 11:30:00'),
                (6, 'value_investor', 'value@example.com', 11200.50, False, '2023-01-25 13:20:00')
            ]
            
            db.execute(text("""
                INSERT INTO users (id, username, email, balance, is_bankrupt, registered_at)
                VALUES (:id, :username, :email, :balance, :is_bankrupt, :registered_at)
            """), users)
            
            # Insert holdings
            holdings = [
                (1, 'AAPL', 50, 145.25, '2023-05-30 09:15:00'),
                (1, 'TSLA', 25, 200.50, '2023-05-30 14:30:00'),
                (1, 'MSFT', 30, 285.00, '2023-05-30 11:45:00'),
                (2, 'GOOGL', 15, 2750.00, '2023-05-30 10:20:00'),
                (2, 'AMZN', 20, 3500.00, '2023-05-30 13:15:00'),
                (2, 'NFLX', 10, 320.00, '2023-05-30 15:40:00'),
                (3, 'AAPL', 40, 150.00, '2023-05-30 08:30:00'),
                (3, 'TSLA', 15, 210.00, '2023-05-30 12:10:00'),
                (3, 'NVDA', 5, 420.00, '2023-05-30 16:25:00'),
                (4, 'MSFT', 25, 280.00, '2023-05-30 09:45:00'),
                (4, 'AMZN', 10, 3450.00, '2023-05-30 14:20:00'),
                (4, 'GOOGL', 10, 2700.00, '2023-05-30 16:30:00'),
                (5, 'BTC', 0.5, 28000.00, '2023-05-30 11:15:00'),
                (5, 'TSLA', 30, 195.00, '2023-05-30 13:45:00'),
                (5, 'ETH', 5, 1800.00, '2023-05-30 15:10:00'),
                (6, 'AAPL', 35, 148.50, '2023-05-30 10:05:00'),
                (6, 'MSFT', 20, 282.00, '2023-05-30 12:30:00'),
                (6, 'JPM', 25, 145.00, '2023-05-30 14:55:00')
            ]
            
            db.execute(text("""
                INSERT INTO holdings (user_id, ticker, quantity, average_buy_price, updated_at)
                VALUES (:user_id, :ticker, :quantity, :average_buy_price, :updated_at)
            """), holdings)
            
            # Insert trades
            trades = [
                (1, 1, 'AAPL', 'buy', 50, 145.25, 7262.50, '2023-05-30 09:15:00'),
                (2, 1, 'TSLA', 'buy', 25, 200.50, 5012.50, '2023-05-30 14:30:00'),
                (3, 1, 'MSFT', 'buy', 30, 285.00, 8550.00, '2023-05-30 11:45:00'),
                (4, 2, 'GOOGL', 'buy', 15, 2750.00, 41250.00, '2023-05-30 10:20:00'),
                (5, 2, 'AMZN', 'buy', 20, 3500.00, 70000.00, '2023-05-30 13:15:00'),
                (6, 2, 'NFLX', 'buy', 10, 320.00, 3200.00, '2023-05-30 15:40:00'),
                (7, 3, 'AAPL', 'buy', 40, 150.00, 6000.00, '2023-05-30 08:30:00'),
                (8, 3, 'TSLA', 'buy', 15, 210.00, 3150.00, '2023-05-30 12:10:00'),
                (9, 3, 'NVDA', 'buy', 5, 420.00, 2100.00, '2023-05-30 16:25:00'),
                (10, 4, 'MSFT', 'buy', 25, 280.00, 7000.00, '2023-05-30 09:45:00'),
                (11, 4, 'AMZN', 'buy', 10, 3450.00, 34500.00, '2023-05-30 14:20:00'),
                (12, 4, 'GOOGL', 'buy', 10, 2700.00, 27000.00, '2023-05-30 16:30:00'),
                (13, 5, 'BTC', 'buy', 0.5, 28000.00, 14000.00, '2023-05-30 11:15:00'),
                (14, 5, 'TSLA', 'buy', 30, 195.00, 5850.00, '2023-05-30 13:45:00'),
                (15, 5, 'ETH', 'buy', 5, 1800.00, 9000.00, '2023-05-30 15:10:00'),
                (16, 6, 'AAPL', 'buy', 35, 148.50, 5197.50, '2023-05-30 10:05:00'),
                (17, 6, 'MSFT', 'buy', 20, 282.00, 5640.00, '2023-05-30 12:30:00'),
                (18, 6, 'JPM', 'buy', 25, 145.00, 3625.00, '2023-05-30 14:55:00')
            ]
            
            db.execute(text("""
                INSERT INTO trades (id, user_id, ticker, trade_type, quantity, price, total_value, timestamp)
                VALUES (:id, :user_id, :ticker, :trade_type, :quantity, :price, :total_value, :timestamp)
            """), trades)
            
            # Insert net worth history
            net_worth = [
                (1, 1, 15000.50, '2023-05-01 00:00:00'),
                (2, 1, 15325.75, '2023-05-02 00:00:00'),
                (3, 1, 15680.25, '2023-05-03 00:00:00'),
                (4, 1, 16025.50, '2023-05-04 00:00:00'),
                (5, 1, 15875.25, '2023-05-05 00:00:00'),
                (6, 1, 16125.75, '2023-05-06 00:00:00'),
                (7, 1, 16350.00, '2023-05-07 00:00:00'),
                (8, 1, 16500.25, '2023-05-08 00:00:00'),
                (9, 1, 16725.50, '2023-05-09 00:00:00'),
                (10, 1, 17000.75, '2023-05-10 00:00:00'),
                (11, 1, 17250.00, '2023-05-11 00:00:00'),
                (12, 1, 17500.25, '2023-05-12 00:00:00'),
                (13, 1, 17750.50, '2023-05-13 00:00:00'),
                (14, 1, 18000.75, '2023-05-14 00:00:00'),
                (15, 1, 18250.00, '2023-05-15 00:00:00'),
                (16, 1, 18500.25, '2023-05-16 00:00:00'),
                (17, 1, 18750.50, '2023-05-17 00:00:00'),
                (18, 1, 19000.75, '2023-05-18 00:00:00'),
                (19, 1, 19250.00, '2023-05-19 00:00:00'),
                (20, 1, 19500.25, '2023-05-20 00:00:00'),
                (21, 1, 19750.50, '2023-05-21 00:00:00'),
                (22, 1, 20000.75, '2023-05-22 00:00:00'),
                (23, 1, 20250.00, '2023-05-23 00:00:00'),
                (24, 1, 20500.25, '2023-05-24 00:00:00'),
                (25, 1, 20750.50, '2023-05-25 00:00:00'),
                (26, 1, 21000.75, '2023-05-26 00:00:00'),
                (27, 1, 21250.00, '2023-05-27 00:00:00'),
                (28, 1, 21500.25, '2023-05-28 00:00:00'),
                (29, 1, 21750.50, '2023-05-29 00:00:00'),
                (30, 1, 22000.75, '2023-05-30 00:00:00')
            ]
            
            db.execute(text("""
                INSERT INTO net_worth_history (id, user_id, net_worth, timestamp)
                VALUES (:id, :user_id, :net_worth, :timestamp)
            """), net_worth)
            
            # Insert auto trades
            auto_trades = [
                (1, 1, 'TSLA', 'buy', 190.00, 10, True, '2023-05-20 09:15:00'),
                (2, 1, 'AAPL', 'sell', 160.00, 5, True, '2023-05-22 14:30:00'),
                (3, 2, 'GOOGL', 'buy', 2700.00, 5, True, '2023-05-21 11:45:00'),
                (4, 2, 'AMZN', 'sell', 3600.00, 10, True, '2023-05-23 10:20:00'),
                (5, 3, 'AAPL', 'buy', 140.00, 15, True, '2023-05-19 13:15:00'),
                (6, 3, 'TSLA', 'sell', 220.00, 5, True, '2023-05-24 15:40:00'),
                (7, 4, 'MSFT', 'buy', 275.00, 10, True, '2023-05-20 09:45:00'),
                (8, 4, 'AMZN', 'sell', 3500.00, 5, True, '2023-05-22 14:20:00'),
                (9, 5, 'BTC', 'buy', 27000.00, 0.25, True, '2023-05-21 11:15:00'),
                (10, 5, 'TSLA', 'sell', 205.00, 15, True, '2023-05-23 13:45:00'),
                (11, 6, 'AAPL', 'buy', 145.00, 20, True, '2023-05-18 10:05:00'),
                (12, 6, 'MSFT', 'sell', 290.00, 10, True, '2023-05-20 12:30:00')
            ]
            
            db.execute(text("""
                INSERT INTO auto_trades (id, user_id, ticker, trade_type, target_price, quantity, is_active, created_at)
                VALUES (:id, :user_id, :ticker, :trade_type, :target_price, :quantity, :is_active, :created_at)
            """), auto_trades)
            
            db.commit()
            print("Data populated successfully!")
            
        except Exception as e:
            print(f"Error populating data: {str(e)}")
            db.rollback()
            raise e
        finally:
            db.close()
    except Exception as e:
        print(f"Failed to connect to database: {str(e)}")
        raise e

if __name__ == "__main__":
    # Wait for database to be ready
    wait_for_db()
    
    # Populate data
    populate_data()