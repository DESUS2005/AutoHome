import pytest
from selenium import webdriver
from Pages import SlowCalculatorPage

def test_slow_calculator():
    driver = webdriver.Chrome()
    calculator_page = SlowCalculatorPage(driver)

    try:
        calculator_page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        calculator_page.set_delay(45)
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")
        result = calculator_page.get_result()
        assert result == "15", f"Ожидали 15, получили {result}"
    finally:
        driver.quit()