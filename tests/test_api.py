import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Добавляет корень проекта в путь

import unittest
from unittest.mock import patch, Mock
import requests
from weather.api import get_geocode, get_weather

class TestApi(unittest.TestCase):
    @patch('requests.get')
    def test_get_geocode_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'results': [{'latitude': 55.75, 'longitude': 37.62}]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        lat, lon = get_geocode('Москва')
        self.assertEqual(lat, 55.75)
        self.assertEqual(lon, 37.62)

    @patch('requests.get')
    def test_get_geocode_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        with self.assertRaises(ValueError):
            get_geocode('Несуществующий')

    @patch('requests.get')
    def test_get_weather_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'current_weather': {'temperature': 10, 'windspeed': 5}}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        data = get_weather(55.75, 37.62)
        self.assertEqual(data['temperature'], 10)

    @patch('requests.get')
    def test_get_weather_error(self, mock_get):
        mock_get.side_effect = requests.RequestException('Ошибка')
        with self.assertRaises(ConnectionError):
            get_weather(55.75, 37.62)
