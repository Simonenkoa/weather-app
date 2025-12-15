"""Главный модуль приложения.

Зачем нужен: Запускает программу, обрабатывает аргументы и выводит результат.
Использует argparse для консольного интерфейса.
"""
import sys
from weather.parser import get_parser
from weather.commands import process_command


def main() :
    """Основная функция запуска приложения."""
    parser = get_parser()
    args = parser.parse_args()      # Разбираем аргументы из командной строки

    try :        # Обрабатываем запрос и получаем данные о погоде
        data = process_command(args)
        print(f"Температура: {data['temperature']}°C, Скорость ветра: {data['windspeed']} км/ч")
    except Exception as e :
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__" :
    main()
    