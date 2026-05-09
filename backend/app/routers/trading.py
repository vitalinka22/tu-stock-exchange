from urllib import response

import yfinance as yf
import redis
import json
from fastapi import FastAPI, APIRouter, HTTPException

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, db=0)

router = APIRouter(prefix="/stocks", tags=["stocks"])
"""
Returns the stock price. 

Args:
    Ticker (str): name of the Company.

Returns:
    float: stock price.
"""
@router.get("")
def get_current_price(ticker: str) -> float:
    # price = yf.Ticker(ticker)
    # price = price.info.get("currentPrice")
    # return price
    try:
        ticker_data = yf.Ticker(ticker)
        price = ticker_data.fast_info["last_price"]
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"Ticker: {ticker} not found")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Unknown problem")
    return round(price, 2)

"""
Returns the stock price, caches it to redis. 

Args:
    Ticker (str): name of the Company.

Returns:
    float: stock price.
"""
@router.get("/{ticker}")
def get_ticker(ticker: str) -> float:
    ticker_price =float(r.get(ticker))
    if ticker_price:
        print("from cache")
        return ticker_price
    try:
        price = get_current_price(ticker)
    except Exception as e:
        raise HTTPException(status_code=404, detconfig --globalail=f"Ticker: {ticker} not found")

    r.setex(ticker, 3600, json.dumps(price))
    return price

"""
Returns the stock history over some period. 

Args:
    ticker (str): name of the Company.
    period (int): period of the history in months

Returns:
    str: history of the day with: "Date", "Open", "High", "Low", "Close", "Volume", "Dividends", "Stock Splits".
"""
@router.get("/{ticker}/{period}")
def get_ticker_history(ticker: str, period: int):
    try:
        ticker_data = yf.Ticker(ticker)
        ticker_history = ticker_data.history(f"{period}mo")
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"Ticker: {ticker} not found")
    return ticker_history.reset_index().to_dict(orient="records")