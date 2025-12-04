import os
import requests
import pytest
import uuid

# Базовый URL API без версии, добавляем при необходимости
BASE_URL = "https://ru.yougile.com"

# Получение токена из переменной окружения для безопасности
TOKEN = os.getenv('YUGILE_TOKEN')

# Заголовки с авторизацией
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

@pytest.fixture
def create_project():
    # Генерируем уникальное название проекта
    project_title = f"Автотест проект {uuid.uuid4()}"
    data = {
        "title": project_title
        # Добавьте другие параметры по необходимости
    }

    # Создаем проект
    response = requests.post(f"{BASE_URL}/api-v2/projects", json=data, headers=headers)
    assert response.status_code == 201 or response.status_code == 200, f"Не удалось создать проект: {response.text}"
    project_id = response.json().get("id")
    yield project_id, project_title

    # После завершения теста удаляем проект
    # Предположим, что можно пометить как удаленный
    requests.put(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        json={"deleted": True},
        headers=headers
    )


def test_create_project_positive():
    """
    Позитивный тест - создание проекта.
    """
    project_title = f"Автотест проект {uuid.uuid4()}"
    data = {
        "title": project_title
    }
    response = requests.post(f"{BASE_URL}/api-v2/projects", json=data, headers=headers)
    assert response.status_code in [200, 201], f"Ошибка при создании проекта: {response.status_code}"
    resp_json = response.json()
    assert "id" in resp_json
    assert resp_json["title"] == project_title

    # Очистка: удаляем созданный проект
    project_id = resp_json["id"]
    requests.put(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        json={"deleted": True},
        headers=headers
    )


def test_create_project_negative_no_auth():
    """
    Негативный тест - создание проекта без авторизации.
    """
    project_title = f"Проба без авторизации {uuid.uuid4()}"
    data = {
        "title": project_title
    }
    response = requests.post(f"{BASE_URL}/api-v2/projects", json=data)
    assert response.status_code == 401 or response.status_code == 403


def test_create_project_negative_empty_title():
    """
    Негативный тест - создание проекта с пустым названием.
    """
    response = requests.post(f"{BASE_URL}/api-v2/projects", json={"title": ""}, headers=headers)
    assert response.status_code in [400, 422], f"Получен неожиданный статус: {response.status_code}"


def test_get_project_positive(create_project):
    """
    Позитивный тест - получение существующего проекта.
    """
    project_id, project_title = create_project
    response = requests.get(f"{BASE_URL}/api-v2/projects/{project_id}", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id
    assert data["title"] == project_title


def test_get_project_negative():
    """
    Негативный тест - получение несуществующего проекта.
    """
    invalid_id = "not-a-valid-id"
    response = requests.get(f"{BASE_URL}/api-v2/projects/{invalid_id}", headers=headers)
    assert response.status_code in [404, 400]


def test_update_project_positive(create_project):
    """
    Позитивное обновление проекта.
    """
    project_id, _ = create_project
    new_title = f"Обновленный проект {uuid.uuid4()}"
    response = requests.put(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        json={"title": new_title},
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id
    # Проверяем, что название обновилось
    get_response = requests.get(f"{BASE_URL}/api-v2/projects/{project_id}", headers=headers)
    assert get_response.json()["title"] == new_title


def test_update_project_negative():
    """
    Негативное обновление несуществующего проекта.
    """
    invalid_id = "invalid-id"
    response = requests.put(
        f"{BASE_URL}/api-v2/projects/{invalid_id}",
        json={"title": "Ошибка обновления"},
        headers=headers
    )
    assert response.status_code in [404, 400]