from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:
    """
    Представляет страницу результатов поиска на сайте labirint.ru.
    """
    URL: str = "https://www.labirint.ru/search/"  # Примерный URL результатов поиска

    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу результатов поиска.

        Args:
            driver: Экземпляр WebDriver.
        """
        self._driver: WebDriver = driver

    def get_search_results(self) -> list[str]:
        """
        Получает заголовки найденных книг на странице результатов.

        Returns:
            Список строк, содержащих заголовки книг.
        """
        wait = WebDriverWait(self._driver, 10)
        # Ждем появления хотя бы одной карточки товара
        # Мы используем CLASS_NAME, так как 'product-card' - это класс каждой карточки
        search_results_locator = (By.CLASS_NAME, "product-card")
        wait.until(EC.presence_of_element_located(search_results_locator))

        # Находим все элементы, содержащие заголовки книг
        # Селектор .product-card__name ищет элементы с этим классом внутри найденных карточек
        book_title_elements = self._driver.find_elements(By.CSS_SELECTOR, ".product-card__name")

        titles = [title.text for title in book_title_elements]
        return titles

    def get_result_count_text(self) -> str:
        """
        Получает текст, отображающий количество найденных результатов.

        Returns:
            Строка с количеством результатов (например, "Найдено 15 товаров").
        """
        wait = WebDriverWait(self._driver, 10)
        count_locator = (By.CSS_SELECTOR, ".searching-results__heading .num")
        try:
            count_element = wait.until(EC.presence_of_element_located(count_locator))
            return count_element.text
        except TimeoutException:
            # Если элемент количества не найден, возвращаем пустую строку или другое значение по умолчанию
            print("Элемент количества результатов не найден.") # Для отладки
            return ""