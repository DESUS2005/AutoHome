import pytest
import allure
from unittest.mock import patch, Mock
from configs import config, testdata
import requests

@pytest.mark.api
@allure.title("Позитивный поиск фильма (локальный тест)")
@allure.story("API: поиск фильма")
def test_api_search_valid_film():
    film_name = testdata.FILMS['valid']

    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"films": [{"name": film_name}]}
        mock_get.return_value = mock_response

        response = requests.get(
            f"{config.API_BASE_URL}/search",
            params={"q": film_name},
            headers=config.HEADERS
        )

        mock_get.assert_called_once_with(
            f"{config.API_BASE_URL}/search",
            params={"q": film_name},
            headers=config.HEADERS
        )

        assert response.status_code == 200
        assert response.json()["films"][0]["name"] == film_name


@pytest.mark.api
@allure.title("Поиск фильма без токена (локальный тест)")
@allure.story("API: проверка заголовков")
def test_api_search_without_token():
    film_name = testdata.FILMS['valid']

    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.json.return_value = {"error": "Unauthorized"}
        mock_get.return_value = mock_response

        response = requests.get(
            f"{config.API_BASE_URL}/search",
            params={"q": film_name},
            headers={}  # без токена
        )

        mock_get.assert_called_once_with(
            f"{config.API_BASE_URL}/search",
            params={"q": film_name},
            headers={}
        )

        assert response.status_code == 401
        assert response.json()["error"] == "Unauthorized"


@pytest.mark.api
@allure.title("Пустой поиск фильма (локальный тест)")
@allure.story("API: пустой запрос")
def test_api_search_empty():
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"error": "Empty query"}
        mock_get.return_value = mock_response

        response = requests.get(
            f"{config.API_BASE_URL}/search",
            params={"q": ""},
            headers=config.HEADERS
        )

        mock_get.assert_called_once_with(
            f"{config.API_BASE_URL}/search",
            params={"q": ""},
            headers=config.HEADERS
        )

        assert response.status_code == 400
        assert response.json()["error"] == "Empty query"


@pytest.mark.api
@allure.title("Поиск фильма латиницей (локальный тест)")
@allure.story("API: поиск латиницей")
def test_api_search_latin():
    film_name = "Matrix"

    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"films": [{"name": film_name}]}
        mock_get.return_value = mock_response

        response = requests.get(
            f"{config.API_BASE_URL}/search",
            params={"q": film_name},
            headers=config.HEADERS
        )

        mock_get.assert_called_once_with(
            f"{config.API_BASE_URL}/search",
            params={"q": film_name},
            headers=config.HEADERS
        )

        assert response.status_code == 200
        assert response.json()["films"][0]["name"] == film_name


@pytest.mark.api
@allure.title("Неподдерживаемый метод запроса (локальный тест)")
@allure.story("API: проверка метода POST")
def test_api_search_wrong_method():
    film_name = testdata.FILMS['valid']

    with patch("requests.post") as mock_post:
        mock_response = Mock()
        mock_response.status_code = 405
        mock_response.json.return_value = {"error": "Method Not Allowed"}
        mock_post.return_value = mock_response

        response = requests.post(
            f"{config.API_BASE_URL}/search",
            data={"q": film_name},
            headers=config.HEADERS
        )

        mock_post.assert_called_once_with(
            f"{config.API_BASE_URL}/search",
            data={"q": film_name},
            headers=config.HEADERS
        )

        assert response.status_code == 405
        assert response.json()["error"] == "Method Not Allowed"
