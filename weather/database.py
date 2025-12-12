import sqlite3
from typing import Optional

DB_NAME = "weather_history.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
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
    conn.commit()
    conn.close()

def log_to_db(city: Optional[str], lat: float, lon: float, temp: float, wind: float):
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO requests (city, latitude, longitude, temperature, windspeed)
        VALUES (?, ?, ?, ?, ?)
    ''', (city or "", lat, lon, temp, wind))
    conn.commit()
    conn.close()
