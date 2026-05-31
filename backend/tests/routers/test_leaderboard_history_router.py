from datetime import datetime, timedelta
import pytest

def test_leaderboard_history(client, db):
    """Test the leaderboard history endpoint returns historical data correctly"""
    # Set up test users
    users = [
        {"id": 1, "username": "user1", "email": "user1@example.com", "password_hash": "hash1", "balance": 10000.0, "is_bankrupt": False},
        {"id": 2, "username": "user2", "email": "user2@example.com", "password_hash": "hash2", "balance": 5000.0, "is_bankrupt": False},
        {"id": 3, "username": "user3", "email": "user3@example.com", "password_hash": "hash3", "balance": 2000.0, "is_bankrupt": False},
    ]
    
    for user in users:
        db.execute(
            "INSERT INTO users (id, username, email, password_hash, balance, is_bankrupt, registered_at) "
            "VALUES (:id, :username, :email, :password_hash, :balance, :is_bankrupt, NOW())",
            user
        )
    
    db.commit()
    
    # Create net worth history records at different timestamps
    now = datetime.utcnow()
    day3 = now - timedelta(days=3)
    day2 = now - timedelta(days=2)
    day1 = now - timedelta(days=1)
    
    # Day 3 data (oldest)
    net_worth_history = [
        {"user_id": 1, "net_worth": 10000.0, "timestamp": day3},
        {"user_id": 2, "net_worth": 5000.0, "timestamp": day3},
        {"user_id": 3, "net_worth": 2000.0, "timestamp": day3},
    ]
    
    # Day 2 data
    net_worth_history += [
        {"user_id": 1, "net_worth": 12000.0, "timestamp": day2},
        {"user_id": 2, "net_worth": 4000.0, "timestamp": day2},
        {"user_id": 3, "net_worth": 3000.0, "timestamp": day2},
    ]
    
    # Day 1 data (most recent)
    net_worth_history += [
        {"user_id": 1, "net_worth": 11000.0, "timestamp": day1},
        {"user_id": 2, "net_worth": 6000.0, "timestamp": day1},
        {"user_id": 3, "net_worth": 2500.0, "timestamp": day1},
    ]
    
    # Insert net worth history
    for record in net_worth_history:
        db.execute(
            "INSERT INTO net_worth_history (user_id, net_worth, timestamp) "
            "VALUES (:user_id, :net_worth, :timestamp)",
            record
        )
    
    db.commit()
    
    # Call leaderboard history endpoint
    response = client.get("/api/leaderboard/history")
    
    # Verify response
    assert response.status_code == 200
    data = response.json()
    
    # Should return 3 history entries (one for each day)
    assert len(data) == 3
    
    # Verify timestamps are in chronological order (oldest first)
    assert data[0]["timestamp"] == day3.isoformat()
    assert data[1]["timestamp"] == day2.isoformat()
    assert data[2]["timestamp"] == day1.isoformat()
    
    # Verify rankings for day 3 (oldest)
    assert data[0]["rankings"][0]["username"] == "user1"
    assert data[0]["rankings"][0]["portfolio_value"] == 10000.0
    assert data[0]["rankings"][0]["rank"] == 1
    
    assert data[0]["rankings"][1]["username"] == "user2"
    assert data[0]["rankings"][1]["portfolio_value"] == 5000.0
    assert data[0]["rankings"][1]["rank"] == 2
    
    assert data[0]["rankings"][2]["username"] == "user3"
    assert data[0]["rankings"][2]["portfolio_value"] == 2000.0
    assert data[0]["rankings"][2]["rank"] == 3
    
    # Verify rankings for day 2
    assert data[1]["rankings"][0]["username"] == "user1"
    assert data[1]["rankings"][0]["portfolio_value"] == 12000.0
    assert data[1]["rankings"][0]["rank"] == 1
    
    assert data[1]["rankings"][1]["username"] == "user3"
    assert data[1]["rankings"][1]["portfolio_value"] == 3000.0
    assert data[1]["rankings"][1]["rank"] == 2
    
    assert data[1]["rankings"][2]["username"] == "user2"
    assert data[1]["rankings"][2]["portfolio_value"] == 4000.0
    assert data[1]["rankings"][2]["rank"] == 3
    
    # Verify rankings for day 1 (most recent)
    assert data[2]["rankings"][0]["username"] == "user1"
    assert data[2]["rankings"][0]["portfolio_value"] == 11000.0
    assert data[2]["rankings"][0]["rank"] == 1
    
    assert data[2]["rankings"][1]["username"] == "user2"
    assert data[2]["rankings"][1]["portfolio_value"] == 6000.0
    assert data[2]["rankings"][1]["rank"] == 2
    
    assert data[2]["rankings"][2]["username"] == "user3"
    assert data[2]["rankings"][2]["portfolio_value"] == 2500.0
    assert data[2]["rankings"][2]["rank"] == 3

