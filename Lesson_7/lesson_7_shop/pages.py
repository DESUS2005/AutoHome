from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.username_input)).send_keys(username)
        wait.until(EC.element_to_be_clickable(self.password_input)).send_keys(password)
        wait.until(EC.element_to_be_clickable(self.login_button)).click()


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        # Локаторы для добавления товаров
        self.backpack_add_button = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        self.tshirt_add_button = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_add_button = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        self.cart_link = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_product_backpack(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.backpack_add_button)).click()

    def add_product_tshirt(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.tshirt_add_button)).click()

    def add_product_onesie(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.onesie_add_button)).click()

    def go_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.cart_link)).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def proceed_to_checkout(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.checkout_button)).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_customer_info(self, first_name, last_name, postal_code):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.first_name_input)).send_keys(first_name)
        wait.until(EC.element_to_be_clickable(self.last_name_input)).send_keys(last_name)
        wait.until(EC.element_to_be_clickable(self.postal_code_input)).send_keys(postal_code)

    def continue_checkout(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.continue_button)).click()

    def get_total(self):
        wait = WebDriverWait(self.driver, 10)
        total_element = wait.until(EC.visibility_of_element_located(self.total_label))
        return total_element.text