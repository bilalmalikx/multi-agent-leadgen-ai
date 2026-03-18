from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    LANGSMITH_PROJECT: str = os.getenv("LANGSMITH_PROJECT", "multi-agent")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/leadgen")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

    class Config:
        env_file = ".env"

settings = Settings()