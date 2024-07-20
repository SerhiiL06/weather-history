from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    db_username: str = Field(alias="POSTGRES_USERNAME")
    db_password: str = Field(alias="POSTGRES_PASSWORD", default="")
    db_host: str = Field(alias="POSTGRES_HOST")
    db_port: str = Field(alias="POSTGRES_PORT")
    db_name: str = Field(alias="POSTGRES_NAME")


config = Settings()
