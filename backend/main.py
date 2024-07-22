from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.presentation.providers.weather_provider import WeatherProvider
from src.presentation.weather_routers import weather_router
from src.repository.exceptions.exc import DoesntExists, doesnt_exists


def application():
    app = FastAPI()

    app.include_router(weather_router)

    app.add_exception_handler(DoesntExists, doesnt_exists)

    cont = make_async_container(WeatherProvider())

    setup_dishka(cont, app)

    return app


app = application()
