import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


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