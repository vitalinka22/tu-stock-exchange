from pydantic import BaseModel

class LeaderboardItem(BaseModel):
    user_id: int
    username: str
    portfolio_value: float

    class Config:
        from_attributes = True