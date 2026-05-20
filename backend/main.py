from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from app.tasks.snapshot import create_daily_snapshot
from app.core.config import settings
from app.utils.logger import logger

app = FastAPI()

scheduler = BackgroundScheduler()

scheduler.add_job(
    create_daily_snapshot,
    'cron',
    hour=0,  # Midnight UTC
    minute=0,
    id='daily_snapshot_job',
    replace_existing=True
)

scheduler.start()
logger.info("Scheduled daily net worth snapshot job (runs at 00:00 UTC)")

@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()
    logger.info("Scheduler stopped")

from app.routers.trading import router as trading_router
from app.routers.auto_trades import router as auto_trades_router

app = FastAPI(title="TU Stock Exchange API")

app.include_router(trading_router, prefix="/api")
app.include_router(auto_trades_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "TU Stock Exchange API is running"}
