import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from data.locators import LocatorsPassRecovery


class PassRecoveryPage(BasePage):


    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_hide_password_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsPassRecovery.SHOW_HIDE_BUTTON))
        return self.driver.find_element(*LocatorsPassRecovery.SHOW_HIDE_BUTTON).click()






    def password_field_focus_status(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsPassRecovery.PASS_INPUT_FIELD))
        class_attribute =  self.driver.find_element(LocatorsPassRecovery.PASS_INPUT_FIELD).get_attribute('class')

        #return "input_active" in class_attribute
        return class_attribute



    #def password_field_focus_status(self):
       # password_input = self.find_element(LocatorsPassRecovery.PASS_INPUT)
       # class_attribute = password_input.get_attribute("class")

        # Проверяем наличие класса, указывающего на активность (например, "input_active")
       # return "input_active" in class_attribute

        #field_pass = self.find_element(LocatorsPassRecovery.PASS_INPUT)
        #return field_pass == self.driver.switch_to.active_element

