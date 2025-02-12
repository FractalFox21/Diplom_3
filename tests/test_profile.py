import allure
from data.locators import LocatorsHomePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from data.URLS import URL_LOGIN, URL_PROFILE, URL_ORDER_HISTORY
from pages.profile_page import ProfilePage


class TestProfile:
    @allure.title('Тест перехода на страницу авторизации по кнопке «Личный кабинет».')
    def test_button_per_office_login_home_page(self, driver):
        login = LoginPage(driver)
        login.go_to_site()
        login.find_clickable_element(LocatorsHomePage.PER_OFFICE).click()
        current_url = login.current_url()
        assert URL_LOGIN == current_url

    @allure.title('Тест перехода на страницу профиля по кнопке «Личный кабинет», авторизованный  пользователь.')
    def test_button_per_office_login_home_page(self, authorization):
        login = HomePage(authorization)
        login.click_office_button()
        current_url = login.current_url()
        assert URL_PROFILE  == current_url

    @allure.title('Тест перехода на страницу истории заказов по кнопке «История заказов».')
    def test_button_per_office_login_home_page(self, authorization):
        user = ProfilePage(authorization)
        user.click_office_button()
        user.click_order_history_button()
        current_url = user.current_url()
        assert URL_ORDER_HISTORY  == current_url

    @allure.title('Тест выхода из личного кабинета по кнопке «Выход».')
    def test_button_per_office_login_home_page(self, authorization):
        user = ProfilePage(authorization)
        user.click_office_button()
        user.click_exit_button()
        user.wait_for_url(URL_LOGIN)
        current_url = user.current_url()
        assert URL_LOGIN  == current_url
