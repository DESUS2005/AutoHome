from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Optional


class MainPage:
    """
    Представляет главную страницу сайта labirint.ru.
    """
    URL: str = "https://www.labirint.ru/"
    # Селекторы элементов на странице
    SEARCH_INPUT_SELECTOR = (By.CSS_SELECTOR, "#search-field")
    SEARCH_BUTTON_SELECTOR = (By.CSS_SELECTOR, "button[type=submit]")
    COOKIE_POLICY_SELECTOR = (By.CSS_SELECTOR,
                              "button[id='cookie-policy-accept']")  # Пример селектора для кнопки принятия куки
    SEARCH_RESULTS_CONTAINER_SELECTOR = (By.CLASS_NAME, "product-card")

    def __init__(self, driver: WebDriver):
        """
        Инициализирует главную страницу.

        Args:
            driver: Экземпляр WebDriver.
        """
        self._driver: WebDriver = driver
        self._driver.maximize_window()

    def open(self) -> None:
        """
        Открывает главную страницу сайта.
        """
        self._driver.get(self.URL)

    def accept_cookie_policy(self) -> None:
        """
        Принимает политику cookie, если кнопка присутствует.
        """
        try:
            wait = WebDriverWait(self._driver, 5)  # Короткое ожидание, т.к. куки могут не появиться
            cookie_button = wait.until(
                EC.element_to_be_clickable(self.COOKIE_POLICY_SELECTOR)
            )
            cookie_button.click()
            print("Политика cookie принята.")
        except Exception:
            print("Кнопка принятия cookie не найдена или уже была нажата.")
            pass  # Кнопки нет или она уже была нажата

    def _wait_for_element(self, locator: tuple[str, str], timeout: int = 10) -> WebDriverWait.until:
        """
        Общий метод для ожидания появления элемента.

        Args:
            locator: Кортеж (By, value), определяющий элемент.
            timeout: Максимальное время ожидания в секундах.

        Returns:
            WebDriver.until: Результат ожидания.
        """
        wait = WebDriverWait(self._driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def _wait_for_clickable_element(self, locator: tuple[str, str], timeout: int = 10) -> WebDriverWait.until:
        """
        Общий метод для ожидания, пока элемент станет кликабельным.

        Args:
            locator: Кортеж (By, value), определяющий элемент.
            timeout: Максимальное время ожидания в секундах.

        Returns:
            WebDriver.until: Результат ожидания.
        """
        wait = WebDriverWait(self._driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def search(self, query: str) -> None:
        """
        Выполняет поиск по заданному запросу.

        Args:
            query: Строка поискового запроса.
        """
        search_input = self._wait_for_element(self.SEARCH_INPUT_SELECTOR)
        search_input.clear()
        search_input.send_keys(query)

        search_button = self._wait_for_clickable_element(self.SEARCH_BUTTON_SELECTOR)
        search_button.click()

        # Ожидаем появления контейнера с результатами поиска
        self._wait_for_element(self.SEARCH_RESULTS_CONTAINER_SELECTOR)
        print(f"Поиск по запросу '{query}' выполнен.")