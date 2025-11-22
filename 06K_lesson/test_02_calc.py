import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("browser", ["chrome"])
def test_slow_calculator(browser):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 60)  # Увеличенное время ожидания

    try:
        # Открываем страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Находим и очищаем поле #delay, вводим 45
        delay_input = wait.until(EC.element_to_be_clickable((By.ID, "delay")))
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажимаем кнопку "7"
        btn_7 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='7']")))
        btn_7.click()

        # Нажимаем "+"
        plus1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='+']")))
        plus1.click()

        # Нажимаем "8"
        btn_8 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='8']")))
        btn_8.click()

        # Нажимаем "="
        equals = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='=']")))
        equals.click()

        # Ждем, пока в <div class="screen"> появится значение "15"
        result_div = wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
        )

        # Дополнительная проверка, что результат равен "15"
        result_text = driver.find_element(By.CSS_SELECTOR, "div.screen").text
        assert result_text == "15", f"Ожидали 15, получили {result_text}"

    finally:
        driver.quit()