import json
from typing import Dict, List
from src.base import Parser
from src.vacancy import Vacancy


class HH(Parser):
    """Класс для работы с файлами"""

    info_about_vacancies: list = []

    def __init__(self, path: str = "data/data.json"):
        self.__path = path
        self.info_about_vacancies = []

    def add_to_file(self, vacancies: List[Dict]):
        """Функция добовляет данные в формат json"""
        with open(self.__path, "w", encoding="utf-8") as json_file:
            json.dump(vacancies, json_file, ensure_ascii=False, indent=4)

    def read_data_json(self):
        """чтение json файла"""
        try:
            with open(self.__path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
            vacancies = []
            for vacancy in data:
                vacancies.append(
                    Vacancy(
                        vacancy["name"],
                        vacancy["url"],
                        vacancy["salary"],
                        vacancy["area"]["name"],
                    )
                )

                self.info_about_vacancies = vacancies
        except FileNotFoundError:
            print(f"Файл {self.__path} не найден.")
            self.info_about_vacancies = []

    @classmethod
    def return_vacancies(cls):
        """Чтение файла"""
        return cls.info_about_vacancies

    def remove_from_file(self):
        """Функция удаляет данные из файла"""
        with open(self.__path, "w"):
            pass

    def __str__(self):
        return str(getattr(self, "info_about_vacancies", ""))
