from abc import ABC, abstractmethod


class WeatherService(ABC):

    @abstractmethod
    def current_weather(self):
        """Get current weather information from some city"""
        raise NotImplementedError()
