from src.api_hh import HeadAPI
from src.vacancy import Vacancy
import pytest
import os

@pytest.fixture
def head_hunter_example():
    """Фикстура экземпляр класса HHJobPlatform"""
    return HeadAPI(base_url="https://api.hh.ru/vacancies")


@pytest.fixture
def mock_hh_api():
    """Создаем mock-объект для HHJobPlatform."""
    platform = HeadAPI(base_url="https://api.hh.ru/vacancies")
    return platform


