from typing import Union

import httpx

from src.infrastructure.settings import config
from src.repository.city_repository import CityRepository
from src.service.exceptions.exc import ThirdApiUnavailable
from src.service.weather_service import WeatherService


class WeatherServiceImpl(WeatherService):

    key = config.weather_key

    def __init__(
        self,
        repo: CityRepository,
    ) -> None:
        self.repo = repo

    async def current_weather(self, ip_address: str):

        async with httpx.AsyncClient() as client:

            url = f"http://ip-api.com/json/{ip_address}"

            data_by_ip = await client.get(url)

            if data_by_ip.status_code != 200:
                raise ThirdApiUnavailable("api getter")

            data_by_id_json = data_by_ip.json()
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={data_by_id_json.get('lat')}&lon={data_by_id_json.get('lon')}&exclude=minutely,hourly,daily,alerts&appid={self.key}"

            response = await client.get(url)

            weather_data_json = response.json()

            if response.status_code != 200:
                raise ThirdApiUnavailable("openweather")

            return {
                "city": weather_data_json["name"],
                "tempetature": self.converter(weather_data_json["main"]["temp"]),
            }

    @staticmethod
    def converter(temp_value: Union[float, str]) -> float:
        """Convert K to C"""
        return round(float(temp_value) - 273.15, 2)
