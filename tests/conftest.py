import os

import pytest

from src.api_hh import HeadAPI
from src.utils import HH
from src.vacancy import Vacancy


@pytest.fixture
def head_hunter_example():
    """Фикстура экземпляр класса HH"""
    return HeadAPI(base_url="https://api.hh.ru/vacancies")


@pytest.fixture
def mock_hh_api():
    """Создаем mock-объект для HH."""
    platform = HeadAPI(base_url="https://api.hh.ru/vacancies")
    return platform


@pytest.fixture
def hh_example():
    """Фикстура экземпляр класса HH"""
    return HH("data/json")


@pytest.fixture
def file_no_found():
    """Создаем mock-объект для HH."""
    file = HH("data/json")
    return file
