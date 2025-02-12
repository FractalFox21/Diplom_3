import allure
import pytest

from pages.home_page import BasePage
from data.URLS import URL_LOGIN, URL_PROFILE, URL_ORDER_HISTORY
from pages.profile_page import ProfilePage


class TestProfile:

    @pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)
    @allure.title('Тест перехода на страницу авторизации по кнопке «Личный кабинет».')
    def test_button_per_office_login_page(self, driver):
        login = BasePage(driver)
        login.go_to_site()
        login.click_office_button()
        current_url = login.current_url()
        assert URL_LOGIN == current_url

    @pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)
    @allure.title('Тест перехода на страницу профиля по кнопке «Личный кабинет», авторизованный  пользователь.')
    def test_button_per_office_login_open_profile_page(self, authorization):
        login = BasePage(authorization)
        login.click_office_button()
        current_url = login.current_url()
        assert URL_PROFILE  == current_url

    @pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)
    @allure.title('Тест перехода на страницу истории заказов по кнопке «История заказов».')
    def test_button_order_history_open_order_history(self, authorization):
        user = ProfilePage(authorization)
        user.click_office_button()
        user.click_on_order()
        current_url = user.current_url()
        assert URL_ORDER_HISTORY  == current_url

    @pytest.mark.parametrize("driver", ("chrome", "firefox"), indirect=True)
    @allure.title('Тест выхода из личного кабинета по кнопке «Выход».')
    def test_button_exit_through_profile_open_login_page(self, authorization):
        user = ProfilePage(authorization)
        user.click_office_button()
        user.click_exit_button()
        user.wait_for_url(URL_LOGIN)
        current_url = user.current_url()
        assert URL_LOGIN  == current_url
