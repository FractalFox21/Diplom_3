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

    @allure.step('Получить текущий url')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Подождать загрузку страницы')
    def wait_for_url(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))

    @allure.step('Получить тип элемента.')
    def get_type(self, locator):
        type_el = self.find_element_located(locator).get_attribute("type")
        return type_el


    #@allure.step('Переключиться на открывшуюся страницу')
    #def switch_window(self, window_number: int=1):
     #   return self.driver.switch_to.window(self.driver.window_handles[window_number])

'''
    def find_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator),
                message=f"Элементы {locator} не найдены")
    
'''