import os
import re
import pandas as pd
from pkginfo.develop import Develop

from src.api_hh import HeadAPI
from src.utils import HH


def user_interaction():
    vacancy = input("Введите название вакансии: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    print("Поиск вакансии")

    hh_vacancies = HeadAPI("https://api.hh.ru/vacancies")
    hh_vacancies.get_vacancies("Python", 20)
    vacancies = hh_vacancies.connect()


    j_vacancies = HH
    j_vacancies.add_to_file()
    j_vacancies.read_data_json()

    is_sort = input("Хотите отсортировать вакансии? Да/Нет ")
    if is_sort.lower() == "да":
        print(v for v in sorted(j_vacancies.info_about_vacancies))


    is_top_n = input(f"Вывести топ {top_n} вакансии? Да/Нет")
    if is_sort.lower() == "да":
        df = pd.DataFrame(j_vacancies.info_about_vacancies)
        print(df.hesd(top_n))
    else:
        print("Вакансии не выведены")


if __name__ == "__main__":
    user_interaction()