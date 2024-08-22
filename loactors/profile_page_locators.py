from selenium.webdriver.common.by import By


class ProfilePageLocators:

    NAME_FIELD = By.XPATH, './/label[text()="Имя"]/parent::div/input'  # поле с именем пользователя
    ORDER_HISTORY = By.LINK_TEXT, "История заказов" # ссылка на историю заказов пользователя
    EXIT_BUTTON = By.XPATH, ".//button[text()='Выход']"  # кнопка "Выход"

    ORDER_NUMBER = By.XPATH, ".//a/div/p[contains(@class,'text_type_digits-default')]" # номер заказа




