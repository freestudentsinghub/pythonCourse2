import json
from abc import ABC, abstractmethod


class WorkVacancies(ABC):
    """Абстрактный класс для сохранения вакансий."""

    @abstractmethod
    def write_data(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class WorkWithJson(WorkVacancies):
    """Класс для сохранения вакансий в формате JSON"""

    def __init__(self):
        self.filename = "data/vacancies.json"

    def write_data(self, vacancy):
        with open(self.filename, "w") as f:
            json.dump(vacancy, f, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy):
        pass
