import allure
from loactors.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Заполняем поле ')
    def fill_email_field(self, email):
        self.set_text_to_form(LoginPageLocators.EMAIL_AUTH_FIELD, email)

    @allure.step('Заполняем поле "Пароль"')
    def fill_password_field(self, password):
        self.set_text_to_form(LoginPageLocators.PWD_AUTH_FIELD, password)

    @allure.step('Заполняем форму авторизации пользователя')
    def fill_user_data_form(self, email, password):
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Кликаем по кнопке "Восстановить пароль"')
    def click_restore_password(self):
        self.find_element_with_wait(LoginPageLocators.RESTORE_PASS_LINK)
        self.click_on_element(LoginPageLocators.RESTORE_PASS_LINK)

    @allure.step('Кликаем по кнопке "Констурктор"')
    def click_constructor_button(self):
        self.find_element_with_wait(LoginPageLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(LoginPageLocators.CONSTRUCTOR_BUTTON)
