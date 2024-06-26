import requests


class WeatherApi:
    def __init__(self, api_key):
        self.hostname = "https://api.weatherapi.com"
        self.version = "/v1"
        self.api_key = api_key

    def api_call(self, path, params):
        endpoint = f"{self.hostname}{self.version}{path}"
        params['key'] = self.api_key

        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return response.raise_for_status()

    def get_weather(self, location):
        get_weather_endpoint = 'location.json'
        params = {'q': "Alken", 'aqi': 'no'}
        return self.api_call(get_weather_endpoint, params)


