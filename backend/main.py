import json

from fastapi import FastAPI
from sqlalchemy import URL, insert, text
from sqlalchemy.ext.asyncio import create_async_engine

from common.city_types import LocationTypeEnum
from src.infrastructure.models.city import City


def application():
    app = FastAPI()

    return app


app = application()
