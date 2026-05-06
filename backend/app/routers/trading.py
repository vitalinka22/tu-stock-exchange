from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel 
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.trade import Trade
from app.models.users import User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
    user_id: int # temporary - later comes from JWT token

@router.post("/trades/buy")
def buy_stock(trade: TradeRequest, db : Session = Depends(get_db)):

    #find the user in database
    user = db.query(User).filter(User.id == trade.user_id).first()
    if not user:
        raise HTTPException(status_code = 404, detail = 'User not found')
    
    price = get_current_price(trade.ticker)
    total_cost = price*trade.quantity

    if user.balance < total_cost:
        raise HTTPException(
            status_code = 400,
            detail = f"Insufficient funds. Need ${total_cost}, have ${user.balance}"
        )
    
    
    user.balance -= total_cost

    new_trade = Trade(
    user_id=user.id,
    ticker=trade.ticker,
    trade_type="buy",
    quantity=trade.quantity,
    price=price,
    total_value=total_cost,
    )
    db.add(new_trade)
    db.commit()

    return {
        "message": "Buy order successful",
        "ticker": trade.ticker,
        "quantity":trade.quantity, 
        "price_per_stock": price, 
        "total_cost" : total_cost,
        "new_balance": user.balance,
    }   

@router.post("/trades/sell")
def sell_stock(trade: TradeRequest, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == trade.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    price = get_current_price(trade.ticker)
    total_value = price * trade.quantity

    new_trade = Trade(
        user_id=user.id,
        ticker=trade.ticker,
        trade_type="sell",
        quantity=trade.quantity,
        price=price,
        total_value=total_value,
    )
    db.add(new_trade)

    user.balance += total_value
    db.commit()

    return {
        "message": "Sell order successful",
        "ticker": trade.ticker,
        "quantity": trade.quantity,
        "price_per_stock": price,
        "total_value": total_value,
        "new_balance": user.balance,
    }



