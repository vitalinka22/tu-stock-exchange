from datetime import datetime
import pytest

def test_leaderboard(client, setup_leaderboard_test_data):
    """Test the leaderboard endpoint returns users in correct order by portfolio value"""
    # Call leaderboard endpoint
    response = client.get("/api/leaderboard")
    
    # Verify response
    assert response.status_code == 200
    data = response.json()
    
    # Should return exactly 5 users (top 5)
    assert len(data) == 5
    
    # Verify users are ordered by portfolio value descending
    # User 1: $10,000 + (10 * 155) + (2 * 1250) = $10,000 + $1,550 + $2,500 = $14,050
    # User 2: $5,000 + (5 * 260) = $5,000 + $1,300 = $6,300
    # User 3: $2,000 + (8 * 310) = $2,000 + $2,480 = $4,480
    # User 4: $4,000 (no holdings)
    # User 5: $3,000 (no holdings)
    
    assert data[0]["username"] == "user1"
    assert data[0]["portfolio_value"] == 14050.0
    
    assert data[1]["username"] == "user2"
    assert data[1]["portfolio_value"] == 6300.0
    
    assert data[2]["username"] == "user3"
    assert data[2]["portfolio_value"] == 4480.0
    
    assert data[3]["username"] == "user4"
    assert data[3]["portfolio_value"] == 4000.0
    
    assert data[4]["username"] == "user5"
    assert data[4]["portfolio_value"] == 3000.0
    
    # Verify bankrupt user is not included
    usernames = [item["username"] for item in data]
    assert "bankrupt_user" not in usernames