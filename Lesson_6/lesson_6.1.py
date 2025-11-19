from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")
driver.implicitly_wait(20)

# Нажимаем на кнопку, вызывающую AJAX-загрузку
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Создаем ожидание
wait = WebDriverWait(driver, 10)

# Ждём появления элемента с классом "bg-success"
label = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)

# Получаем и выводим текст элемента
txt = label.text
print(txt)

driver.quit()