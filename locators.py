from selenium.webdriver.common.by import By


class Locators:
    # Item
    add_button = (By.CSS_SELECTOR, "#add_to_basket_form button")
    # Registration form
    email_field = (By.CSS_SELECTOR, "#id_registration-email")
    pwd1_field = (By.CSS_SELECTOR, "#id_registration-password1")
    pwd2_field = (By.CSS_SELECTOR, "#id_registration-password2")
    reg_button = (By.NAME, "registration_submit")
    profile_link = (By.CSS_SELECTOR, "a[href*='accounts']")
