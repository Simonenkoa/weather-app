import requests
import time

def get_geocode(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=ru"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if 'results' in data and data['results']:
            return data['results'][0]['latitude'], data['results'][0]['longitude']
        else:
            raise ValueError("Город не найден")
    except requests.RequestException as e:
        raise ConnectionError(f"Ошибка API: {e}")

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&timezone=auto"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()['current_weather']
        return {
            'temperature': data['temperature'],
            'windspeed': data['windspeed'],
            'time': time.time()  # timestamp для кэша
        }
    except requests.RequestException as e:
        raise ConnectionError(f"Ошибка API: {e}")
