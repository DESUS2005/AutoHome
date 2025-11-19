from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

# Создаем объект ожидания
wait = WebDriverWait(driver, 10)

# Находим поле ввода и вводим текст "SkyPro"
input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='MyButton']")))
input_field.clear()
input_field.send_keys("SkyPro")

# Находим и нажимаем кнопку
button = wait.until(EC.element_to_be_clickable((By.ID, "updatingButton")))
button.click()

# Получаем текущий текст кнопки
button_text = wait.until(EC.visibility_of_element_located((By.ID, "updatingButton"))).text

# Выводим текст кнопки
print(button_text)

driver.quit()