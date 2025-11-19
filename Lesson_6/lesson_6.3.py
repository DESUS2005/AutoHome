from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ждем появления всех 4 картинок
images = wait.until(lambda d: d.find_elements(By.TAG_NAME, "img"))

# Проверяем, что на странице есть нужные картинки по id
ids = ["compass", "calendar", "award", "landscape"]
for img_id in ids:
    wait.until(EC.presence_of_element_located((By.ID, img_id)))


# Проверяем, что все изображения полностью загрузились
for img_id in ids:
    img_element = driver.find_element(By.ID, img_id)
    wait.until(lambda d, im=img_element: im.get_attribute("naturalWidth") != '0')


# После этого получаем свойство src у картинки с id="award"
award_img = driver.find_element(By.ID, "award")
src_value = award_img.get_attribute("src")
print("Значение src для картинки 'award':", src_value)

driver.quit()