import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from data.locators import LocatorsPassRecovery


class PassRecoveryPage(BasePage):


    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_hide_pass_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsPassRecovery.SHOW_HIDE_BUTTON))
        return self.driver.find_element(*LocatorsPassRecovery.SHOW_HIDE_BUTTON).click()

    @allure.step("Получить фокус статус поля 'пароль'")
    def get_focus_status_field_pass(self):
        return self.get_type(LocatorsPassRecovery.FIELD_PASS)

