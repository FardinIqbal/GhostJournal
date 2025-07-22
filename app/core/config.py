from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str
    alpaca_api_key: str
    alpaca_secret_key: str
    alpaca_base_url: str = 'https://paper-api.alpaca.markets'
    redis_url: str = 'redis://localhost:6379/0'

    class Config:
        env_file = '.env'

settings = Settings()
