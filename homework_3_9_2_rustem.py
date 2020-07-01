from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from re import search
import time


def empty_basket_workaround(browser):
    browser.get("http://selenium1py.pythonanywhere.com/en-gb/basket/")

    quantity = browser.find_elements_by_css_selector(".checkout-quantity .input-group input")
    update = browser.find_elements_by_css_selector(".checkout-quantity .input-group button")

    for qa in quantity:
        qa.clear()
        qa.send_keys('0')
    for upd in update:
        upd.click()


def test_case_after_all(browser):
    # time.sleep(5)
    browser.quit()


def test_case_01_adding_to_basket():
    """
    Positive case: Adding an item to basket
    1) Open catalog by link
    2) Add item "Hacking Exposed Wireless" to basket
    Expected: Message which contains "Hacking Exposed Wireless" substring
    """

    browser = webdriver.Chrome()
    try:
        browser.get("http://selenium1py.pythonanywhere.com/en-gb/catalogue/")

        title = "Hacking Exposed Wireless"

        xpath_add = "//a[text()='{title}']/ancestor::li//button".format(title=title)
        add_button = browser.find_element_by_xpath(xpath_add)
        add_button.click()

        WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div/*[text()[contains(., '{title}')]]".format(title=title)), title))

        success_e = browser.find_element_by_xpath("//div/*[text()[contains(., '{title}')]]".format(title=title))
        success_message = success_e.text

        assert title == success_message, "Adding an item to basked has been failed!"
    finally:
        test_case_after_all(browser)


def test_case_02_opening_basket():
    """
    Positive case: Checking item in the basket
    1) Open catalog by link
    2) Add item "Coders at Work" to basket
    3) Open basket and compare price and title with just added item
    Expected: Price and title matches
    """

    browser = webdriver.Chrome()
    try:
        browser.get("http://selenium1py.pythonanywhere.com/en-gb/catalogue/")

        title = "Coders at Work"
        xpath_price = "//a[text()='{title}']/ancestor::li//p[@class='price_color']".format(title=title)
        price_element = browser.find_element_by_xpath(xpath_price)
        price = price_element.text

        xpath_add = "//a[text()='{title}']/ancestor::li//button".format(title=title)
        add_button = browser.find_element_by_xpath(xpath_add)
        add_button.click()

        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".alertinner a.btn-info")))

        view_button = browser.find_element_by_css_selector(".alertinner a:nth-child(1)")
        view_button.click()

        xpath_title = "//a[text()='{title}']".format(title=title)
        add_title_el = browser.find_element_by_xpath(xpath_title)
        add_title = add_title_el.text

        add_price_el = browser.find_element_by_css_selector(".basket-items .col-sm-1 .price_color")
        add_price = add_price_el.text

        assert (title == add_title) and (price == add_price), "Checking item in the basket has been failed!"
    finally:
        test_case_after_all(browser)


def test_case_basket_actions_before(browser):
    browser.get("http://selenium1py.pythonanywhere.com/en-gb/catalogue/")

    title = "Hacking Exposed Wireless"
    xpath_add = "//a[text()='{title}']/ancestor::li//button".format(title=title)
    add_button = browser.find_element_by_xpath(xpath_add)
    add_button.click()
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div/*[text()[contains(., '{title}')]]".format(title=title)), title))


def test_case_03_checkout_new_user():
    """
    Positive case: Finishing the order
    Precondition: "Hacking Exposed Wireless" is added to basket
    1) Open basket by link
    2) Click Checkout now
    3) Fill first name / last name / first addr / city / zip code / country on Shipping address form
    4) Click continue on Payment form
    5) Click place order on Preview page
    Expected: Confirmation form is opened with order #
    """
    browser = webdriver.Chrome()
    test_case_basket_actions_before(browser)
    try:
        browser.get("http://selenium1py.pythonanywhere.com/en-gb/basket/")

        che_button = browser.find_element_by_xpath("//a[text()='Proceed to checkout']")
        che_button.click()

        # Checkout gateway
        WebDriverWait(browser, 10).until(EC.title_contains("Checkout gateway"))
        input_email = browser.find_element_by_css_selector("#id_username")
        input_email.send_keys("angmar@mordor.com")
        # Workaround
        input_passw = browser.find_element_by_css_selector("#id_password")
        input_passw.send_keys("123")
        ############
        cont_guest = browser.find_element_by_css_selector(".btn-primary")
        cont_guest.click()

        # Shipping address
        WebDriverWait(browser, 10).until(EC.title_contains("Shipping address"))
        input_fname = browser.find_element_by_css_selector("#id_first_name")
        input_fname.send_keys("Angmar")
        input_lname = browser.find_element_by_css_selector("#id_last_name")
        input_lname.send_keys("King")
        input_addr = browser.find_element_by_css_selector("#id_line1")
        input_addr.send_keys("Middle-earth, Mordor")
        input_city = browser.find_element_by_css_selector("#id_line4")
        input_city.send_keys("Mordor")
        input_zip = browser.find_element_by_css_selector("#id_postcode")
        input_zip.send_keys("194021")
        select_country = Select(browser.find_element_by_css_selector("#id_country"))
        select_country.select_by_visible_text("Russian Federation")

        cont_button = browser.find_element_by_css_selector(".btn-primary")
        cont_button.click()

        # Payment details
        cont_pay_button = browser.find_element_by_css_selector(".btn-primary")
        cont_pay_button.click()

        # Preview order
        order_button = browser.find_element_by_css_selector(".btn-primary")
        order_button.click()

        # Order confirmation
        conf_xpath = "//h1[text()[contains(., 'confirmation')]]"
        conf_element = browser.find_element_by_xpath(conf_xpath)
        confirmation_message = conf_element.text
        order_num_exists = search(r'\d+', confirmation_message) is not None

        assert order_num_exists, "Ordering has failed or there is no order number"
    finally:
        test_case_after_all(browser)


def test_case_04_editing_quantity():
    """
    Positive case: Editing item's quantity
    Precondition: "Hacking Exposed Wireless" is added to basket
    1) Open basket by link
    2) Increase item quantity by 1
    3) Click Update button
    Expected: Total is twice bigger than Price
    """
    browser = webdriver.Chrome()
    test_case_basket_actions_before(browser)
    try:
        browser.get("http://selenium1py.pythonanywhere.com/en-gb/basket/")

        quantity = browser.find_element_by_css_selector(".input-group .form-control")
        quantity.clear()
        quantity.send_keys('2')

        update = browser.find_element_by_css_selector(".input-group .btn-default")
        update.click()

        updated = "Your basket total is now"
        WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//p[text()[contains(., '{upd_mess}')]]".format(upd_mess=updated)), updated))

        add_price_el = browser.find_element_by_css_selector(".basket-items .col-sm-1 .price_color")
        add_price = add_price_el.text[1:]

        add_total_el = browser.find_element_by_css_selector(".basket-items .col-sm-2 .price_color")
        add_total = add_total_el.text[1:]

        if add_price == "" or add_total == "":
            raise AssertionError('There is no Price or Total')

        price = float(add_price)
        total = float(add_total)

        assert total == 2*price, "Quantity checking error"
    finally:
        test_case_after_all(browser)


def test_case_05_empty_basket():
    """
    Positive case: Deleting items from basket
    Precondition: "Hacking Exposed Wireless" is added to basket
    1) Open basket by link
    2) Click Remove fot the item
    Expected: Basket is empty message
    """
    browser = webdriver.Chrome()
    test_case_basket_actions_before(browser)
    try:
        browser.get("http://selenium1py.pythonanywhere.com/en-gb/basket/")

        remove = browser.find_element_by_css_selector("a[data-behaviours='remove']")
        remove.click()
        # empty_basket_workaround(browser)

        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alertinner p:first-child")))
        empty_message = "Your basket is now empty"
        message = browser.find_element_by_css_selector(".alertinner p:first-child")
        assert message.text == empty_message, "Deleting items from basket error"
    finally:
        test_case_after_all(browser)


if __name__ == '__main__':
    test_case_01_adding_to_basket()
    test_case_02_opening_basket()
    test_case_03_checkout_new_user()
    test_case_04_editing_quantity()
    test_case_05_empty_basket()
