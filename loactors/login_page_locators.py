from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL_AUTH_FIELD = By.XPATH, ".//*[text()='Email']/following-sibling::input"  # поле ввода email
    PWD_AUTH_FIELD = By.XPATH, ".//input[@type = 'password']"  # поле ввода пароля
    LOGIN_BUTTON = By.XPATH, ".//button[text()='Войти']"  # кнопка "Войти"
    RESTORE_PASS_LINK = By.LINK_TEXT, "Восстановить пароль" # ссылка Восстановить пароль
    CONSTRUCTOR_BUTTON = By.LINK_TEXT, "Конструктор" # кнопка "Конструктор"
