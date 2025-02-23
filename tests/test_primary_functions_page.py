from page_objects.primary_functions_page import PrimaryFunctionsPage
import allure


@allure.feature("Основные функции приложения")
class TestPrimaryFunctionsPage:

    @allure.title("Переход по клику на «Конструктор»")
    def test_navigate_to_constructor_section(self, driver):
        primary_functions_page = PrimaryFunctionsPage(driver)
        primary_functions_page.click_on_personal_account_button()
        primary_functions_page.click_on_constructor_button()
        assert primary_functions_page.is_constructor_panel_visible

    @allure.title("Переход по клику на «Лента заказов»")
    def test_navigate_to_order_feed_section(self, driver):
        primary_functions_page = PrimaryFunctionsPage(driver)
        primary_functions_page.click_on_personal_account_button()
        primary_functions_page.click_on_order_list_button()
        assert primary_functions_page.is_order_list_visible()

    @allure.title("При клике на ингредиент появляется всплывающее окно с деталями")
    def test_ingredient_details_popup_appears(self, driver):
        primary_functions_page = PrimaryFunctionsPage(driver)
        primary_functions_page.click_on_burger_item()
        assert primary_functions_page.is_ingredient_popup_visible()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_ingredient_details_popup(self, driver):
        primary_functions_page = PrimaryFunctionsPage(driver)
        primary_functions_page.click_on_burger_item()
        primary_functions_page.close_ingredient_popup()
        assert not primary_functions_page.is_ingredient_popup_visible()


    @allure.title("При добавлении ингредиента в заказ увеличивается счетчик")
    def test_ingredient_counter_increases(self, driver):
        primary_functions_page = PrimaryFunctionsPage(driver)
        primary_functions_page.put_sauce_in_basket()
        counter = primary_functions_page.get_sauce_counter_data()
        assert counter == "1"

    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_authorized_user_can_place_order(self, driver, registered_user):
        email = registered_user['email']
        password = registered_user['password']
        main_functions_page = PrimaryFunctionsPage(driver)
        main_functions_page.authorize(email,password)
        main_functions_page.assemble_burger_and_place_order()
        assert main_functions_page.is_order_subtitle_test_visible()