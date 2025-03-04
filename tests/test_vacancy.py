import unittest

from pandas import DataFrame

from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):
    def setUp(self):
        # Создаем тестовые данные
        self.vacancy1 = Vacancy(
            name="Python Developer",
            url="https://example.com",
            salary={"from": 100000, "to": 150000},
            vacancy="Python Developer",
        )

        self.vacancy2 = Vacancy(
            name="Java Developer",
            url="https://example.com",
            salary={"from": 120000, "to": 180000},
            vacancy="Java Developer",
        )

        self.vacancy3 = Vacancy(
            name="Junior Developer",
            url="https://example.com",
            salary={"from": 80000, "to": 120000},
            vacancy="Junior Developer",
        )

    def test_init(self):
        self.assertEqual(self.vacancy1.name, "Python Developer")
        self.assertEqual(self.vacancy1.url, "https://example.com")
        self.assertEqual(self.vacancy1.salary_from, 100000)
        self.assertEqual(self.vacancy1.salary_to, 150000)

    def test_validate_salary(self):
        # Тестирование валидации зарплаты
        vacancy_no_salary = Vacancy(
            name="No Salary",
            url="https://example.com",
            salary=None,
            vacancy="No Salary",
        )
        self.assertEqual(vacancy_no_salary.salary_from, 0)
        self.assertEqual(vacancy_no_salary.salary_to, 0)

    def test_comparison_operators(self):
        # Тестирование операторов сравнения
        self.assertTrue(self.vacancy1 < self.vacancy2)
        self.assertTrue(self.vacancy1 > self.vacancy3)
        self.assertTrue(self.vacancy1 <= self.vacancy1)
        self.assertTrue(self.vacancy1 >= self.vacancy1)
        self.assertFalse(self.vacancy1 == self.vacancy2)
