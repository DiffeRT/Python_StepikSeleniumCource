from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import WishPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.product_name = None
        self.product_price = None

    # ---------- Actions ----------------------------
    def add_item_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        self.product_name = self.browser.find_element(*ProductPageLocators.NAME).text
        self.product_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        add_button.click()

    def add_item_to_wishlist(self, language):
        add_button = self.browser.find_element(*WishPageLocators.get_add_button_locator(language))
        self.product_name = self.browser.find_element(*ProductPageLocators.NAME).text
        add_button.click()

    def do_chekout_now(self):
        checkout_button = self.browser.find_element(*ProductPageLocators.CHECKOUT_LINK)
        checkout_button.click()

    # ---------- Checks ----------------------------
    def should_be_added_successfully(self):
        self.is_correct_added_item_name()
        self.is_correct_basket_price()

    def should_be_added_to_wishlist_successfully(self):
        wish_list_message = self.browser.find_element(*ProductPageLocators.WISHLIST_MESSAGE).text
        prod_name = f"'{self.product_name}'"
        assert prod_name in wish_list_message, "Wrong product name in wishlist notification"

    def is_correct_added_item_name(self):
        added_item_name = self.browser.find_element(*ProductPageLocators.PROD_MESSAGE).text
        assert self.product_name == added_item_name, "Wrong product name in notification"

    def is_correct_basket_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        assert self.product_price == price, "Wrong price in notification"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"

    def should_be_disabled_adding_to_wishlist(self, language):
        add_button = self.browser.find_element(*WishPageLocators.get_add_button_locator(language))
        assert (not add_button.is_enabled()), "Add to wish list is enabled, but should not be"
