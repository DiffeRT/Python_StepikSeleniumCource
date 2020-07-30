import pytest
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


@pytest.mark.need_review_custom_scenarios
class TestGuestBasketPageActions:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.add_item_to_basket()
        page.should_be_added_successfully()

    def test_guest_can_edit_quantity(self, browser):
        link = "http://selenium1py.pythonanywhere.com/basket/"
        page = BasketPage(browser, link)
        page.open()
        page.update_quantity("2")
        page.should_be_updated_message()

    @pytest.mark.xfail
    def test_guest_can_remove_item(self, browser, get_language):
        link = "http://selenium1py.pythonanywhere.com/basket/"
        page = BasketPage(browser, link)
        page.open()
        page.remove_item()
        page.should_be_empty(get_language)
