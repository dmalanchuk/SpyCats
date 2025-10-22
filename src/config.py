from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    CATS_API: str

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()