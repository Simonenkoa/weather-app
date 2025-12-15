import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
import time
from weather.cache import load_cache, save_cache, get_from_cache, save_to_cache, CACHE_FILE

class TestCache(unittest.TestCase):
    def setUp(self):
        if os.path.exists(CACHE_FILE):
            os.remove(CACHE_FILE)

    def tearDown(self):
        if os.path.exists(CACHE_FILE):
            os.remove(CACHE_FILE)

    def test_save_and_load_cache(self):
        cache = {'key': {'temperature': 10, 'windspeed': 5, 'time': time.time()}}
        save_cache(cache)
        loaded = load_cache()
        self.assertEqual(loaded['key']['temperature'], 10)

    def test_get_from_cache_fresh(self):
        key = 'key'
        data = {'temperature': 10, 'windspeed': 5, 'time': time.time()}
        save_to_cache(key, data)
        result = get_from_cache(key)
        self.assertEqual(result['temperature'], 10)

    def test_get_from_cache_old(self):
        key = 'key'
        data = {'temperature': 10, 'windspeed': 5, 'time': time.time() - 7200}
        save_to_cache(key, data)
        result = get_from_cache(key)
        self.assertIsNone(result)

    def test_load_cache_error(self):
        with open(CACHE_FILE, 'w') as f:
            f.write('invalid')
        result = load_cache()
        self.assertEqual(result, {})