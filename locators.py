from selenium.webdriver.common.by import By


class Locators:
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PWD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PWD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")
    PROFILE_LINK = (By.CSS_SELECTOR, "a[href*='accounts']")
