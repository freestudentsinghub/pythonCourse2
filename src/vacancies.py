import json


class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

        if not isinstance(self.salary, (str, int)):
            self.salary = "Не указана"

    def __str__(self):
        return f"{self.title}\nЗарплата: {self.salary}\nСсылка: {self.link}\nОписание: {self.description}\n"

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def to_json(self):
        """Конвертирует объект Vacancy в строку формата JSON."""
        return self.__dict__

    @staticmethod
    def from_json(json_str):
        """Создает объект Vacancy из строки в формате JSON."""
        data = json.loads(json_str)
        return Vacancy(data["title"], data["link"], data["salary"], data["description"])

    @staticmethod
    def check_data_str(value):
        """Валидатор для строковых значений"""
        if value:
            return value
        return "информация не найдена"

    @staticmethod
    def check_data_int(value):
        """Валидатор для числовых значений"""
        if value:
            return value
        return 0
