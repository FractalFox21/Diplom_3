import allure
import pytest

from pages.home_page import BasePage, HomePage
from data.URLS import  URL_ORDER_LIST, URL_HOME_PAGE



class TestFunctional:

    @pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)
    @allure.title('Тест перехода на страницу конструктора по кнопке «Конструктор».')
    def test_button_constructor_through_order_feeds_home_page(self, driver):
        user = HomePage(driver)
        user.go_to_site(URL_ORDER_LIST)
        user.click_constructor_button()
        current_url = user.current_url()
        assert URL_HOME_PAGE == current_url, "Переход на страницу 'конструктор' не выполнен."

    @pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)
    @allure.title('Тест перехода на страницу заказов по кнопке «Лента заказов».')
    def test_button_order_list_through_constructor_page_order_list_page(self, driver):
        user = HomePage(driver)
        user.go_to_site()
        user.click_order_list_button()
        current_url = user.current_url()
        assert URL_ORDER_LIST == current_url, "Переход на страницу 'лента заказов' не выполнен."

    @pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)
    @allure.title('Тест если кликнуть на ингредиент, появится всплывающее окно с деталями.')
    def test_button_ingredients_open_details(self, driver):
        user = HomePage(driver)
        user.go_to_site()
        user.click_bun()
        control_el = user.check_pop_up_details()
        assert control_el.is_displayed(), "Элемент не найден или не видим"

    @pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)
    @allure.title('Тест закрытия всплывающего окна по крестику.')
    def test_click_the_cross_pop_up_close(self, driver):
        user = HomePage(driver)
        user.go_to_site()
        user.click_bun()
        control_el = user.check_pop_up_details()
        user.click_exit_bun_details()
        user.wait_invisibility_pop_up()
        assert control_el.is_displayed() == False, "Закрытие окна не выполнено."

    @pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)
    @allure.title('Тест при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента.')
    def test_add_ingredient_counter_increments_counter_two(self, driver):
        user = HomePage(driver)
        user.go_to_site()
        user.add_ingredient_to_order()
        assert user.get_counter_increments() == True, "Каунтер не увеличен."

    @pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)
    @allure.title('Тест авторизованный пользователь может оформить заказ')
    def test_auth_user_can_place_an_order(self, authorization):
        user = HomePage(authorization)
        user.go_to_site()
        user.add_ingredient_to_order()
        user.click_place_order()
        assert user.check_order_status(), "Заказ не оформлен"


