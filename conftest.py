import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="Chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en-gb", help="Select language: en-gb, ru, es, ect...")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "Chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    browser.implicitly_wait(10)

    yield browser
    browser.quit()


@pytest.fixture
def get_language(request):
    return request.config.getoption("language")