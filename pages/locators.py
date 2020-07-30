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
    WISHLIST_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")
    CHECKOUT_LINK = (By.CSS_SELECTOR, "#messages a[href*='checkout']")


class BasketPageLocators:
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEM = (By.CSS_SELECTOR, "#content_inner .basket-items")
    QUANTITY = (By.CSS_SELECTOR, "#id_form-0-quantity")
    UPDATE_BUTTON = (By.CSS_SELECTOR, "#basket_formset .btn-default")
    REMOVE_LINK = (By.CSS_SELECTOR, "#basket_formset a[data-id='0']")
    TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner p:nth-child(1)")


class WishPageLocators:
    add_wish_text = {
        'en': "Add to wish list",
        'ru': "Добавить к списку желаемого",
        'es': "Añadir a la lista de deseos"
    }

    # The problem is: "Add to wish list" has different locators and structure in case of not registered user,
    # registered but without wishlist and for registered with created wishlist
    @staticmethod
    def get_add_button_locator(language):
        return By.XPATH, f"//*[text()[contains(., '{WishPageLocators.add_wish_text[language]}')]]"


class CheckOutPageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_username")
    PWD_FIELD = (By.CSS_SELECTOR, "#id_password")
    AS_GUEST = (By.CSS_SELECTOR, "#id_options_0")
    AS_NEW = (By.CSS_SELECTOR, "#id_options_1")
    AS_USER = (By.CSS_SELECTOR, "#id_options_2")
    GO_STEP1 = (By.CSS_SELECTOR, "button.btn-primary")

    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#id_first_name")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#id_last_name")
    ADDRESS_FIELD = (By.CSS_SELECTOR, "#id_line1")
    CITY_FIELD = (By.CSS_SELECTOR, "#id_line4")
    ZIP_FIELD = (By.CSS_SELECTOR, "#id_postcode")
    COUNTRY_FIELD = (By.CSS_SELECTOR, "#id_country")
    GO_STEP2 = (By.CSS_SELECTOR, "button.btn-primary")

    GO_STEP3 = (By.CSS_SELECTOR, "#view_preview")

    GO_PLACE_ORDER = (By.CSS_SELECTOR, "#place-order")

    REG_EMAIL = (By.CSS_SELECTOR, "#id_email")
    REG_PWD1 = (By.CSS_SELECTOR, "#id_password1")
    REG_PWD2 = (By.CSS_SELECTOR, "#id_password2")
    REG_BUTTON = (By.NAME, "registration_submit")

    CONFIRMATION = (By.CSS_SELECTOR, "#default p.lead")
