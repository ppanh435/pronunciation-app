from pydantic_settings import BaseSettings
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent.parent.parent / ".env"

class Settings(BaseSettings):
    openai_api_key: str
    database_url: str

    class Config:
        env_file = str(ENV_PATH)
        env_file_encoding = "utf-8"

settings = Settings()