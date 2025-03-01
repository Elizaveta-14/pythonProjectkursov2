from pandas import DataFrame


class Vacancy:
    """ Класс для работы с вакансиями """
    dataset: dict
    df_categories: DataFrame

    def __init__(self, name: str, url: str, salary, vacancy: str):
        """Инициализация элементов проверки """
        self.name = name
        self.url = url
        self.salary = 0
        self.vacancy = vacancy
        self.__validate_salary(salary)

    def __validate_salary(self, salary):
        """ валидация по зарплате """
        if salary:
            self.salary_from = salary['from'] if salary['from'] else 0
            self.salary_to = salary['to'] if salary['to'] else 0
        else:
            self.salary_from = 0
            self.salary_to = 0

        self.salary = self.salary_from


    def __str__(self):
        return f"{self.url}, количество вакансии: {len(self.__vacancies)} "

    def __validate_salary(self, salary):
        """ валидация по зарплате """
        if salary:
            self.salary_from = salary['from'] if salary['from'] else 0
            self.salary_to = salary['to'] if salary['to'] else 0
        else:
            self.salary_from = 0
            self.salary_to = 0

    def __eq__(self, other: "Vacancy") -> bool:
        """Сравнение на равенство по минимальной зарплате"""
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        return NotImplemented

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнение меньшей по минимальной зарплате"""
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        return NotImplemented

    def __le__(self, other: "Vacancy") -> bool:
        """Сравнение на меньше ил ровно по минимальной зарплате"""
        if isinstance(other, Vacancy):
            return self.salary <= other.salary
        return NotImplemented

    def __gt__(self, other: "Vacancy") -> bool:
        """Сравнение на больше по минимальной зарплате"""
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        return NotImplemented

    def __ge__(self, other: "Vacancy") -> bool:
        """Сравнение на ,больше или ровно по минимальной зарплате"""
        if isinstance(other, Vacancy):
            return self.salary >= other.salary
        return NotImplemented

    def __repr__(self) -> str:
        """Представление объекту"""
        return f"Vacancy(title={self.name}, salary={self.salary}"
    