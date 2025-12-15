"""Модуль для работы с SQLite базой данных.

Зачем нужен: Хранит историю запросов (дата, время, город, координаты, погода).
Создаёт таблицу автоматически.
"""
import sqlite3
from typing import Optional

DB_NAME = "weather_history.db"

def init_db():
    """Инициализирует БД и создаёт таблицу, если нужно."""
    conn = sqlite3.connect(DB_NAME)     # Подключаемся к БД (если файла нет — создаётся)
    cursor = conn.cursor()      # Курсор для выполнения SQL-запросов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            city TEXT,
            latitude REAL,
            longitude REAL,
            temperature REAL,
            windspeed REAL
        )
    ''')
    conn.commit()    # Сохраняем изменения
    conn.close()

def log_to_db(city: Optional[str], lat: float, lon: float, temp: float, wind: float):      # Сохраняет результат запроса в БД
    """Сохраняет запрос в БД.

        Args:
            city (str or None): Город.
            lat (float): Широта.
            lon (float): Долгота.
            temp (float): Температура.
            wind (float): Ветер.
        """
    init_db()     # Сначала проверяем/создаём таблицу
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO requests (city, latitude, longitude, temperature, windspeed)
        VALUES (?, ?, ?, ?, ?)
    ''', (city or "", lat, lon, temp, wind))     # Параметры для защиты от SQL-инъекций
    conn.commit()
    conn.close()
