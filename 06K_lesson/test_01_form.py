import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.common.exceptions import TimeoutException

@pytest.fixture
def driver():
    edge_driver_path = r"C:\Users\user\Desktop\EDGE\msedgedriver.exe"
    service = EdgeService(executable_path=edge_driver_path)
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

field_ids = ["first-name", "last-name", "address", "e-mail", "phone", "zip-code", "city", "country", "job-position", "company"]

def test_form_validation_and_highlighting(driver):
    wait = WebDriverWait(driver, 10)

    # Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполняем поля
    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")

    # Нажимаем кнопку Submit
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn').click()

    # Проверка, что поле ZIP подсвечено красным (класс "alert-danger")
    zip_div = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    class_attr = zip_div.get_attribute("class")
    assert "alert-danger" in class_attr, "Поле ZIP не подсвечено красным"

    # Цвета для ошибки
    expected_bg_color_error = "rgb(248, 215, 218)"  # или "#f8d7da" в формате hex
    expected_border_color_error = "rgb(245, 194, 199)"  # для border-color или "#f5c2c7"

    # Цвета для заполненного поля
    expected_bg_color_filled = "rgb(209, 231, 221)"  # либо "#d1e7dd"
    expected_border_color_filled = "rgb(186, 219, 204)"  # либо "#badbcc"

    def normalize_color(color_str):
        if color_str.startswith('rgba'):
            # 'rgba(209, 231, 221, 1)' -> 'rgb(209, 231, 221)'
            return color_str.replace('rgba', 'rgb').rsplit(',', 1)[0] + ')'
        return color_str

    for field_id in field_ids:
        try:
            element = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
            bg_color = normalize_color(element.value_of_css_property("background-color").strip())
            border_color = normalize_color(element.value_of_css_property("border-color").strip())

            # Проверяем, есть ли класс alert-danger (ошибка)
            parent_element = element  # Или, если нужно, найти родитель или другой элемент
            class_attr = parent_element.get_attribute("class")
            if "alert-danger" in class_attr:
                # Поле в ошибке
                expected_bg_color = expected_bg_color_error
                expected_border_color = expected_border_color_error
            else:
                # Поле заполнено правильно
                expected_bg_color = expected_bg_color_filled
                expected_border_color = expected_border_color_filled

            assert bg_color == expected_bg_color, \
                f"Поле '{field_id}' не подсвечено нужным фоном. Получено: {bg_color}, ожидаемо: {expected_bg_color}"
            assert border_color == expected_border_color, \
                f"Поле '{field_id}' не подсвечено нужной рамкой. Получено: {border_color}, ожидаемо: {expected_border_color}"

            print(f"{field_id} background-color: {bg_color}")
            print(f"{field_id} border-color: {border_color}")

        except TimeoutException:
            print(f"Элемент с id='{field_id}' не найден или не видим.")

        print(f"{field_id} background-color: {element.value_of_css_property('background-color')}")
        print(f"{field_id} border-color: {element.value_of_css_property('border-color')}")