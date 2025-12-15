import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from weather.parser import get_parser

class TestParser(unittest.TestCase):
    def test_get_parser_city(self):
        parser = get_parser()
        args = parser.parse_args(['--city', 'Москва'])
        self.assertEqual(args.city, 'Москва')

    def test_get_parser_coords(self):
        parser = get_parser()
        args = parser.parse_args(['--coords', '55.75', '37.62'])
        self.assertEqual(args.coords, [55.75, 37.62])

    def test_get_parser_no_args(self):
        parser = get_parser()
        with self.assertRaises(SystemExit):
            parser.parse_args([])