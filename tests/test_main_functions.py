import allure
import urls
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainFunctions:

    @allure.title('Проверка перехода на главную страницу по клику на кнопку "Конструктор"')
    def test_open_constructor(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        driver.get(urls.LOGIN_PAGE)
        login_page.click_constructor_button()
        main_page.wait_for_load_main_page()
        result_url = main_page.get_current_url()

        assert result_url == urls.BASE_URL

    @allure.title('Проверка перехода в Ленту заказов')
    def test_open_order_feed(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        driver.get(urls.BASE_URL)
        main_page.wait_for_load_main_page()
        main_page.click_feed_button()
        feed_page.wait_for_load_feed_page()
        result_url = feed_page.get_current_url()

        assert result_url == urls.FEED_PAGE

    @allure.title('Проверка, что по клику на ингредиент, появится всплывающее окно с деталями')
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        driver.get(urls.BASE_URL)
        main_page.wait_for_load_main_page()
        main_page.click_on_ingredient()
        element = main_page.find_ingredient_modal()
        assert element

    @allure.title('Проверка, что по клику на крестик всплывающее окно с деталями закрывается')
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        driver.get(urls.BASE_URL)
        main_page.wait_for_load_main_page()
        main_page.click_on_ingredient()
        main_page.find_ingredient_modal()
        main_page.close_ingredient_modal()
        visibility = main_page.check_visibility_modal()

        assert visibility is False

    @allure.title('Проверка, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_added_ingredient_increased_counter(self, driver):
        main_page = MainPage(driver)

        driver.get(urls.BASE_URL)
        main_page.wait_for_load_main_page()
        ingredient = main_page.choose_ingredient()
        main_page.add_ingredient(ingredient)
        expected_count = main_page.expected_count(ingredient)
        count = main_page.get_actual_counter(ingredient)

        assert count == expected_count

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    def test_create_order_by_authorized_user(self, driver, authorize_user):
        main_page = MainPage(driver)

        driver.get(urls.LOGIN_PAGE)
        main_page.wait_for_load_main_page()
        ingredient = main_page.choose_ingredient()
        main_page.add_ingredient(ingredient)
        main_page.click_order_button()
        element = main_page.find_order_modal()

        assert element
