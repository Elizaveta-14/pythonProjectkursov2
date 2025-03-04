from abc import ABC, abstractmethod


class HeadHunterAPI(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_vacancies(self, search_query: str, page: int = 1):
        """Метод для получения списка вакансий по поисковому запросу"""
        pass


class Parser(ABC):
    """абстрактный класс"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_to_file(self, vacancies):
        pass

    @abstractmethod
    def read_data_json(self):
        pass

    @abstractmethod
    def return_vacancies(self):
        pass
