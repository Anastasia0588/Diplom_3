from selenium.webdriver.common.by import By


class MainPageLocators:

    # кнопка перехода в Личный кабинет
    PROFILE_LINK = By.LINK_TEXT, "Личный Кабинет"
    # кнопка "Войти в аккаунт"
    LOGIN_BUTTON_FROM_MAIN_PAGE = By.XPATH, ".//button[text()='Войти в аккаунт']"
    # кнопка перехода в "Ленту заказов"
    FEED_BUTTON = By.XPATH, ".//p[text()='Лента Заказов']"
    # первый ингредиент в списке
    FIRST_INGREDIENT = By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient_')][1]"
    # лист ингредиентов
    INGREDIENTS_LIST = By.XPATH, ".//p[contains(text(), 'булка')]//parent::a[contains(@href, '/ingredient/')]"
    # заголовок окна деталей ингредиента
    INGREDIENT_MODAL_HEADER = By.XPATH, ".// h2[text() = 'Детали ингредиента']"
    # кнопка "Закрыть" окно деталей заказа
    CLOSE_MODAL_BUTTON = By.XPATH, './/button[contains(@class,"Modal_modal__close_modified")]'
    # BASKET_LIST = By.XPATH, ".//ul[contains(@class,'BurgerConstructor_basket')]"
    # блоки элемента булка в корзине
    BASKET = By.CLASS_NAME, 'constructor-element_pos_top'
    # кнопка "Оформить заказ"
    ORDER_BUTTON = By.XPATH, ".//button[text()='Оформить заказ']"
    # текст в модальном коне деталей заказа
    ORDER_MODAL_HEADER = By.XPATH, ".//p[text()='идентификатор заказа']"
    # номер заказа в модельном окне деталей заказа
    ORDER_NUMBER = By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]"
    # кнопка закрыть модальное окно
    CLOSE_ORDER_BUTTON = By.XPATH, ".//button[contains(@class,'Modal_modal__close_modified')]"





