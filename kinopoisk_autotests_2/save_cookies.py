from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pickle
import time


options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)


driver.get("https://www.kinopoisk.ru/")


input("После входа и прохождения капчи нажмите Enter...")


with open("cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

driver.quit()
print("Куки сохранены в cookies.pkl")
