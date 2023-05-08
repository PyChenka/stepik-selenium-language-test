import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru', help="Please select a language. Default - 'ru'")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language:
        print(language)
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print(f"\nstart chrome browser({language}) for test..")
        browser = webdriver.Chrome(options=options)
    else:
        print("\nstart chrome browser(ru) for test..")
        browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()