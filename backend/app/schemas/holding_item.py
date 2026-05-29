from pydantic import BaseModel

class HoldingItem(BaseModel):
    ticker: str
    quantity: int
    average_buy_price: float
    current_price: float

    class Config:
        orm_mode = True