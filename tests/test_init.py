import unittest
from unittest.case import TestCase
from main import *
from ya_rest_api import YaUploader


class TestAll(TestCase):
    def test_max_sale(self):
        res = max(stats, key=stats.get)
        self.assertEqual(res, max_sale(stats))

    def test_unique_geo(self):
        res = [213, 15, 54, 119, 35, 98]
        self.assertCountEqual(res, unique_geo(ids))

    def test_vizit(self):
        expected = {'visit1': ['Москва', 'Россия'], 'visit3': ['Владимир', 'Россия'],
                    'visit7': ['Тула', 'Россия'], 'visit8': ['Тула', 'Россия'],
                    'visit9': ['Курск', 'Россия'], 'visit10': ['Архангельск', 'Россия']}
        self.assertDictEqual(expected, visit_from_rus(geo_logs))
        self.assertIsInstance(visit_from_rus(geo_logs), dict)

    def test_create_folder(self):
        with open('token_1.txt', 'r') as file_object:
            token_ya = file_object.read().strip()
        self.assertEqual(YaUploader(token_ya).get_create_folder(), 201)

    def test_exists_folder(self):
        with open('token_1.txt', 'r') as file_object:
            token_ya = file_object.read().strip()
        self.assertEqual(YaUploader(token_ya).get_create_folder(), 409)


if __name__ == '__main__':
    unittest.main(verbosity=2)
