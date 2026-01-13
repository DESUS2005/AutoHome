import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from configs import config, testdata

@pytest.mark.ui
@allure.title("Проверка поиска фильма")
@allure.story("Функциональный тест: поиск фильма")
def test_search_film(driver):
    page = MainPage(driver)
    page.open(config.BASE_URL)
    page.search_film(testdata.FILMS["valid"])
    cards = WebDriverWait(driver, 120).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-tid^="movie-card"]'))
    )
    assert len(cards) > 0, "Результаты поиска не найдены"

@pytest.mark.ui
@allure.title("Поиск фильма на кириллице")
@allure.story("Функциональный тест: поиск фильма")
def test_search_film_cyrillic(driver):
    driver.get(config.BASE_URL)
    search_input = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.NAME, "kp_query"))
    )
    search_input.send_keys(testdata.FILMS["cyrillic"])
    search_input.send_keys(Keys.ENTER)
    cards = WebDriverWait(driver, 120).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-tid^="movie-card"]'))
    )
    assert len(cards) > 0, "Результаты поиска не найдены"

@pytest.mark.ui
@allure.title("Поиск фильма на латинице")
@allure.story("Функциональный тест: поиск фильма")
def test_search_film_latin(driver):
    driver.get(config.BASE_URL)
    search_input = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.NAME, "kp_query"))
    )
    search_input.send_keys(testdata.FILMS["latin"])
    search_input.send_keys(Keys.ENTER)
    cards = WebDriverWait(driver, 120).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-tid^="movie-card"]'))
    )
    assert len(cards) > 0, "Результаты поиска не найдены"

@pytest.mark.ui
@allure.title("Просмотр страницы фильма")
@allure.story("Функциональный тест: информация о фильме")
def test_view_movie_page(driver):
    driver.get(config.BASE_URL)
    search_input = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.NAME, "kp_query"))
    )
    search_input.send_keys(testdata.FILMS["valid"])
    search_input.send_keys(Keys.ENTER)
    first_card = WebDriverWait(driver, 120).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-tid^="movie-card"] a'))
    )
    first_card.click()
    movie_title = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    ).text
    poster = driver.find_elements(By.CSS_SELECTOR, 'img[data-tid^="poster"]')
    assert movie_title != "", "Название фильма не найдено"
    assert len(poster) > 0, "Постер фильма не найден"

@pytest.mark.ui
@allure.title("Проверка логотипа и возврата на главную")
@allure.story("Функциональный тест: навигация")
def test_logo_redirect(driver):
    driver.get(config.BASE_URL + "/some-movie")
    logo = WebDriverWait(driver, 120).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-test-id="next-link"]'))
    )
    logo.click()
    search_input = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.NAME, "kp_query"))
    )
    assert search_input.is_displayed(), "Главная страница не загружена после клика по логотипу"
