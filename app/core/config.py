from pydantic_settings import BaseSettings 

class Settings(BaseSettings):   # this class manages application settings
    DATABASE_URL: str           # the database connection URL
    SECRET_KEY: str = "super-secret"    # secret key for security purposes
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"    # specify the environment file to load variables from 

settings = Settings()
