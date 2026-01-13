import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach", True)  # оставить браузер открытым после теста

    service = Service()  # автоматически найдет chromedriver, если он в PATH
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()