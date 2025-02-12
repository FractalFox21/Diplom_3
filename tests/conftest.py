import pytest
import requests
from selenium import webdriver

from data.URLS import URL_LOGIN, URL_HOME_PAGE
from data.constants import TEST_EMAIL, TEST_PASSWORD
from data.generator import GenerateUsers
from data.handles import URL_USER
from data.queries import Queries
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

#фикстура для создания и удаления временного пользователя
@pytest.fixture(scope='function')
def create_and_delete_user():
    user = GenerateUsers.generate_fake_user()
    response = Queries.post_create_user(data=user)
    token = response.json()['accessToken']
    yield user , token , response
    requests.delete(f'{URL_HOME_PAGE}{URL_USER}', headers={'Authorization': f'{token}'})




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