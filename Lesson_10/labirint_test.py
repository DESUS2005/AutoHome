import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List

# --- Константы ---
# Используем константы из MainPage для единообразия
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage

# Cookie policy
COOKIE_POLICY_DETAILS = {
    "name": "cookie_policy",
    "value": "1"
}

# --- Описание тестов ---
FEATURE = "Labirint Site"
STORY = "Add to Cart Functionality"

# --- Вспомогательная функция для ожидания кликабельности ---
@allure.step("Ожидание кликабельности элемента: {locator}")
def wait_for_clickable(driver: WebDriver, locator: tuple[str, str], timeout: int = 10) -> bool:
    """
    Ожидает, пока элемент станет кликабельным.

    Args:
        driver: Экземпляр WebDriver.
        locator: Кортеж (By, value), определяющий элемент.
        timeout: Максимальное время ожидания в секундах.

    Returns:
        True, если элемент стал кликабельным.
    Raises:
        TimeoutException: Если элемент не стал кликабельным за указанное время.
    """
    wait = WebDriverWait(driver, timeout)
    wait.until(EC.element_to_be_clickable(locator))
    return True


# --- Тестовая функция ---
@allure.feature(FEATURE)
@allure.story(STORY)
@allure.title("Добавление всех книг с результатов поиска в корзину")
@allure.description("Тест проверяет добавление всех книг из результатов поиска в корзину "
                    "и сверяет количество товаров в корзине.")
@allure.severity(allure.severity_level.NORMAL)
def test_add_all_books_to_cart(driver: WebDriver):
    """
    Тест выполняет поиск, добавляет все найденные товары в корзину
    и проверяет, что счетчик корзины соответствует количеству добавленных товаров.
    """
    main_page = MainPage(driver)
    result_page = ResultPage(driver)

    search_query = "python"

    with allure.step("Открываем главную страницу и принимаем куки"):
        main_page.open()
        main_page.accept_cookie_policy()

    with allure.step(f"Выполняем поиск по запросу: '{search_query}'"):
        main_page.search(search_query)

    with allure.step("Ожидаем появления кнопок 'В корзину'"):
        buy_button_selector = (By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")
        wait = WebDriverWait(driver, 10)
        buy_buttons: List[webdriver.Remote.webelement.WebElement] = wait.until(
            EC.presence_of_all_elements_located(buy_button_selector)
        )

        # Проверяем, что найдены кнопки для добавления в корзину
        assert buy_buttons, "Кнопки 'В корзину' не найдены на странице."
        print(f"Найдено {len(buy_buttons)} кнопок 'В корзину'.")

    counter_added = 0
    with allure.step("Добавляем все найденные товары в корзину"):
        for index, btn in enumerate(buy_buttons):
            try:
                # Используем wait_for_clickable для каждой кнопки перед кликом
                wait_for_clickable(driver, buy_button_selector)
                btn.click()
                counter_added += 1
                print(f"Товар {index + 1} добавлен в корзину.")
                # Убираем sleep, полагаемся на ожидания
            except Exception as e:
                print(f"Не удалось добавить товар {index + 1} в корзину. Ошибка: {e}")
                allure.attach(str(e), name=f"Error adding item {index + 1}",
                              attachment_type=allure.attachment_type.TEXT)

    with allure.step("Переходим в корзину"):
        driver.get("https://www.labirint.ru/cart/")

    with allure.step("Проверяем счетчик товаров в корзине"):
        cart_counter_selector = (By.CSS_SELECTOR, "span.basket-in-cart-a.j-cart-count")
        wait = WebDriverWait(driver, 10)
        try:
            # Ждем появления элемента счетчика
            cart_counter_element = wait.until(
                EC.presence_of_element_located(cart_counter_selector)
            )
            actual_count_text = cart_counter_element.text.strip()
            actual_count = int(actual_count_text) if actual_count_text.isdigit() else 0

            # --- Проверка ---
            assert counter_added == actual_count, \
                f"Количество добавленных товаров ({counter_added}) не совпадает с показанным в корзине ({actual_count})"

            print(f"Проверка счетчика корзины прошла успешно. Ожидалось: {counter_added}, Найдено: {actual_count}.")
            allure.attach(f"Ожидалось: {counter_added}, Найдено: {actual_count}", name="Cart Counter Check",
                          attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            print(f"Ошибка при проверке счетчика корзины. Ошибка: {e}")
            allure.attach(str(e), name="Cart Counter Check Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"Не удалось проверить счетчик корзины: {e}")  # Останавливаем тест при ошибке проверки

    print("Тест 'test_add_all_books_to_cart' успешно завершен.")