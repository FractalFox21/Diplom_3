import allure
from data.constants import EMAIL
from pages.forgot_pass_page import ForgotPassPage
from pages.login_page import LoginPage
from data.URLS import URL_LOGIN, URL_FORGOT_PASS, URL_RESET_PASS
from pages.pass_recovery_page import PassRecoveryPage


class TestPassRecovery:

    @allure.title('Тест перехода на страницу "забыл пароль" по кнопке «Восстановить пароль».')
    def test_forgot_pass_click_recovery_button_url_forgot_pass(self, driver):
        forgot_pass = LoginPage(driver)
        forgot_pass.go_to_site(URL_LOGIN)
        forgot_pass.click_recover_pass_button()
        current_url = forgot_pass.current_url()
        assert URL_FORGOT_PASS in current_url, "Переход на страницу 'забыл пароль' не выполнен"

    @allure.title('Тест ввода почты и клик по кнопке «Восстановить», откроется страница восстановления.')
    def test_enter_mail_click_restore_button_url_recovery_pass(self, driver):
        forgot_pass = ForgotPassPage(driver)
        forgot_pass.go_to_site(URL_FORGOT_PASS)
        forgot_pass.enter_email(EMAIL)
        forgot_pass.click_recover_button()
        forgot_pass.wait_for_url(URL_RESET_PASS)
        current_url = forgot_pass.current_url()
        assert URL_RESET_PASS in current_url, "Переход на страницу восстановления не выполнен"

    @allure.title('На странице восстановления пароля клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_click_show_hide_pass_active_field(self, driver):
        forgot_pass = ForgotPassPage(driver)
        pass_rec = PassRecoveryPage(driver)
        forgot_pass.go_to_site(URL_FORGOT_PASS)
        forgot_pass.enter_email(EMAIL)
        forgot_pass.click_recover_button()
        forgot_pass.wait_for_url(URL_RESET_PASS)
        focus = pass_rec.password_field_focus_status()
        assert focus == False, "Поле в фокусе."
        pass_rec.click_show_hide_password_button()
        focus = pass_rec.password_field_focus_status()
        assert focus == True, "Поле пароля не стало активным после клика."
