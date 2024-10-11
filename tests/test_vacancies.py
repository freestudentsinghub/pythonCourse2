import json

import pytest

from src.vacancies import Vacancy


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        (
            {
                "title": "Software Engineer",
                "link": "www.example.com",
                "salary": 100000,
                "description": "Develops software",
            },
            "Software Engineer\nЗарплата: 100000\nСсылка: www.example.com\nОписание: Develops software\n",
        ),
        (
            {
                "title": "Manager",
                "link": "",
                "salary": "Not specified",
                "description": "",
            },
            "Manager\nЗарплата: Not specified\nСсылка: \nОписание: \n",
        ),
    ],
)
def test_to_string(input_data, expected_output):
    v = Vacancy(**input_data)
    assert str(v) == expected_output


def test_less_than():
    a = Vacancy("A", "a", 10, "desc A")
    b = Vacancy("B", "b", 20, "desc B")

    assert a < b


def test_greater_than():
    a = Vacancy("A", "a", 10, "desc A")
    b = Vacancy("B", "b", 20, "desc B")
    c = Vacancy("C", "c", 10, "desc C")
    d = Vacancy("D", "d", 30, "desc D")

    assert b > a
    assert d > b
    assert d > c


def test_to_json():
    v = Vacancy("Title", "Link", 1000, "Desc")
    json_str = json.dumps(v.to_json())
    actual = json.loads(json_str)
    expected = {"title": "Title", "link": "Link", "salary": 1000, "description": "Desc"}
    assert actual == expected


def test_from_json():
    json_str = (
        '{"title": "Title", "link": "Link", "salary": 1000, "description": "Desc"}'
    )
    v = Vacancy.from_json(json_str)
    assert v.title == "Title"
    assert v.link == "Link"
    assert v.salary == 1000
    assert v.description == "Desc"


def test_check_data_str():
    assert Vacancy.check_data_str("Hello") == "Hello"
    assert Vacancy.check_data_str(None) == "информация не найдена"


def test_check_data_int():
    assert Vacancy.check_data_int(100) == 100
    assert Vacancy.check_data_int(None) == 0
