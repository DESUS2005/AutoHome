from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def search_film(self, film_name):
        search_input = WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located((By.NAME, "kp_query"))
        )
        search_input.send_keys(film_name)
        search_input.send_keys(Keys.ENTER)
