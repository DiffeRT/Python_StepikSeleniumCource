from selenium.common.exceptions import NoSuchElementException
from locators import Locators
from random import randint


def go_to_login_page(browser):
    login = browser.find_element(*Locators.LOGIN_LINK)
    login.click()


def fill_registration_form(browser):
    browser.find_element(*Locators.EMAIL_FIELD).send_keys(f'angmar-{randint(1, 10000)}@mordor.uk')
    browser.find_element(*Locators.PWD1).send_keys('angmar123!')
    browser.find_element(*Locators.PWD2).send_keys('angmar123!')


registration_text = {
    'en-gb': "Thanks for registering!",
    'ru': "Спасибо за регистрацию!",
    'es': "Gracias por registrarse!"
}


def is_success_registration(browser, get_language):
    try:
        success_element = browser.find_element(*Locators.SUCCESS_ELEM)
        success_message = success_element.text
        if get_language in registration_text:
            expected = registration_text[get_language]
        else:
            return False
        return success_message == expected
    except NoSuchElementException:
        return False


def test_registered_user_authorized(browser, get_language):
    """
    Positive case: Registered user is automatically authorized
    1) Open registration form
    2) Fill email
    3) Fill password
    4) Fill confirmation password
    5) Click register
    Expected: User is authorized and can see success message
    """
    link = "http://selenium1py.pythonanywhere.com"
    browser.get(link)
    go_to_login_page(browser)
    fill_registration_form(browser)
    browser.find_element(*Locators.REG_BUTTON).click()
    assert is_success_registration(browser, get_language), 'Wrong message after user registration'
