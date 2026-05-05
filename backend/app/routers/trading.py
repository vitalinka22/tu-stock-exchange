from fastapi import APIRouter, HTTPException
from pydantic import BaseModel 

router = APIRouter()

# FAKE PRICE FUNCTION
#BE3 ALAN PLEASE IMPLEMENT IT 
def get_current_price(ticker: str) -> float:
    fake_prices = {
        "AAPL": 150.25,
        "GOOGL": 2800.00,
        "TSLA": 200.00,
        "MSFT": 380.00,
        "AMZN": 3500.00,
    }
    return fake_prices.get(ticker, 100.00)

# data the frontend send
class TradeRequest(BaseModel):
    ticker: str
    quantity: int

@router.post("/trades/buy")
def buy_stock(trade: TradeRequest):
    price = get_current_price(trade.ticker)
    total_cost = price*trade.quantity

    return {
        "message": "Buy order received",
        "ticker": trade.ticker,
        "quantity":trade.quantity, 
        "price_per_stock": price, 
        "total_cost" : total_cost
    }   

@router.post("/trades/sell")
def sell_stock(trade: TradeRequest):
    price = get_current_price(trade.ticker)
    total_value = price * trade.quantity

    return {
        "message": "Sell order received",
        "ticker": trade.ticker,
        "quantity": trade.quantity,
        "price_per_stock": price,
        "total_value": total_value,
    }