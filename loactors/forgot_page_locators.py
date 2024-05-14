from selenium.webdriver.common.by import By


class ForgotPageLocators:
    EMAIL_FIELD = By.XPATH, ".//*[text()='Email']/following-sibling::input"  # поле ввода email
    RESTORE_BUTTON = By.XPATH, ".//button[text()='Восстановить']"  # кнопка "Восстановить"