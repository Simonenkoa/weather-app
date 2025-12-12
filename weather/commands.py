from .api import get_geocode, get_weather
from .cache import get_from_cache, save_to_cache


def process_command(args) :
    if args.city :
        key = f"city:{args.city}"
        cache_data = get_from_cache(key)
        if cache_data :
            return cache_data
        lat, lon = get_geocode(args.city)
    else :
        lat, lon = args.coords
        key = f"coords:{lat},{lon}"
        cache_data = get_from_cache(key)
        if cache_data :
            return cache_data

    weather_data = get_weather(lat, lon)
    save_to_cache(key, weather_data)
    return weather_data
