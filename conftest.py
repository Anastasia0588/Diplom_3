import allure
import pytest
import requests
from selenium import webdriver

from helper import generate_user_creds
from urls import register_url, user_url


@pytest.fixture(scope='function', params=['firefox', 'chrome'])
@allure.title('Запуск драйвера')
def driver(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1024,768')
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
@allure.title('Создание юзера')
def user():
    user_data = generate_user_creds()
    response = requests.post(register_url, data=user_data)
    if response.status_code == 200:
        user_data['access_token'] = response.json()['accessToken']
    yield user_data
    requests.delete(user_url, headers={"Authorization": user_data['access_token']})




