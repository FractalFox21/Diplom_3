import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.locators import LocatorsLoginPage
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Нажать на кнопку 'Восстановить пароль'")
    def click_recover_pass_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsLoginPage.RECOVER_PASS_BUTTON))
        return self.find_element_located(LocatorsLoginPage.RECOVER_PASS_BUTTON).click()