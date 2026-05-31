import requests
from app.services.redis_client import redis_client
from app.core.config import settings

CACHE_TTL = 3600  # 1 hour
FINNHUB_URL = "https://finnhub.io/api/v1/quote"


def get_current_price(ticker: str) -> float | None:
    ticker = ticker.upper()
    cache_key = f"price:{ticker}"

    try:
        cached = redis_client.get(cache_key)
        if cached:
            return float(cached)
    except Exception:
        pass

    try:
        response = requests.get(
            FINNHUB_URL,
            params={"symbol": ticker, "token": settings.FINNHUB_API_KEY},
            timeout=5,
        )
        data = response.json()
        price = data.get("c")  # "c" = current price
        if not price or float(price) <= 0:
            return None
        price = float(price)
        try:
            redis_client.setex(cache_key, CACHE_TTL, str(price))
        except Exception:
            pass
        return price
    except Exception:
        return None
