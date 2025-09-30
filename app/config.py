# Installed pydantic package
# app/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache
#base settings is a class from pydantic package that allows us to define settings for our application
# it can read from environment variables or .env file

#here we define our settings class
class Settings(BaseSettings):
    database_url: str
    jwt_secret_key: str          # ✅ add this line
    jwt_algorithm: str = "HS256"
    redis_url: str
    environment: str = "development"

    class Config:
        env_file = ".env"

# we use lru_cache to cache the settings instance
# so that we don't create a new instance every time we call get_settings
@lru_cache()    
def get_settings():
    return Settings()
