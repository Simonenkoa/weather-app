import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
import sqlite3
from weather.database import init_db, log_to_db, DB_NAME

class TestDatabase(unittest.TestCase):
    def setUp(self):
        init_db()

    def tearDown(self):
        if os.path.exists(DB_NAME):
            os.remove(DB_NAME)

    def test_log_to_db(self):
        log_to_db('Москва', 55.75, 37.62, 10.0, 5.0)
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT city, temperature FROM requests")
        row = cursor.fetchone()
        self.assertEqual(row[0], 'Москва')
        self.assertEqual(row[1], 10.0)
        conn.close()