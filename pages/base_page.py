import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    def click_on_element(self, locator):
        WebDriverWait(self.driver, 50).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def set_text_to_form(self, locator, text):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получаем url текущей страницы')
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step('Ожидаем изменения адреса страницы')
    def wait_for_url(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    def check_visibility_of_element(self, locator):
        try:
            self.driver.find_element_with_wait(locator)
            return True
        finally:
            return False

    def wait_disappear_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Перетаскиваем элемент на элемент')
    def drag_n_drop(self, source, target):
        action_chains = ActionChains(self.driver)
        drag = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(source))
        drop = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(target))
        action_chains.drag_and_drop(drag, drop).perform()





