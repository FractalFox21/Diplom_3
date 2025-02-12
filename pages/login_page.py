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

    @allure.step("Заполнить поле Email")
    def input_email(self, email):
        self.find_clickable_element(LocatorsLoginPage.FILED_EMAIL).send_keys(email)

    @allure.step("Заполнить поле Пароль")
    def input_password(self, password):
        self.find_clickable_element(LocatorsLoginPage.FILED_PASSWORD).send_keys(password)


    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        self.find_clickable_element(LocatorsLoginPage.BUTTON_LOGIN).click()