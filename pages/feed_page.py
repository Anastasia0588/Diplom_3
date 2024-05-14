import allure
import urls
from loactors.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step('Ожидаем загрузки страницы "Лента заказов"')
    def wait_for_load_feed_page(self):
        self.wait_for_url(urls.FEED_PAGE)

    @allure.step('Кликаем на верхний заказ в ленте заказов')
    def click_first_feed_order(self):
        self.find_element_with_wait(FeedPageLocators.FIRST_ORDER)
        self.click_on_element(FeedPageLocators.FIRST_ORDER)

    @allure.step('Находим модальное окно Заказа')
    def find_order_modal(self):
        element = self.find_element_with_wait(FeedPageLocators.ORDER_MODAL_HEADER)
        return element

    @allure.step('Получаем номер заказа пользователя')
    def get_order(self):
        element = self.find_element_with_wait(FeedPageLocators.ORDERS)
        return element.text

    @allure.step('Получаем количество заказов за все время')
    def get_count_of_orders_all_time(self):
        element = self.find_element_with_wait(FeedPageLocators.ORDER_COUNTER_ALL_TIME)
        return int(element.text)

    @allure.step('Получаем количество заказов за сегодня')
    def get_count_of_orders_by_day(self):
        element = self.find_element_with_wait(FeedPageLocators.ORDER_COUNTER_BY_DAY)
        return int(element.text)

    @allure.step('Получить список заказов в работе')
    def get_order_in_work(self):
        self.find_element_with_wait(FeedPageLocators.EMPTY_ORDERS_IN_WORK)
        self.wait_disappear_element(FeedPageLocators.EMPTY_ORDERS_IN_WORK)
        element = self.find_element_with_wait(FeedPageLocators.ORDER_IN_WORK)
        return element.text.lstrip('#')
