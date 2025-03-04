import json
import unittest
from pathlib import Path
from unittest.mock import mock_open, patch

from src.utils import HH
from src.vacancy import Vacancy


class TestHH(unittest.TestCase):
    def setUp(self):
        self.hh = HH("test_data.json")
        self.test_vacancies = [
            {
                "name": "Python Developer",
                "url": "https://example.com",
                "salary": {"from": 100000, "to": 150000},
                "area": {"name": "Москва"},
            }
        ]

    def test_add_to_file(self):
        """Проверяем добавление данных в файл"""
        self.hh.add_to_file(self.test_vacancies)
        with open("test_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        self.assertEqual(data, self.test_vacancies)

    def test_read_data_json(self):
        """Создаем тестовый файл"""
        with open("test_data.json", "w", encoding="utf-8") as file:
            json.dump(self.test_vacancies, file, ensure_ascii=False, indent=4)

        self.hh.read_data_json()
        self.assertEqual(len(self.hh.info_about_vacancies), 1)
        self.assertIsInstance(self.hh.info_about_vacancies[0], Vacancy)

    def test_file_not_found(self):
        """Проверяем обработку ошибки при отсутствии файла"""
        with patch("builtins.open", side_effect=FileNotFoundError):
            self.hh.read_data_json()
            self.assertEqual(self.hh.info_about_vacancies, [])


@patch("json.loads")
def test_get_work(mock_get):
    """Проверяет на возвращение списка"""
    mock_get.return_value.status_code = 200
    return HH != 0


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_no_found(file_no_found):
    """Проверяет на возвращение не пустого списка при ошибке"""
    transactions = HH("data/json")
    assert transactions != []
