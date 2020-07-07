import time
from locators import Locators

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_button_availability(browser, get_language):
    browser.get(link)
    # time.sleep(10)
    add_list = browser.find_elements(*Locators.add_button)
    assert len(add_list) > 0, f"Error: Add button is not available for language: {get_language}"
