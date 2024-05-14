import allure

import urls
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestOrderFeed:

    @allure.title('Проверка открытия окна детализации заказа')
    def test_open_order_modal(self,driver):
        feed_page = FeedPage(driver)

        driver.get(urls.FEED_PAGE)
        feed_page.wait_for_load_feed_page()
        feed_page.click_first_feed_order()
        element = feed_page.find_order_modal()

        assert element

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_users_order_in_feed(self, driver, user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)
        profile_page = ProfilePage(driver)

        driver.get(urls.BASE_URL)
        main_page.click_profile_link()
        login_page.fill_user_data_form(user['email'], user['password'])
        main_page.wait_for_load_main_page()
        ingredient = main_page.choose_ingredient()
        main_page.add_ingredient(ingredient)
        main_page.click_order_button()
        main_page.wait_create_order()
        main_page.close_order_modal()
        main_page.click_profile_link()

        profile_page.click_order_history_link()
        user_order_from_history = profile_page.get_user_order()

        main_page.click_feed_button()
        feed_page.wait_for_load_feed_page()
        user_order_from_feed = feed_page.get_order()

        assert user_order_from_history in user_order_from_feed

    @allure.title('Увеличение счетчика заказов за все время')
    def test_order_counter_all_time_increased(self, driver, user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        driver.get(urls.BASE_URL)
        main_page.click_profile_link()
        login_page.fill_user_data_form(user['email'], user['password'])
        main_page.wait_for_load_main_page()

        main_page.click_feed_button()
        feed_page.wait_for_load_feed_page()
        count_before = feed_page.get_count_of_orders_all_time()

        login_page.click_constructor_button()
        main_page.wait_for_load_main_page()
        ingredient = main_page.choose_ingredient()
        main_page.add_ingredient(ingredient)
        main_page.click_order_button()
        main_page.wait_create_order()
        main_page.close_order_modal()

        main_page.click_feed_button()
        feed_page.wait_for_load_feed_page()
        count_after = feed_page.get_count_of_orders_all_time()

        assert count_after == count_before + 1

    @allure.title('Увеличение счетчика заказов за день')
    def test_order_counter_by_day_increased(self, driver, user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        driver.get(urls.BASE_URL)
        main_page.click_profile_link()
        login_page.fill_user_data_form(user['email'], user['password'])
        main_page.wait_for_load_main_page()

        main_page.click_feed_button()
        feed_page.wait_for_load_feed_page()
        count_before = feed_page.get_count_of_orders_by_day()

        login_page.click_constructor_button()
        main_page.wait_for_load_main_page()
        ingredient = main_page.choose_ingredient()
        main_page.add_ingredient(ingredient)
        main_page.click_order_button()
        main_page.wait_create_order()
        main_page.close_order_modal()

        main_page.click_feed_button()
        feed_page.wait_for_load_feed_page()
        count_after = feed_page.get_count_of_orders_by_day()

        assert count_after == count_before + 1

    @allure.title('Отображение созданного заказа "В работе"')
    def test_created_order_in_work_list(self, driver,user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        driver.get(urls.BASE_URL)
        main_page.click_profile_link()
        login_page.fill_user_data_form(user['email'], user['password'])
        main_page.wait_for_load_main_page()

        login_page.click_constructor_button()
        main_page.wait_for_load_main_page()
        ingredient = main_page.choose_ingredient()
        main_page.add_ingredient(ingredient)
        main_page.click_order_button()
        main_page.wait_create_order()
        new_order = main_page.get_order_number()
        main_page.close_order_modal()

        main_page.click_feed_button()
        feed_page.wait_for_load_feed_page()
        order_in_work = feed_page.get_order_in_work()

        assert new_order in order_in_work

















