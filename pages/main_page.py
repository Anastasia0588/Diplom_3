import allure
import urls
from loactors.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from random import choice


class MainPage(BasePage):

    @allure.step('Нажимаем на кнопку Личный кабинет')
    def click_profile_link(self):
        self.find_element_with_wait(MainPageLocators.PROFILE_LINK)
        self.click_on_element(MainPageLocators.PROFILE_LINK)


    @allure.step('Нажимаем на кнопку "Войти в аккаунт"')
    def click_login_button(self):
        self.find_element_with_wait(MainPageLocators.LOGIN_BUTTON_FROM_MAIN_PAGE)
        self.click_on_element(MainPageLocators.LOGIN_BUTTON_FROM_MAIN_PAGE)

    @allure.step('Ожидаем загрузки главной страницы')
    def wait_for_load_main_page(self):
        self.wait_for_url(urls.BASE_URL)
        self.find_element_with_wait(MainPageLocators.INGREDIENTS_LIST)

    @allure.step('Нажимаем на кнопку "Лента заказов"')
    def click_feed_button(self):
        self.find_element_with_wait(MainPageLocators.FEED_BUTTON)
        self.click_on_element(MainPageLocators.FEED_BUTTON)

    @allure.step('Нажимаем на ингредиент')
    def click_on_ingredient(self):
        self.find_element_with_wait(MainPageLocators.FIRST_INGREDIENT)
        self.click_on_element(MainPageLocators.FIRST_INGREDIENT)

    @allure.step('Находим модальное окно Деталей ингредиента')
    def find_ingredient_modal(self):
        element = self.find_element_with_wait(MainPageLocators.INGREDIENT_MODAL_HEADER)
        return element

    @allure.step('Закрываем модальное окно Деталей ингредиента')
    def close_ingredient_modal(self):
        self.find_element_with_wait(MainPageLocators.CLOSE_MODAL_BUTTON)
        self.click_on_element(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step('Проверяем видимость модального окна деталей ингредиента')
    def check_visibility_modal(self):
        return self.check_visibility_of_element(MainPageLocators.INGREDIENT_MODAL_HEADER)

    @allure.step('Выбираем ингредиент из списка')
    def choose_ingredient(self):
        ingredients = self.driver.find_elements(*MainPageLocators.INGREDIENTS_LIST)
        selected_ingredient = choice(ingredients)
        return selected_ingredient

    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredient(self, ingredient):
        basket = self.find_element_with_wait(MainPageLocators.BASKET)
        self.drag_n_drop(ingredient, basket)

    @allure.step('Находим счетчик выбранного ингредиента')
    def get_actual_counter(self, ingredient):
        ingredient_count = ingredient.text[0]
        return int(ingredient_count)

    @staticmethod
    def expected_count(ingredient):
        ingredient_type = ingredient.text
        if 'булка' in ingredient_type:
            counter = 2
        else:
            counter = 1
        return int(counter)

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_order_button(self):
        self.find_element_with_wait(MainPageLocators.ORDER_BUTTON)
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Находим модальное окно заказа')
    def find_order_modal(self):
        element = self.find_element_with_wait(MainPageLocators.ORDER_MODAL_HEADER)
        return element

    @allure.step('Закрываем окно заказа')
    def close_order_modal(self):
        self.find_element_with_wait(MainPageLocators.CLOSE_ORDER_BUTTON)
        self.click_on_element(MainPageLocators.CLOSE_ORDER_BUTTON)

    @allure.step('Ожидаем обновление номера заказа')
    def wait_create_order(self):
        order_number = "9999"
        while order_number == "9999":
            order_number = self.find_element_with_wait(MainPageLocators.ORDER_NUMBER).text
        return order_number

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        element = self.find_element_with_wait(MainPageLocators.ORDER_NUMBER)
        return element.text
