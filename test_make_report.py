from locators import Locators
from random import randint

link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_registered_user_authorized(browser, get_language):
    """
    Positive case: Registered user is automatically authorized
    1) Open registration form
    2) Fill email
    3) Fill password
    4) Fill confirmation password
    5) Click register
    Expected: User is authorized and can see accounts links
    """
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element(*Locators.EMAIL_FIELD).send_keys(f'angmar-{randint(1, 10000)}@mordor.uk')
    browser.find_element(*Locators.PWD1).send_keys('angmar123!')
    browser.find_element(*Locators.PWD2).send_keys('angmar123!')
    browser.find_element(*Locators.REG_BUTTON).click()
    profile_link = browser.find_elements(*Locators.PROFILE_LINK)
    assert len(profile_link) > 0, f'Error during user registration on language: {get_language}'