def test_leaderboard_history_days_parameter(client, db):
    """Test the leaderboard history endpoint correctly filters by days parameter"""
    # Set up test users
    users = [
        {"id": 1, "username": "user1", "email": "user1@example.com", "password_hash": "hash1", "balance": 10000.0, "is_bankrupt": False},
        {"id": 2, "username": "user2", "email": "user2@example.com", "password_hash": "hash2", "balance": 5000.0, "is_bankrupt": False},
    ]
    
    for user in users:
        db.execute(
            "INSERT INTO users (id, username, email, password_hash, balance, is_bankrupt, registered_at) "
            "VALUES (:id, :username, :email, :password_hash, :balance, :is_bankrupt, NOW())",
            user
        )
    
    db.commit()
    
    # Create net worth history for multiple days
    now = datetime.utcnow()
    day5 = now - timedelta(days=5)
    day4 = now - timedelta(days=4)
    day3 = now - timedelta(days=3)
    day2 = now - timedelta(days=2)
    day1 = now - timedelta(days=1)
    
    net_worth_history = [
        {"user_id": 1, "net_worth": 10000.0, "timestamp": day5},
        {"user_id": 2, "net_worth": 5000.0, "timestamp": day5},
        {"user_id": 1, "net_worth": 11000.0, "timestamp": day4},
        {"user_id": 2, "net_worth": 4500.0, "timestamp": day4},
        {"user_id": 1, "net_worth": 12000.0, "timestamp": day3},
        {"user_id": 2, "net_worth": 4000.0, "timestamp": day3},
        {"user_id": 1, "net_worth": 13000.0, "timestamp": day2},
        {"user_id": 2, "net_worth": 3500.0, "timestamp": day2},
        {"user_id": 1, "net_worth": 14000.0, "timestamp": day1},
        {"user_id": 2, "net_worth": 3000.0, "timestamp": day1},
    ]
    
    # Insert net worth history
    for record in net_worth_history:
        db.execute(
            "INSERT INTO net_worth_history (user_id, net_worth, timestamp) "
            "VALUES (:user_id, :net_worth, :timestamp)",
            record
        )
    
    db.commit()
    
    # Test with days=3 parameter
    response = client.get("/api/leaderboard/history?days=3")
    
    # Verify response
    assert response.status_code == 200
    data = response.json()
    
    # Should return only 3 history entries (days 3, 2, and 1)
    assert len(data) == 3
    
    # Verify timestamps are in chronological order (oldest first)
    assert data[0]["timestamp"] == day3.isoformat()
    assert data[1]["timestamp"] == day2.isoformat()
    assert data[2]["timestamp"] == day1.isoformat()

def test_leaderboard_history_empty_data(client, db):
    """Test the leaderboard history endpoint returns empty list when no data exists"""
    # Call leaderboard history endpoint
    response = client.get("/api/leaderboard/history")
    
    # Verify response
    assert response.status_code == 200
    data = response.json()
    
    # Should return empty list
    assert len(data) == 0

