from dishka import Provider, Scope, provide

from src.repository.city_repository import CityRepository
from src.service.impl.weather_service_impl import WeatherServiceImpl


class WeatherProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def weather_repo(self) -> CityRepository:
        return CityRepository()

    @provide(scope=Scope.REQUEST)
    def weather_service(self, repo: CityRepository) -> WeatherServiceImpl:

        return WeatherServiceImpl(repo)
