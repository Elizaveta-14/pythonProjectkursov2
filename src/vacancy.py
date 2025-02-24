from src.api_hh import HeadHunterAPI
import requests
from typing import Dict, List
from src.zero_vacancies import ZeroVacanciesException
from typing import Any
class HeadWorck:
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """
    __slots__ = ("url", "headers", "params", "vacancies")
    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
            super().__init__()


    def __str__(self):
        return f"{self.url}, количество вакансии: {len(self.__vacancies)} "


    def add_vacancies(self,new_vacancies: List[Dict], params: int) -> Any:
        """Добавление вакансии"""
        if isinstance(new_vacancies, params):
            try:
                if new_vacancies.params == 0:
                    raise ZeroVacanciesException(
                        "Нельзя добавить Добавить вакансию с нулевыми параметрами"
                    )
            except ZeroVacanciesException as e:
                print(str(e))
            else:
                self.vacancies.append(new_vacancies)
                new_vacancies.params['page'] += 1
                print("Вакансия успешно добавлена")
            finally:
                print("Обработка вакансии успешно завершена")
        else:
            raise TypeError
        return new_vacancies

    def filter_words(self, vacancies: List[Dict], keyword,) -> List[Dict]:
        """Фильтрует вакансии по ключевому слову"""
        return [vacancy for vacancy in vacancies if keyword.lower() in vacancy[""].lower()]

    def __delitem__(self, keyword) -> List[Dict]:
        """Удаляет вакансии"""
        if isinstance(keyword, int):
            del self.vacancies[keyword]
        elif isinstance(keyword, list):
            for vacancies in keyword:
                while vacancies in self.vacancies:
                    self.vacancies.remove(vacancies)
        else:
            raise TypeError("Ключевое слово не найдено")


    def __eq__(self, other: object, vacancy) -> bool:
        """Сравнение на равенство по минимальной зарплате"""
        if isinstance(other, vacancy):
            return self.salary == other.salary
        return NotImplemented

    def __lt__(self, other: object, vacancy) -> bool:
        """Сравнение меньшей по минимальной зарплате"""
        if isinstance(other, vacancy):
            return self.salary < other.salary
        return NotImplemented

    def __le__(self, other: object, vacancy) -> bool:
        """Сравнение на меньше ил ровно по минимальной зарплате"""
        if isinstance(other, vacancy):
            return self.salary <= other.salary
        return NotImplemented

    def __gt__(self, other: object, vacancy) -> bool:
        """Сравнение на больше по минимальной зарплате"""
        if isinstance(other, vacancy):
            return self.salary > other.salary
        return NotImplemented

    def __ge__(self, other: object, vacancy) -> bool:
        """Сравнение на ,больше или ровно по минимальной зарплате"""
        if isinstance(other, vacancy):
            return self.salary >= other.salary
        return NotImplemented

    def __repr__(self) -> str:
        """Представление объекту"""
        return f"vacancy(title={self.name}, salary={self.salary}"
    