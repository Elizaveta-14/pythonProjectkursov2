from pandas import DataFrame


class Vacancy:
    """Класс для работы с вакансиями"""
    __slots__ = ("__name","__url","__salary", "__vacancy", "salary_from", "salary_to")

    dataset: dict
    df_categories: DataFrame

    def __init__(self, name, url, salary, vacancy):
        """Инициализация элементов проверки"""
        self.__name = name
        self.__url = url
        self.__vacancy = vacancy
        self.__validate_salary(salary)



    def __validate_salary(self, salary):
        """Валидация по зарплате"""
        if salary:
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else 0
        else:
            self.salary_from = 0
            self.salary_to = 0


    def __eq__(self, other: object) -> bool:
        """Сравнение на равенство по минимальной зарплате"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from == other.salary_from

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнение меньшей по минимальной зарплате"""
        if isinstance(other, Vacancy):
            return self.salary_from < other.salary_from
        return NotImplemented

    def __le__(self, other: "Vacancy") -> bool:
        """Сравнение на меньше ил ровно по минимальной зарплате"""
        if isinstance(other, Vacancy):
            return self.salary_from <= other.salary_from
        return NotImplemented

    def __gt__(self, other: "Vacancy") -> bool:
        """Сравнение на больше по минимальной зарплате"""
        if isinstance(other, Vacancy):
            return self.salary_from > other.salary_from
        return NotImplemented

    def __ge__(self, other: "Vacancy") -> bool:
        """Сравнение на ,больше или ровно по минимальной зарплате"""
        if isinstance(other, Vacancy):
            return self.salary_from >= other.salary_from
        return NotImplemented

    def __repr__(self) -> str:
        """Представление объекту"""
        return f"Vacancy(title={self.name}, salary={self.salary_from}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def vacancy(self):
        return self.__vacancy

    @vacancy.setter
    def vacancy(self, value):
        self.__vacancy = value
