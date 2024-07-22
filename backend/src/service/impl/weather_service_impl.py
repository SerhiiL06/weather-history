from typing import Union

import httpx
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.city_repository import CityRepository
from src.service.weather_service import WeatherService


class WeatherServiceImpl(WeatherService):

    def __init__(
        self,
        repo: CityRepository,
    ) -> None:
        self.key = "e8786867674a069d90519fc948992e87"
        self.repo = repo

    async def current_weather(self, city_name: str, session: AsyncSession):

        city = await self.repo.get_coordinate_by_name(name=city_name, session=session)

        async with httpx.AsyncClient() as client:
            url = f"https://api.openweathermap.org/data/3.0/onecall?lat={city.lat}&lon={city.lng}&exclude=minutely,hourly,daily,alerts&appid={self.key}"

            response = await client.get(url)

        #     return {"data": self.converter(response.json()["data"]["temp"])}
        return city

    @staticmethod
    def converter(temp_value: Union[float, str]) -> float:
        """Convert f to c"""
        return (float(temp_value) - 32) * 5 / 9