def test_leaderboard_history_more_than_10_users(client, db):
    """Test the leaderboard history endpoint returns only top 10 users"""
    # Set up 15 test users
    users = []
    for i in range(1, 16):
        users.append({
            "id": i,
            "username": f"user{i}",
            "email": f"user{i}@example.com",
            "password_hash": f"hash{i}",
            "balance": (16 - i) * 1000.0,
            "is_bankrupt": False
        })
    
    for user in users:
        db.execute(
            "INSERT INTO users (id, username, email, password_hash, balance, is_bankrupt, registered_at) "
            "VALUES (:id, :username, :email, :password_hash, :balance, :is_bankrupt, NOW())",
            user
        )
    
    db.commit()
    
    # Create net worth history for one timestamp
    now = datetime.utcnow()
    net_worth_history = []
    for i in range(1, 16):
        net_worth_history.append({
            "user_id": i,
            "net_worth": (16 - i) * 1000.0,
            "timestamp": now
        })
    
    # Insert net worth history
    for record in net_worth_history:
        db.execute(
            "INSERT INTO net_worth_history (user_id, net_worth, timestamp) "
            "VALUES (:user_id, :net_worth, :timestamp)",
            record
        )
    
    db.commit()
    
    # Call leaderboard history endpoint
    response = client.get("/api/leaderboard/history")
    
    # Verify response
    assert response.status_code == 200
    data = response.json()
    
    # Should return 1 history entry
    assert len(data) == 1
    
    # Should return only 10 rankings (top 10 users)
    assert len(data[0]["rankings"]) == 10
    
    # Verify the top 10 users are correctly ranked
    for i, ranking in enumerate(data[0]["rankings"], 1):
        assert ranking["rank"] == i
        assert ranking["username"] == f"user{i}"
        assert ranking["portfolio_value"] == (16 - i) * 1000.0

def test_leaderboard_history_with_bankrupt_user(client, db):
    """Test the leaderboard history endpoint excludes bankrupt users"""
    # Set up test users
    users = [
        {"id": 1, "username": "user1", "email": "user1@example.com", "password_hash": "hash1", "balance": 10000.0, "is_bankrupt": False},
        {"id": 2, "username": "user2", "email": "user2@example.com", "password_hash": "hash2", "balance": 5000.0, "is_bankrupt": False},
        {"id": 3, "username": "bankrupt_user", "email": "bankrupt@example.com", "password_hash": "hash3", "balance": 0.0, "is_bankrupt": True},
    ]
    
    for user in users:
        db.execute(
            "INSERT INTO users (id, username, email, password_hash, balance, is_bankrupt, registered_at) "
            "VALUES (:id, :username, :email, :password_hash, :balance, :is_bankrupt, NOW())",
            user
        )
    
    db.commit()
    
    # Create net worth history
    now = datetime.utcnow()
    net_worth_history = [
        {"user_id": 1, "net_worth": 10000.0, "timestamp": now},
        {"user_id": 2, "net_worth": 5000.0, "timestamp": now},
        {"user_id": 3, "net_worth": 0.0, "timestamp": now},
    ]
    
    # Insert net worth history
    for record in net_worth_history:
        db.execute(
            "INSERT INTO net_worth_history (user_id, net_worth, timestamp) "
            "VALUES (:user_id, :net_worth, :timestamp)",
            record
        )
    
    db.commit()
    
    # Call leaderboard history endpoint
    response = client.get("/api/leaderboard/history")
    
    # Verify response
    assert response.status_code == 200
    data = response.json()
    
    # Should return 1 history entry
    assert len(data) == 1
    
    # Should return only 2 rankings (bankrupt user excluded)
    assert len(data[0]["rankings"]) == 2
    
    # Verify the bankrupt user is not included
    usernames = [item["username"] for item in data[0]["rankings"]]
    assert "bankrupt_user" not in usernames