from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

def run_test():
    # Запуск Firefox
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    try:
        # Переход на страницу
        driver.get("http://the-internet.herokuapp.com/inputs")
        sleep(2)  

        # Находим поле ввода по тегу или по селектору
        input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')

        # Вводим "Sky" в поле
        input_field.send_keys("Sky")
        sleep(1)

        # Очищаем поле
        input_field.clear()
        sleep(1)

        # Вводим "Pro"
        input_field.send_keys("Pro")
        sleep(2) 

    finally:
        # закрываем браузер
        driver.quit()

# Запуск теста
if __name__ == "__main__":
    run_test()