import os
from dotenv import load_dotenv
from weather_api import WeatherApi


class Controller:
    def __init__(self):
        load_dotenv()
        self.weather_app = WeatherApi(self._get_api_key())

    def _get_api_key(self):
        return os.getenv('API_KEY')

    def get_weather(self, location, version):
        return self.weather_app.get_weather(location, version)