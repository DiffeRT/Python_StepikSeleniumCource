from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    empty_text = {
        'en': "Your basket is empty",
        'ru': "Ваша корзина пуста",
        'es': "Tu carrito esta vacío"
    }

    def should_be_empty(self, language):
        self.should_not_be_items_in_basket()
        self.should_be_empty_message(language)

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Item is presented in basket, but should not be"

    def should_be_empty_message(self, language):
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text
        expected = self.empty_text[language]
        assert expected in empty_message, "There is no empty basket message"
