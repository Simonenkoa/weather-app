"""Модуль для кэширования данных в JSON-файле.

Зачем нужен: Хранит свежие данные о погоде локально, чтобы избежать повторных API-запросов.
Кэш в файле cache.json, свежесть — 1 час.
"""
import json
import os
import time

CACHE_FILE = 'cache.json'

def load_cache():      # Загружаем кэш из файла, если он существует
    """Загружает кэш из JSON-файла.

        Returns:
            dict: Словарь с кэшем или пустой dict при ошибке.
        """
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Ошибка чтения кэша: {e}")
            return {}
    return {}

def save_cache(cache):     # Сохраняем кэш в файл
    """Сохраняет кэш в JSON-файл.

        Args:
            cache (dict): Данные для сохранения.

        Raises:
            IOError: При ошибке записи файла.
        """
    try:
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(cache, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка записи кэша: {e}")

def get_from_cache(key, max_age=3600):    # 1 час. Возвращаем данные из кэша, если они свежие
    """Получает данные из кэша, если они свежие.

        Args:
            key (str): Ключ кэша (например, 'city:Москва').
            max_age (int): Максимальный возраст данных в секундах (по умолчанию 3600 — 1 час).

        Returns:
            dict or None: Данные о погоде или None, если кэш старый/отсутствует.
        """
    cache = load_cache()
    if key in cache and time.time() - cache[key]['time'] < max_age:
        return cache[key]
    return None

def save_to_cache(key, data):       # Сохраняем новые данные в кэш
    """Сохраняет данные в кэш.

        Args:
            key (str): Ключ кэша.
            data (dict): Данные о погоде.
        """
    cache = load_cache()
    cache[key] = data
    save_cache(cache)
