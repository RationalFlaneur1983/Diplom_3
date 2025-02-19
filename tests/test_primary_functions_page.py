from helpers.locators import Locators
from page_objects.primary_functions_page import PrimaryFunctionsPage
from helpers.urls import Urls
import allure


@allure.feature("Основные функции приложения")
class TestPrimaryFunctionsPage:

    @allure.title("Переход по клику на «Конструктор»")
    def test_navigate_to_constructor_section(self, driver):
        primary_functions_page = PrimaryFunctionsPage(driver)
        primary_functions_page.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        primary_functions_page.find_element(Locators.SIGN_IN_TITLE)
        primary_functions_page.click_element(Locators.CONSTRUCTOR_BUTTON)
        result = primary_functions_page.find_element(Locators.CONSTRUCTOR_TITLE)
        assert result

    @allure.title("Переход по клику на «Лента заказов»")
    def test_navigate_to_order_feed_section(self, driver):
        primary_functions_page = PrimaryFunctionsPage(driver)
        primary_functions_page.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        primary_functions_page.find_element(Locators.SIGN_IN_TITLE)
        primary_functions_page.click_element(Locators.ORDERS_LIST_BUTTON)
        result = primary_functions_page.find_element(Locators.ORDER_LIST_TITLE)
        assert result

    @allure.title("При клике на ингредиент появляется всплывающее окно с деталями")
    def test_ingredient_details_popup_appears(self, driver):
        primary_functions_page = PrimaryFunctionsPage(driver)
        primary_functions_page.click_element(Locators.BURGER_ITEM)
        result = primary_functions_page.find_element(Locators.INGREDIENT_DETAILS_TITLE)
        assert result

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_ingredient_details_popup(self, driver):
        primary_functions_page = PrimaryFunctionsPage(driver)
        primary_functions_page.click_element(Locators.BURGER_ITEM)
        primary_functions_page.wait_until_element_visible(Locators.INGREDIENT_POPUP)
        primary_functions_page.click_element(Locators.CLOSE_CROSS_BUTTON)
        primary_functions_page.wait_until_element_invisible(Locators.INGREDIENT_POPUP)
        popup = primary_functions_page.driver.find_element(*Locators.INGREDIENT_POPUP)
        assert not popup.is_displayed()


    @allure.title("При добавлении ингредиента в заказ увеличивается счетчик")
    def test_ingredient_counter_increases(self, driver):
        primary_functions_page = PrimaryFunctionsPage(driver)
        primary_functions_page.drag_and_drop(Locators.SPICY_SAUCE_ITEM, Locators.BASKET)
        counter = primary_functions_page.get_element_text(Locators.SPICY_SAUCE_COUNTER)
        assert counter == "1"

    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_authorized_user_can_place_order(self, driver, registered_user):
        email = registered_user['email']
        password = registered_user['password']
        main_functions_page = PrimaryFunctionsPage(driver)
        main_functions_page.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        main_functions_page.wait_until_url_matches(Urls.PERSONAL_ACCOUNT_URL)
        main_functions_page.fill_login_form(
            Locators.EMAIL_INPUT, email,
            Locators.PASSWORD_INPUT, password,
            Locators.SIGN_IN_BUTTON
            )

        main_functions_page.drag_and_drop(Locators.BUN_ITEM, Locators.BASKET)
        main_functions_page.drag_and_drop(Locators.SPICY_SAUCE_ITEM, Locators.BASKET)
        main_functions_page.click_element(Locators.PLACE_ORDER_BUTTON)
        result = main_functions_page.find_element(Locators.ORDER_SUBTITLE)
        assert result