import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_shopping_flow(driver):
    wait = WebDriverWait(driver, 10)

    # Открыть сайт
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    username_input = wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
    username_input.send_keys("standard_user")
    password_input = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    password_input.send_keys("secret_sauce")
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    # Добавить товары в корзину
    products = [
        "#add-to-cart-sauce-labs-backpack",
        "#add-to-cart-sauce-labs-bolt-t-shirt",
        "#add-to-cart-sauce-labs-onesie"
    ]
    for product_locator in products:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, product_locator))).click()

    # Перейти в корзину
    cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping_cart_link")))
    cart_button.click()

    # Нажать Checkout
    checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_button.click()

    # Заполнить форму
    first_name_input = wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
    first_name_input.send_keys("Денис")
    last_name_input = driver.find_element(By.ID, "last-name")
    last_name_input.send_keys("Слепцов")
    postal_code_input = driver.find_element(By.ID, "postal-code")
    postal_code_input.send_keys("678181")
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    # Проверить сумму и вывести её в терминал
    total_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
    total_text = total_element.text
    print(f"Полученная сумма на странице: '{total_text}'")  # Вывод в консоль

    # Проверка суммы
    assert total_text == "Total: $58.29", f"Expected total to be '$58.29' but got '{total_text}'"

    # Закрытие браузера происходит автоматически