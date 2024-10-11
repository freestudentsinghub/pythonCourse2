def filter_vacancies(vacancies, key_words):
    """получить вакансии с ключевым словом в описании."""
    return [
        vacancy
        for vacancy in vacancies
        if any(key.lower() in vacancy["description"].lower() for key in key_words)
    ]


def sort_vacancies(vacancies):
    """Сортирует список вакансий по убыванию зарплаты"""
    return sorted(
        vacancies, key=lambda vacancy: vacancy.get("salary_from", 0), reverse=True
    )


def get_top_vacancies(vacancies, upper_part):
    """получить топ N вакансий по зарплате"""
    return vacancies[:upper_part]


def print_vacancies(vacancies):
    """Выводит информацию о вакансиях в консоль."""
    if vacancies:
        for index, vacancy in enumerate(vacancies, start=1):
            print(f"Вакансия {index}:")
            print(f"Название: {vacancy.get('name', 'Не указано')}")
            print(f"Зарплата от: {vacancy.get('salary_from', 'Не указана')}")
            print(f"Описание: {vacancy.get('description', 'Отсутствует')}")
            print(f"Ссылка: {vacancy.get('alternate_url', 'Не указана')}")
            print()
    else:
        print("Нет подходящих вакансий")
