import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


W_WIDTH = 1280
W_HEIGHT = 960


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", help="Select language: en-gb, ru, es, ect...")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    language = request.config.getoption("language")
    browser = None
    if browser_name.lower() == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name.lower() == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise Exception(f"Unknown browser name: {browser_name}. Choose chrome or firefox")
    browser.set_window_size(W_WIDTH, W_HEIGHT)

    yield browser
    browser.quit()


@pytest.fixture
def get_language(request):
    return request.config.getoption("language")
