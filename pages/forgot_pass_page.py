import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.locators import LocatorsForgotPage, LocatorsPassRecovery
from pages.base_page import BasePage


class ForgotPassPage(BasePage):

    @allure.step("Ввести email")
    def enter_email(self, email):
        return self.driver.find_element(*LocatorsForgotPage.EMAIL_INPUT).send_keys(email)

    @allure.step("Нажать на кнопку 'Восстановить'")
    def click_recover_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsForgotPage.RECOVER_BUTTON))
        return self.find_element_located(LocatorsForgotPage.RECOVER_BUTTON).click()

    @allure.step("Проверить фокус поля 'пароль'.")
    def get_focus_status_field_pass(self):
        focus_type = self.get_type(LocatorsPassRecovery.FIELD_PASS)
        return focus_type