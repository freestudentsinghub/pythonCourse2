import pytest

from src.hhapi import HHApi


@pytest.fixture
def hh_api():
    return HHApi()


def test_get_vacancies(hh_api):
    query = "Python developer"
    expected_result = [
        {
            "description": "Описание отсутствует",
            "link": "https://hh.ru/vacancy/108444291",
            "salary": "Не указана",
            "title": "Младший Back-end разработчик",
        }
    ]
    result = hh_api.get_vacancies(query)
    assert len(result) > 0
    assert result[0] == expected_result[0]
