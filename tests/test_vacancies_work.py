import json
import os
import shutil
import tempfile

import pytest

from src.vacancies_work import WorkWithJson


@pytest.fixture
def temporary_directory():
    directory = tempfile.mkdtemp()
    yield directory
    shutil.rmtree(directory)


@pytest.fixture
def work_with_json():
    return WorkWithJson()


def test_write_data(temporary_directory, work_with_json):
    work_with_json.filename = os.path.join(temporary_directory, "vacancies.json")
    vacancy = {
        "title": "Python Developer",
        "salary": 100000,
        "description": "Develops software",
    }
    work_with_json.write_data(vacancy)
    with open(work_with_json.filename, "r") as f:
        read_data = json.load(f)
    assert read_data["title"] == "Python Developer"
    assert read_data["salary"] == 100000
    assert read_data["description"] == "Develops software"
