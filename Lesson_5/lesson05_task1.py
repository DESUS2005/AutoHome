from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def run_test():
    # Запуск Google Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    try:
        # Открываем страницу
        driver.get("http://uitestingplayground.com/classattr")
        sleep(2)  # ждем, чтобы страница полностью загрузилась

        # Ищем кнопку по CSS-классу
        button = driver.find_element(By.CSS_SELECTOR, '.btn.class2.btn-primary.btn-test')

        # Кликаем по кнопке
        button.click()
        sleep(2)  
    finally:
        # Закрываем браузер
        driver.quit()

# Запускаем три раза вручную
if __name__ == "__main__":
    run_test()