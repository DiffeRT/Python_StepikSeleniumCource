from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.product_name = None
        self.product_price = None

    def add_item_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        self.product_name = self.browser.find_element(*ProductPageLocators.NAME).text
        self.product_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        add_button.click()

    def should_be_added_successfully(self):
        self.is_correct_added_item_name()
        self.is_correct_basket_price()

    def is_correct_added_item_name(self):
        added_item_name = self.browser.find_element(*ProductPageLocators.PROD_MESSAGE).text
        assert self.product_name == added_item_name, "Wrong product name in notification"

    def is_correct_basket_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        assert self.product_price == price, "Wrong price in notification"
