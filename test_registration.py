import time
from locators import Locators
from random import randint

link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_register_new_user(browser, get_language):
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element(*Locators.email_field).send_keys(f'angmar-{randint(1, 10000)}@mordor.gb')
    browser.find_element(*Locators.pwd1_field).send_keys('angmar123!')
    browser.find_element(*Locators.pwd2_field).send_keys('angmar123!')
    browser.find_element(*Locators.reg_button).click()
    # time.sleep(10)
    profile_link = browser.find_elements(*Locators.profile_link)
    assert len(profile_link) > 0, 'Error during user registration'
