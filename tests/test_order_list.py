import allure
import pytest

from data.URLS import URL_ORDER_LIST
from data.constants import ORDER
from data.locators import LocatorsProfileOrder
from data.queries import Queries
from pages.home_page import HomePage
from pages.order_history_page import OrderHistoryPage


class TestsOrderHistory:

    @pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)
    @allure.title('Тест если кликнуть на заказ, откроется всплывающее окно с деталями.')
    def test_click_order_open_order_info(self, driver):
        user = OrderHistoryPage(driver)
        user.go_to_site(URL_ORDER_LIST)
        user.click_order()
        control_el = user.check_pop_up_order()
        assert control_el.is_displayed(), "Элемент не найден или не видим"

    @pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)
    @allure.title('Тест заказ пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_in_history_list_and_full_order_list(self, authorization):
        user = OrderHistoryPage(authorization)
        user.click_office_button()
        user.click_on_order()
        control_order= user.get_last_order()
        user.click_order_list_button()
        assert user.check_last_order(control_order) == True

    @pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)
    @allure.title('Тест при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_new_order_change_last_order_number(self, driver, create_and_delete_user):
        user = HomePage(driver)
        api_user = create_and_delete_user
        user.go_to_site(URL_ORDER_LIST)
        last_number = user.get_text(LocatorsProfileOrder.ALL_TIME_ORDERS)
        Queries.post_create_order(data=ORDER, token=api_user[1])
        new_order = user.get_text(LocatorsProfileOrder.ALL_TIME_ORDERS)
        assert new_order > last_number

    @pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)
    @allure.title('Тест при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_new_order_change_today_orders(self, driver, create_and_delete_user):
        user = HomePage(driver)
        api_user = create_and_delete_user
        user.go_to_site(URL_ORDER_LIST)
        last_number = user.get_text(LocatorsProfileOrder.TODAY_ORDERS)
        Queries.post_create_order(data=ORDER, token=api_user[1])
        new_order = user.get_text(LocatorsProfileOrder.TODAY_ORDERS)
        assert new_order > last_number

    @pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)
    @allure.title('Тест после оформления заказа его номер появляется в разделе "В работе"')
    def test_new_order_have_in_work(self, driver, create_and_delete_user):
        user = OrderHistoryPage(driver)
        api_user = create_and_delete_user
        user.go_to_site(URL_ORDER_LIST)
        response = Queries.post_create_order(data=ORDER, token=api_user[1])
        assert user.wait_order_in_work(response) == True
