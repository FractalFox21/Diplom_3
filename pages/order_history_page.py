import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.locators import LocatorsProfile, LocatorsProfileOrder, LocatorsBasePage
from pages.profile_page import ProfilePage


class OrderHistoryPage(ProfilePage):

    @allure.step("Нажать на 'заказ'")
    def click_on_order(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsProfile.ORDER_HISTORY_BUTTON))
        return self.find_element_located(LocatorsProfile.ORDER_HISTORY_BUTTON).click()

    @allure.step("Нажать на кнопку 'лента заказов'")
    def click_order_list_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsBasePage.ORDER_LIST))
        return self.find_element_located(LocatorsBasePage.ORDER_LIST).click()

    @allure.step("Нажать на заказ в списке заказов")
    def click_order(self):
        self.find_clickable_element(LocatorsProfileOrder.CONTROL_ORDER).click()

    @allure.step("Проверка всплывающего окна")
    def check_pop_up_order(self):
        return self.find_element_located(LocatorsProfileOrder.POP_UP_ORDER)

    @allure.step("Получить номер последнего заказа пользователя")
    def get_last_order(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LocatorsProfileOrder.CONTROL_ORDER))
        self.find_clickable_element(LocatorsProfileOrder.CONTROL_ORDER)
        element = self.driver.find_elements(*LocatorsProfileOrder.CONTROL_ORDER)
        if not element:
            raise Exception("Нет искомых заказов в истори.")
        return element[-1].text


    @allure.step("Проверить наличие последнего заказа из 'истории заказов' в 'Ленте заказов'")
    def check_last_order(self, control_order):
        numbers = self.find_all_elements(LocatorsProfileOrder.ORDER_LIST)
        for number in numbers:
            if control_order == number.text:
                return True
        return True

    @allure.step("Ожидание прогрузки заказа в ленту готовых заказов.")
    def wait_order_in_work(self, order):
        numbers = self.find_all_elements(LocatorsProfileOrder.ORDERS_IN_WORK)
        for number in numbers:
            if order == number.text:
                return True
        return True
