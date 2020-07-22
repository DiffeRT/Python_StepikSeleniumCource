from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a[href*='basket']")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PWD1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PWD2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    NAME = (By.CSS_SELECTOR, "#content_inner .product_main h1")
    PRICE = (By.CSS_SELECTOR, "#content_inner .product_main p.price_color")
    PROD_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) div")


class BasketPageLocators:
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEM = (By.CSS_SELECTOR, "#content_inner .basket-items")
