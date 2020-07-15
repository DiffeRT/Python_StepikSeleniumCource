from selenium.webdriver.common.by import By


class Locators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PWD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PWD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")
    SUCCESS_ELEM = (By.CSS_SELECTOR, "#messages .alertinner")
