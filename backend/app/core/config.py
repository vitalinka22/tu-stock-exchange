from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    LOG_TO_FILE: bool = False
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = ""
    FINNHUB_API_KEY: str = ""

    class Config:
        env_file = ".env" #specifies the file from which to load environment variables


settings = Settings()