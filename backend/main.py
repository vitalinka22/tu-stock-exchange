from fastapi import FastAPI
from app.routers.trading import router as trading_router

app = FastAPI(title="TU Stock Exchange API")

app.include_router(trading_router)

@app.get("/")
def root():
    return {"message": "TU Stock Exchange API is running"}