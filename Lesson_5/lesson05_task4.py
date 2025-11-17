from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

def run_test():
    # Запуск Firefox
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    try:
        # Переход на страницу логина
        driver.get("http://the-internet.herokuapp.com/login")
        sleep(2)

        # Ввод username
        username_input = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
        username_input.send_keys("tomsmith")
        sleep(1)

        # Ввод password
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
        password_input.send_keys("SuperSecretPassword!")
        sleep(1)

        # Нажатие кнопки "Login"
        login_button = driver.find_element(By.CSS_SELECTOR, 'button.radius')
        login_button.click()
        sleep(2)

        # Вывод текста зеленой плашки
        flash_message = driver.find_element(By.CSS_SELECTOR, 'div#flash')
        print("Сообщение:", flash_message.text.strip())

    finally:
        driver.quit()

# Запуск теста
if __name__ == "__main__":
    run_test()