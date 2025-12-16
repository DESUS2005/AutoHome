import pytest
import allure
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage  # Импортируем ResultPage для проверки

# --- Маркеры для Allure ---
# Можно определить константы, чтобы избежать опечаток
FEATURE = "Labirint Site"
STORY = "Search Functionality"


# --- Тестовые функции ---
@allure.feature(FEATURE)
@allure.story(STORY)
@allure.title("Поиск книги с использованием Page Object")
@allure.description("Тест проверяет функциональность поиска на главной странице.")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_with_page_object(driver: webdriver.Chrome):
    """
    Тест проверяет поиск книги, используя паттерн Page Object.
    """
    main_page = MainPage(driver)
    result_page = ResultPage(driver)

    with allure.step("Открываем главную страницу"):
        main_page.open()
        main_page.accept_cookie_policy()

    search_query = 'java'
    with allure.step(f"Выполняем поиск по запросу: '{search_query}'"):
        main_page.search(search_query)

    with allure.step("Проверяем, что результаты поиска отображаются"):
        # Здесь мы просто проверяем, что есть хоть какие-то результаты
        results = result_page.get_search_results()
        assert len(results) > 0, f"Не найдены результаты поиска для '{search_query}'"

        print(f"Найдено {len(results)} результатов.")
        # alluredocs.add_attachment(f"Найденные результаты: {results}", name="search_results.txt", attachment_type=allure.attachment_type.TEXT) # Пример добавления вложения

    print("Тест 'test_search_with_page_object' успешно пройден.")