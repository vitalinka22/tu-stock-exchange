from pydantic import BaseModel
from datetime import datetime
from .leaderboard_item import LeaderboardItem

class LeaderboardHistoryItem(BaseModel):
    timestamp: datetime
    rankings: list[LeaderboardItem]
    
    class Config:
        from_attributes = True

class LeaderboardItem(LeaderboardItem):
    rank: int = 1  # Add rank to the existing leaderboard item
    
    class Config:
        from_attributes = True