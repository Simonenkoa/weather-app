import json
import os
import time

CACHE_FILE = 'cache.json'

def load_cache():      # Загружаем кэш из файла, если он существует
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Ошибка чтения кэша: {e}")
            return {}
    return {}

def save_cache(cache):     # Сохраняем кэш в файл
    try:
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(cache, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка записи кэша: {e}")

def get_from_cache(key, max_age=3600):    # 1 час. Возвращаем данные из кэша, если они свежие
    cache = load_cache()
    if key in cache and time.time() - cache[key]['time'] < max_age:
        return cache[key]
    return None

def save_to_cache(key, data):       # Сохраняем новые данные в кэш
    cache = load_cache()
    cache[key] = data
    save_cache(cache)
