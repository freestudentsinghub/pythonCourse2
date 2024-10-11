from src.hhapi import HHApi
from src.vacancies_work import WorkWithJson
from utils.utils import (filter_vacancies, get_top_vacancies, print_vacancies,
                         sort_vacancies)


def user_interaction():
    """Основная работа с кодом"""
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    hh_api = HHApi()
    hh_vacancies = hh_api.get_vacancies(search_query)
    saver = WorkWithJson()
    saver.write_data(hh_vacancies)
    print("Ответ API:", hh_vacancies)

    if hh_vacancies:
        vacancies_list = []

        for vac in hh_vacancies:
            print(vac)
            vacancies_list.append(vac)

        print(vacancies_list)
        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
        sorted_vacancies = sort_vacancies(filtered_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        print_vacancies(top_vacancies)
    else:
        print(
            "Не удалось получить вакансии. Пожалуйста, проверьте запрос и попробуйте снова."
        )


if __name__ == "__main__":
    user_interaction()
    print("Программа завершила выполнение.")
