import json
from src.vacancy import Vacancy
from src.base import Perser

class HH(Perser):
   """Класс для работы с файлами"""
   info_about_vacancies: list = []

   def __init__(self, patch: str = "data/data.json"):
       self.__path = patch
       self.info_about_vacancies =[]


   def add_to_file(self, vacancies: list[[dict]]):
       """Функция добовляет данные в формат json"""
       with open(self.__patch, "w", encoding="utf-8") as json_file:
           json.dump(vacancies, json_file, ensure_ascii=False, indent=4)


   def read_data_json(self):
        """ чтение json файла """
        try:
            with open(self.__path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            vacancies = []
            for vacancy in data['items']:
                vacancies.append(Vacancy(
                    vacancy['name'],
                    vacancy['apply_alternate_url'],
                    vacancy['salary'],
                    vacancy['area']['name']
                ))

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
        return str(getattr(self, 'info_about_vacancies', ''))









