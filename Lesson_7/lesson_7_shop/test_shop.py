import pytest
from selenium import webdriver
from pages import LoginPage, ProductPage, CartPage, CheckoutPage

def test_shopping_flow():
    driver = webdriver.Firefox()
    driver.maximize_window()
    try:
        # Открыть сайт
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Добавление товаров
        product_page = ProductPage(driver)
        product_page.add_product_backpack()
        product_page.add_product_tshirt()
        product_page.add_product_onesie()

        # Переход в корзину
        product_page.go_to_cart()

        # Открытие корзины
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()

        # Оформление заказа
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_customer_info("Денис", "Слепцов", "678181")
        checkout_page.continue_checkout()

        # Проверить итоговую сумму
        total_text = checkout_page.get_total()
        print(f"Полученная сумма: '{total_text}'")
        assert total_text == "Total: $58.29", f"Ожидали 'Total: $58.29', получили '{total_text}'"

    finally:
        driver.quit()