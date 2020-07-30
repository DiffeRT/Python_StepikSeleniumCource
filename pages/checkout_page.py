from selenium.webdriver.support.select import Select

from .base_page import BasePage
from .locators import CheckOutPageLocators


class CheckOutPage(BasePage):
    def init_checkout_as_guest(self, email):
        self.browser.find_element(*CheckOutPageLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*CheckOutPageLocators.AS_GUEST).click()
        # dirty hack
        # self.browser.find_element(*CheckOutPageLocators.PWD_FIELD).send_keys("123")
        self.browser.find_element(*CheckOutPageLocators.GO_STEP1).click()

    def init_checkout_as_user(self, email, password):
        self.browser.find_element(*CheckOutPageLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*CheckOutPageLocators.AS_USER).click()
        self.browser.find_element(*CheckOutPageLocators.PWD_FIELD).send_keys(password)
        self.browser.find_element(*CheckOutPageLocators.GO_STEP1).click()

    def init_checkout_as_new_user(self, email):
        self.browser.find_element(*CheckOutPageLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*CheckOutPageLocators.AS_NEW).click()
        self.browser.find_element(*CheckOutPageLocators.GO_STEP1).click()

    def register_as_new(self, email, password):
        self.browser.find_element(*CheckOutPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*CheckOutPageLocators.REG_PWD1).send_keys(password)
        self.browser.find_element(*CheckOutPageLocators.REG_PWD2).send_keys(password)
        self.browser.find_element(*CheckOutPageLocators.REG_BUTTON).click()

    def fill_shipping_address(self, name, last_name, address, city, zip_code, country):
        self.browser.find_element(*CheckOutPageLocators.FIRST_NAME_FIELD).send_keys(name)
        self.browser.find_element(*CheckOutPageLocators.LAST_NAME_FIELD).send_keys(last_name)
        self.browser.find_element(*CheckOutPageLocators.ADDRESS_FIELD).send_keys(address)
        self.browser.find_element(*CheckOutPageLocators.CITY_FIELD).send_keys(city)
        self.browser.find_element(*CheckOutPageLocators.ZIP_FIELD).send_keys(zip_code)
        select_country = Select(self.browser.find_element(*CheckOutPageLocators.COUNTRY_FIELD))
        select_country.select_by_value(country)
        self.browser.find_element(*CheckOutPageLocators.GO_STEP2).click()

    def fill_payment_method(self):
        self.browser.find_element(*CheckOutPageLocators.GO_STEP3).click()

    def place_order(self):
        self.browser.find_element(*CheckOutPageLocators.GO_PLACE_ORDER).click()

    def should_be_confirmation(self, language):
        message = self.browser.find_element(*CheckOutPageLocators.CONFIRMATION).text
        expected = "confirmation"
        assert expected in message, "There is no confirmation message"
