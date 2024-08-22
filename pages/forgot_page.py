import allure
import urls
from loactors.forgot_page_locators import ForgotPageLocators
from pages.base_page import BasePage


class ForgotPage(BasePage):

    @allure.step('Ожидаем загрузки страницы Восстановления пароля')
    def wait_for_forgot_page_loaded(self):
        self.wait_for_url(urls.FORGOT_PAGE)

    @allure.step('Заполняем поле "emai"')
    def fill_email_field(self, email):
        self.find_element_with_wait(ForgotPageLocators.EMAIL_FIELD)
        self.set_text_to_form(ForgotPageLocators.EMAIL_FIELD, email)

    @allure.step('Нажимаем кнопку "Восстановить"')
    def click_restore_button(self):
        self.find_element_with_wait(ForgotPageLocators.RESTORE_BUTTON)
        self.click_on_element(ForgotPageLocators.RESTORE_BUTTON)
