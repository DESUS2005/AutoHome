from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def run_test():
    # Запуск Google Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    try:
        # Переход на страницу
        driver.get("http://uitestingplayground.com/dynamicid")
        sleep(2)  

        # Находим кнопку по классу
        button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')

        # Кликаем по кнопке
        button.click()
        sleep(2)  
    finally:
        driver.quit()

# Запускаем три раза вручную
if __name__ == "__main__":
    run_test()

