import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.locators import LocatorsHomePage
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step("Клик по булке")
    def click_bun(self):
        self.find_clickable_element(LocatorsHomePage.BUN).click()

    @allure.step("Проверка всплывающего окна.")
    def check_pop_up_details(self):
        return self.find_element_located(LocatorsHomePage.POP_UP_BUN)

    @allure.step("Клик по закрытию всплывающего окна.")
    def click_exit_bun_details(self):
        self.find_clickable_element(LocatorsHomePage.EXIT_WINDOW).click()

    @allure.step("Подождать закрытия всплывающего окна.")
    def wait_invisibility_pop_up(self):
        self.wait_invisibility_element(LocatorsHomePage.POP_UP_BUN)

    @allure.step("Перенос булки в корзину")
    def add_ingredient_to_order(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsHomePage.BUN))
        bun = self.find_clickable_element(LocatorsHomePage.BUN)
        place = self.find_clickable_element(LocatorsHomePage.PLACE)
        self.drag_and_drop(bun, place)

    @allure.step("Проверить увеличение каунтера.")
    def get_counter_increments(self):
        self.find_element_located(LocatorsHomePage.CAUNTER_STATUS)
        return self.get_text(LocatorsHomePage.CAUNTER_STATUS) == "2"

    @allure.step("Нажать кнопку 'оформить заказ'")
    def click_place_order(self):
        self.find_clickable_element(LocatorsHomePage.BUTTON_PLACE_ORDER).click()

    @allure.step("Проверить оформление заказа.")
    def check_order_status(self):
        return self.find_element_located(LocatorsHomePage.ORDER_STATUS)
