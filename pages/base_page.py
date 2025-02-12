import allure

from data.URLS import URL_HOME_PAGE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Перейти на сайт')
    @allure.description('Если URL сайта не задан, откроет домашнюю страницу')
    def go_to_site(self, url=None):
        if url is None:
            url = URL_HOME_PAGE
        self.driver.get(url)

    @allure.step('Получить кликабельный элемент.')
    def find_clickable_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Подождать загрузку элемента на странице.')
    def find_element_located(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Подождать загрузку всех искомых элементов.')
    def find_all_elements(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Получить текущий url')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Подождать загрузку страницы')
    def wait_for_url(self, expected_url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

    @allure.step('Получить тип элемента.')
    def get_type(self, locator):
        type_el = self.find_element_located(locator).get_attribute("type")
        return type_el

    @allure.step('Получить текст элемента.')
    def get_text(self, locator):
        text = self.find_clickable_element(locator).text
        return text
