import pytest
from selenium import webdriver

from data.URLS import URL_LOGIN
from data.constants import TEST_EMAIL, TEST_PASSWORD
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture
def authorization(driver, email = TEST_EMAIL, password = TEST_PASSWORD):
    user = LoginPage(driver)
    user.go_to_site(URL_LOGIN)
    user.input_email(email)
    user.input_password(password)
    user.click_login_button()
    return driver


'''

@pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)


@pytest.fixture(params=['firefox','chrome'])
def driver(request):
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
    else:
        raise ValueError ('Unknown browser')

    yield browser
    browser.quit()
    
'''