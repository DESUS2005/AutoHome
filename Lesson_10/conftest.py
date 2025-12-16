import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def driver():
    """
    Фикстура для инициализации WebDriver.
    WebDriver будет создан один раз для всей тестовой сессии.
    """
    print("\n--- Инициализация WebDriver ---")
    # Настройка сервиса Chrome
    service = ChromeService(ChromeDriverManager().install())
    # Настройка опций Chrome (если нужны, например, headless режим)
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(60) # Устанавливаем таймаут загрузки страницы
    driver.implicitly_wait(5) # Устанавливаем неявное ожидание (можно уменьшить, если используете явные)

    yield driver # Предоставляем драйвер тестам

    print("\n--- Закрытие WebDriver ---")
    driver.quit() # Закрываем браузер после завершения всех тестов