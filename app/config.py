from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """Application settings from environment variables"""
    
    # App
    app_name: str = "Expense Tracker API"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # Database
    database_url: str = "sqlite:///./expenses.db"
    
    # API
    api_prefix: str = "/api/v1"
    
    # CORS
    cors_origins: str = "http://localhost:3000,http://localhost:8080"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

@lru_cache()
def get_settings():
    """Cached settings instance"""
    return Settings()