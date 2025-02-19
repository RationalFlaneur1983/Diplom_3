from selenium.webdriver.common.by import By

class Locators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')
    EMAIL_INPUT = (By.XPATH, '//label[contains(text(),"Email")]/following-sibling::input[@name="name"]')
    PASSWORD_INPUT = (By.XPATH, '//label[contains(text(),"Пароль")]/following-sibling::input[@name="Пароль"]')
    SIGN_IN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    SIGN_IN_TO_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')
    SIGN_IN_TITLE = (By.XPATH, '//h2[text()="Вход"]')
    CONSTRUCTOR_TITLE = (By.XPATH, '//h1[text()="Соберите бургер"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//a[@href="/"]')
    ORDERS_LIST_BUTTON = (By.XPATH, '//a[@href="/feed"]')
    SIGN_OUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')

    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//a[@href="/forgot-password"]')
    FORGOT_PASSWORD_TITLE = (By.XPATH, '//h2[text()="Восстановление пароля"]')
    RESET_PASSWORD_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    SAVE_PASSWORD_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')

    NEW_PASSWORD_INPUT= (By.XPATH, '//input[@name="Введите новый пароль"]')
    SHOW_PASSWORD_BUTTON = (By.XPATH, '//div[@class="input__icon input__icon-action"]')

    BURGER_ITEM = (By.XPATH, '//p[contains(text(),"Флюоресцентная булка")]')

    INGREDIENT_DETAILS_TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]')


    INGREDIENT_POPUP = (By.XPATH, "//div[@class='Modal_modal__container__Wo2l_']")
    ORDER_ITEM = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem__2x95r")]')
    ORDERS_POPUP = (By.XPATH, "//p[@class='text text_type_digits-default mb-10 mt-5']")
    ORDERS_POPUP_OVERLAY = (By.XPATH, "//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']")

    CLOSE_CROSS_BUTTON = (By.XPATH, "//button[@type='button']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]")


    SPICY_SAUCE_COUNTER = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']//div[contains(@class, 'counter_counter__ZNLkj')]")
    SPICY_SAUCE_ITEM = (By.XPATH, '//p[contains(text(), "Соус Spicy-X")]')
    BASKET = (By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]')
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    ORDER_SUBTITLE = (By.XPATH, '//p[text()="идентификатор заказа"]')
    ORDER_LIST_TITLE = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")
    BUN_ITEM = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")

    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    ORDER_NUMBER_IN_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list__OLh59')]/li[1]//p[contains(@class, 'text_type_digits-default')]")

    ALL_ORDERS_COUNT = (By.XPATH, "//div[contains(@class,'undefined')]//p[contains(@class, 'text_type_digits-large')]")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]")