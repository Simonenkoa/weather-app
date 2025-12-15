"""Модуль для обработки аргументов командной строки.

Зачем нужен: Разбирает входные аргументы с помощью argparse для удобного запуска.
Поддерживает --city или --coords.
"""
import argparse
# Парсер нужен, чтобы программа удобно запускалась из консоли с разными параметрами

def get_parser():
    """Создаёт объект argparse.Parser для разбора аргументов.

        Returns:
            argparse.ArgumentParser: Готовый парсер с группой аргументов.
        """
    parser = argparse.ArgumentParser(description='Погода по городу или координатам')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--city', type=str, help='Название города (например, Москва)')
    group.add_argument('--coords', nargs=2, metavar=('LAT', 'LON'), type=float, help='Широта и долгота (например, 55.75 37.62)')
    return parser
