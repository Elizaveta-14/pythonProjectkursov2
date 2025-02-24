from abc import ABC, abstractmethod

class HeadHunterAPI(ABC):
    @abstractmethod
    def connect(self):
        pass


    @abstractmethod
    def get_vacancies(self, search_query: str, page: int = 1):
        """Метод для получения списка вакансий по поисковому запросу"""
        pass
