import allure
import urls
from pages.forgot_page import ForgotPage
from pages.login_page import LoginPage
from pages.reset_page import ResetPage


class TestResetPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_open_forgot_page(self, driver):
        login_page = LoginPage(driver)
        forgot_page = ForgotPage(driver)

        driver.get(urls.LOGIN_PAGE)
        login_page.click_restore_password()
        forgot_page.wait_for_forgot_page_loaded()
        result_url = forgot_page.get_current_url()

        assert result_url == urls.FORGOT_PAGE

    @allure.title('Проверка переход на страницу сброса пароля по кнопке «Восстановить»')
    def test_open_reset_page(self, driver):
        forgot_page = ForgotPage(driver)
        reset_page = ResetPage(driver)

        driver.get(urls.FORGOT_PAGE)
        forgot_page.fill_email_field('test@email.ru')
        forgot_page.click_restore_button()
        reset_page.wait_for_reset_page_loaded()
        result_url = forgot_page.get_current_url()

        assert result_url == urls.RESET_PAGE

    @allure.title('Проверка что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_password(self,driver):
        forgot_page = ForgotPage(driver)
        reset_page = ResetPage(driver)

        driver.get(urls.FORGOT_PAGE)
        forgot_page.fill_email_field('test@email.ru')
        forgot_page.click_restore_button()
        reset_page.wait_for_reset_page_loaded()
        reset_page.click_on_show_password()
        element_class = reset_page.get_password_field_class()

        assert 'input_status_active' in element_class
