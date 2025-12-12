from .api import get_geocode, get_weather
from .cache import get_from_cache, save_to_cache
from .database import log_to_db


def process_command(args):
    city_name = args.city  # может быть None, если использовали --coords
    lat, lon = None, None

    # 1. Пытаемся взять из старого кэша
    if city_name:
        key = f"city:{city_name}"
        cached = get_from_cache(key)
        if cached:
            # Если данные свежие — сразу возвращаем
            temperature = cached['temperature']
            windspeed = cached['windspeed']
        else:
            lat, lon = get_geocode(city_name)
    else:
        lat, lon = args.coords
        key = f"coords:{lat},{lon}"
        cached = get_from_cache(key)
        if cached:
            temperature = cached['temperature']
            windspeed = cached['windspeed']
        else:
            pass

    # 2. Если в кэше не было — делаем запрос к API
    if not cached:
        weather_data = get_weather(lat, lon)
        temperature = weather_data['temperature']
        windspeed = weather_data['windspeed']

        # Сохраняем в старый JSON-кэш
        save_to_cache(key, weather_data)

    # 3. В любом случае логируем запрос в базу данных
    log_to_db(
        city=city_name or "",      # если запрос был по координатам — город пустой
        lat=lat,
        lon=lon,
        temp=temperature,
        wind=windspeed
    )

    # Возвращаем результат для вывода в main.py
    return {
        "temperature": temperature,
        "windspeed": windspeed
    }