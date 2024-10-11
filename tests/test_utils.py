from typing import List


from utils.utils import (filter_vacancies, get_top_vacancies, print_vacancies,
                         sort_vacancies)


def generate_sample_vacancies(size: int) -> List[dict]:
    sample_vacancies = []
    for i in range(size):
        sample_vacancies.append(
            {
                "id": i + 1,
                "name": f"Job {i + 1}",
                "alternate_url": f"job_{i + 1}.com",
                "salary_from": 100000 + i * 10000,
                "description": f"Description for Job {i + 1}",
            }
        )
    return sample_vacancies


def test_filter_vacancies():
    keywords = ["python", "developer"]
    sample_vacancies = generate_sample_vacancies(10)
    filtered_vacancies = filter_vacancies(sample_vacancies, keywords)
    assert len(filtered_vacancies) >= 0
    assert all(
        [
            any(keyword in vacancy["description"].lower() for keyword in keywords)
            for vacancy in filtered_vacancies
        ]
    )


def test_sort_vacancies():
    sample_vacancies = generate_sample_vacancies(10)
    sorted_vacancies = sort_vacancies(sample_vacancies)
    last_item = sorted_vacancies[-1]
    first_item = sorted_vacancies[0]
    assert last_item["salary_from"] <= first_item["salary_from"]


def test_get_top_vacancies():
    size = 5
    sample_vacancies = generate_sample_vacancies(10)
    top_vacancies = get_top_vacancies(sample_vacancies, size)
    assert len(top_vacancies) == size
    assert all(
        [
            vacancy["salary_from"] >= top_vacancies[-1]["salary_from"]
            for vacancy in sample_vacancies
            if vacancy not in top_vacancies
        ]
    )


def test_print_vacancies():
    sample_vacancies = generate_sample_vacancies(10)
    print_vacancies(sample_vacancies)
    assert True
