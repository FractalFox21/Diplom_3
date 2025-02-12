import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.locators import LocatorsProfile
from pages.home_page import HomePage


class ProfilePage(HomePage):

    @allure.step("Нажать на кнопку 'Итория заказов'")
    def click_on_order(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsProfile.ORDER_HISTORY_BUTTON))
        return self.find_element_located(LocatorsProfile.ORDER_HISTORY_BUTTON).click()

    @allure.step("Нажать на кнопку 'Выход'")
    def click_exit_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsProfile.LOGOUT))
        return self.find_element_located(LocatorsProfile.LOGOUT).click()


