import sqlite3
from typing import Optional

DB_NAME = "weather_history.db"

def init_db():
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
    init_db()     # Сначала проверяем/создаём таблицу
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO requests (city, latitude, longitude, temperature, windspeed)
        VALUES (?, ?, ?, ?, ?)
    ''', (city or "", lat, lon, temp, wind))     # Параметры для защиты от SQL-инъекций
    conn.commit()
    conn.close()
