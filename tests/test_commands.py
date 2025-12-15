import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from unittest.mock import patch
from argparse import Namespace
from weather.commands import process_command

class TestCommands(unittest.TestCase):
    @patch('weather.commands.get_geocode')
    @patch('weather.commands.get_weather')
    @patch('weather.commands.get_from_cache')
    @patch('weather.commands.save_to_cache')
    @patch('weather.commands.log_to_db')
    def test_process_command_city(self, mock_log, mock_save, mock_cache, mock_weather, mock_geocode):
        args = Namespace(city='Москва', coords=None)
        mock_cache.return_value = None
        mock_geocode.return_value = (55.75, 37.62)
        mock_weather.return_value = {'temperature': 10, 'windspeed': 5, 'time': 123}
        result = process_command(args)
        self.assertEqual(result['temperature'], 10)
        mock_save.assert_called()
        mock_log.assert_called()

    @patch('weather.commands.get_from_cache')
    def test_process_command_cache(self, mock_cache):
        args = Namespace(city='Москва', coords=None)
        mock_cache.return_value = {'temperature': 10, 'windspeed': 5}
        result = process_command(args)
        self.assertEqual(result['temperature'], 10)

    @patch('weather.commands.get_from_cache')
    @patch('weather.commands.get_geocode')
    def test_process_command_error(self, mock_geocode, mock_cache):
        args = Namespace(city='Несуществующий', coords=None)
        mock_cache.return_value = None
        mock_geocode.side_effect = ValueError('Город не найден')
        with self.assertRaises(ValueError):
            process_command(args)