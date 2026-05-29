from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from redis import Redis
from app import schemas, models
from app.services import redis_client
from app.db import database
from app.routers.trading import get_current_price
from app.schemas.leaderboard_item import LeaderboardItem
from app.db.dependencies import get_db

router = APIRouter()

@router.get("/leaderboard", response_model=list[LeaderboardItem])
async def get_leaderboard(
    db: Session = Depends(get_db),
):

    try:
        users = db.query(
            models.User.id,
            models.User.username,
            models.User.balance
        ).all()

        holdings = db.query(
            models.Holding.user_id,
            models.Holding.ticker,
            models.Holding.quantity
        ).all()

        user_holdings = {}
        for holding in holdings:
            if holding.user_id not in user_holdings:
                user_holdings[holding.user_id] = []
            user_holdings[holding.user_id].append(holding)

        tickers = set(holding.ticker for holding in holdings)
        ticker_prices = {}
        
        for ticker in tickers:
            price = get_current_price(ticker)
            if price is None:
                raise HTTPException(
                    status_code=503,
                    detail=f"Could not fetch price for {ticker}. Service temporarily unavailable."
                )
            ticker_prices[ticker] = price

        # Calculate portfolio values
        user_values = []
        for user in users:
            total_value = user.balance
            
            # Add value of all holdings
            if user.id in user_holdings:
                for holding in user_holdings[user.id]:
                    total_value += holding.quantity * ticker_prices[holding.ticker]
            
            user_values.append({
                "user_id": user.id,
                "username": user.username,
                "portfolio_value": round(total_value, 2)
            })

        # Sort by portfolio value (descending) and return top 5
        #user_values.sort(key=lambda x: x["portfolio_value"], reverse=True)
        #return user_values[:5]

        return [
            schemas.LeaderboardItem(
                user_id=item["user_id"],
                username=item["username"],
                portfolio_value=item["portfolio_value"]
            ) 
            for item in user_values[:5]
        ]

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Internal server error while generating leaderboard"
        ) from e