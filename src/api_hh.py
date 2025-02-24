from typing import Dict, List
import requests
from src.base import HeadHunterAPI

class HeadhunterAPI(HeadHunterAPI):
    def __init__(self, base_url="https://api.hh.ru/vacancies") -> None:
        self.base_url = base_url


    def connect(self) -> True:
        """Проверяет подключение к API"""
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Ошибка подключения: {e}")



    def get_vacancies(self, search_query: str, per_page: int = 20) -> List[Dict]:
        """Получаем вакансии с платформы"""

        params = {"text": search_query, "per_page": per_page}
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json().get("items", [])
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")
            return []
