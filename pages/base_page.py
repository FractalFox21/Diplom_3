import allure

from data.URLS import URL_HOME_PAGE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from data.locators import LocatorsBasePage


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Перейти на сайт')
    @allure.description('Если URL сайта не задан, откроет домашнюю страницу')
    def go_to_site(self, url=None):
        if url is None:
            url = URL_HOME_PAGE
        self.driver.get(url)

    @allure.step("Нажать на кнопку 'Личный кабинет'")
    def click_office_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsBasePage.PER_OFFICE))
        return self.find_element_located(LocatorsBasePage.PER_OFFICE).click()

    @allure.step("Нажать на кнопку 'Конструктор'")
    def click_constructor_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsBasePage.CONSTR))
        return self.find_element_located(LocatorsBasePage.CONSTR).click()

    @allure.step("Нажать на кнопку 'Лента заказов'")
    def click_order_list_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsBasePage.ORDER_LIST))
        return self.find_element_located(LocatorsBasePage.ORDER_LIST).click()

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

    @allure.step('Подождать исчезновения элемента.')
    def wait_invisibility_element(self, locator):
        return WebDriverWait(self.driver, 50).until(EC.invisibility_of_element_located(locator))

    @allure.step('Перетащить элемент.')
    def drag_and_drop(self, source_element, target_element):
        browser_name = self.driver.capabilities['browserName']
        if browser_name == "chrome":
            action = ActionChains(self.driver)
            action.drag_and_drop(source_element, target_element).perform()
        elif browser_name == "firefox":
            self.driver.execute_script(
                """
                const dataTransfer = new DataTransfer();
                arguments[0].dispatchEvent(new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer }));
                arguments[1].dispatchEvent(new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer }));
                """,
                source_element,
                target_element,
            )
