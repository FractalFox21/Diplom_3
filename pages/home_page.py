import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.locators import LocatorsHomePage
from pages.base_page import BasePage


class HomePage(BasePage):


    @allure.step("Нажать на кнопку 'Личный кабинет'")
    def click_office_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsHomePage.PER_OFFICE))
        return self.find_element_located(LocatorsHomePage.PER_OFFICE).click()
