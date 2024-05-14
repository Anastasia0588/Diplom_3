import allure
import urls
from loactors.reset_page_locators import ResetPageLocators
from pages.base_page import BasePage


class ResetPage(BasePage):

    @allure.step('Ожидаем загрузки страницы сброса пароля')
    def wait_for_reset_page_loaded(self):
        self.wait_for_url(urls.RESET_PAGE)

    @allure.step('Нажимаем на кнопку показа пароля')
    def click_on_show_password(self):
        self.find_element_with_wait(ResetPageLocators.SHOW_PASSWORD_BUTTON)
        self.click_on_element(ResetPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Получаем класс поля ввода пароля')
    def get_password_field_class(self):
        element_class = self.find_element_with_wait(ResetPageLocators.PASSWORD_FIELD).get_attribute('class')
        return element_class
