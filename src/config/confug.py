from pydantic import BaseSettings


class Settings(BaseSettings):
    mongo_db_host: str = ""

    class Config:
        env_file = ".env"
