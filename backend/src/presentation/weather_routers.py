from typing import Annotated

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database_core import core, session_transaction
from src.repository.city_repository import CityRepository
from src.service.impl.weather_service_impl import WeatherServiceImpl

weather_router = APIRouter()


@weather_router.post("/", response_model=None)
@inject
async def fetch_weather_by_city(
    city_name: str,
    session: Annotated[AsyncSession, Depends(session_transaction)],
    service: FromDishka[WeatherServiceImpl],
):
    return await service.current_weather(city_name, session)
