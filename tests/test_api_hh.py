import unittest
from unittest.mock import Mock, patch

from src.api_hh import HeadAPI




def test_connect(mock_hh_api):
    """Тест на успешное подключение к API"""
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        assert mock_hh_api.connect() is True


def test_get_vacancies_success(mock_hh_api):
    """Тест на успешное получение вакансий."""
    with patch("requests.get") as mock_get:
        # Мокаем успешный ответ от API с вакансией
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "items": [{"id": 1, "name": "Developer"}]
        }

        vacancies = mock_hh_api.get_vacancies("developer")
        assert len(vacancies) == 1
        assert vacancies[0]["name"] == "Developer"
