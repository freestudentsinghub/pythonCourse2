from abc import ABC, abstractmethod

import requests

from src.vacancies import Vacancy


class GetApi(ABC):
    """Абстрактный класс для работы с API по поиску вакансий."""

    @abstractmethod
    def get_vacancies(self, search_query):
        pass


class HHApi(GetApi):
    """Класс для работы с api hh.ru"""

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query):
        """Получает данные о вакансиях с сайта HH.ru на основе поискового запроса."""
        settings = {"text": search_query, "area": 1}
        response = requests.get(self.url, params=settings).json()["items"]
        vacancy_list = []
        for vacancy_info in response:
            name = vacancy_info.get("name", "Не указано")
            alternate_url = vacancy_info.get("alternate_url", "Не указано")
            salary_info = vacancy_info.get("salary")
            description = vacancy_info.get("description", "Описание отсутствует")
            vacancy_list.append(
                Vacancy(name, alternate_url, salary_info, description).to_json()
            )
        return vacancy_list
