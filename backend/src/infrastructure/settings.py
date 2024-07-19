from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    db_username: str = Field(alias="POSTGRES_USERNAME")
    db_password: str = Field(alias="POSTGRES_PASSWORD")
    db_host: str = Field(alias="POSTGRES_HOST")
    db_port: int = Field(alias="POSTGRES_PORT")
    db_name: str = Field(alias="POSTGRES_NAME")


config = Settings()
