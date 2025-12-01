from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver

        # Локаторы
        self.delay_input_locator = (By.ID, "delay")
        # Все кнопки – по тексту внутри <span>
        self.button_locator = lambda text: (By.XPATH, f"//span[text()='{text}']")
        self.result_locator = (By.CSS_SELECTOR, "div.screen")

    def open(self, url):
        self.driver.get(url)

    def set_delay(self, delay_seconds):
        wait = WebDriverWait(self.driver, 10)
        delay_input = wait.until(EC.element_to_be_clickable(self.delay_input_locator))
        delay_input.clear()
        delay_input.send_keys(str(delay_seconds))

    def click_button(self, text):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable(self.button_locator(text)))
        button.click()

    def get_result(self):
        wait = WebDriverWait(self.driver, 60)
        # Ждем появления "15" в диве
        wait.until(EC.text_to_be_present_in_element(self.result_locator, "15"))
        return self.driver.find_element(*self.result_locator).text