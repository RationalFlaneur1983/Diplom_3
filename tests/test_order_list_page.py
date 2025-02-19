from helpers.locators import Locators
from page_objects.orders_list_page import OrdersListPage
from helpers.urls import Urls
import allure

class TestOrdersListPage:

    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_popup_with_order_details(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.click_element(Locators.ORDERS_LIST_BUTTON)
        orders_list_page.click_element(Locators.ORDER_ITEM)
        popup = orders_list_page.wait_until_element_visible(Locators.ORDERS_POPUP)
        assert popup.is_displayed()

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_orders_displayed_in_orders_list(self, driver, registered_user):
        email = registered_user['email']
        password = registered_user['password']

        orders_list_page = OrdersListPage(driver)
        orders_list_page.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        orders_list_page.wait_until_url_matches(Urls.PERSONAL_ACCOUNT_URL)

        orders_list_page.fill_login_form(
            Locators.EMAIL_INPUT, email,
            Locators.PASSWORD_INPUT, password,
            Locators.SIGN_IN_BUTTON
        )

        orders_list_page.drag_and_drop(Locators.BUN_ITEM, Locators.BASKET)
        orders_list_page.drag_and_drop(Locators.SPICY_SAUCE_ITEM, Locators.BASKET)
        orders_list_page.click_element(Locators.PLACE_ORDER_BUTTON)
        orders_list_page.wait_until_element_invisible(Locators.ORDERS_POPUP_OVERLAY)
        user_order_number = '#0' + orders_list_page.get_element_text(Locators.ORDER_NUMBER)
        orders_list_page.click_element(Locators.CLOSE_CROSS_BUTTON)
        orders_list_page.click_element(Locators.ORDERS_LIST_BUTTON)
        order_number = orders_list_page.get_element_text(Locators.ORDER_NUMBER_IN_LIST)
        assert user_order_number == order_number

    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_all_orders_count_increases(self, driver, registered_user):
        email = registered_user['email']
        password = registered_user['password']

        orders_list_page = OrdersListPage(driver)
        orders_list_page.click_element(Locators.ORDERS_LIST_BUTTON)
        orders_list_page.find_element(Locators.ORDER_LIST_TITLE)
        before_order = int(orders_list_page.get_element_text(Locators.ALL_ORDERS_COUNT))
        orders_list_page.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        orders_list_page.wait_until_url_matches(Urls.PERSONAL_ACCOUNT_URL)

        orders_list_page.fill_login_form(
            Locators.EMAIL_INPUT, email,
            Locators.PASSWORD_INPUT, password,
            Locators.SIGN_IN_BUTTON
        )

        orders_list_page.drag_and_drop(Locators.BUN_ITEM, Locators.BASKET)
        orders_list_page.drag_and_drop(Locators.SPICY_SAUCE_ITEM, Locators.BASKET)
        orders_list_page.click_element(Locators.PLACE_ORDER_BUTTON)
        orders_list_page.wait_until_element_invisible(Locators.ORDERS_POPUP_OVERLAY)
        orders_list_page.click_element(Locators.CLOSE_CROSS_BUTTON)
        orders_list_page = OrdersListPage(driver)
        orders_list_page.click_element(Locators.ORDERS_LIST_BUTTON)
        orders_list_page.find_element(Locators.ORDER_LIST_TITLE)
        after_order = int(orders_list_page.get_element_text(Locators.ALL_ORDERS_COUNT))
        assert before_order < after_order

    @allure.title("при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_today_orders_count_increases(self, driver, registered_user):
        email = registered_user['email']
        password = registered_user['password']

        orders_list_page = OrdersListPage(driver)
        orders_list_page.click_element(Locators.ORDERS_LIST_BUTTON)
        before_order = int(orders_list_page.get_element_text(Locators.TODAY_ORDERS_COUNT))
        orders_list_page.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        orders_list_page.wait_until_url_matches(Urls.PERSONAL_ACCOUNT_URL)

        orders_list_page.fill_login_form(
            Locators.EMAIL_INPUT, email,
            Locators.PASSWORD_INPUT, password,
            Locators.SIGN_IN_BUTTON
        )

        orders_list_page.drag_and_drop(Locators.BUN_ITEM, Locators.BASKET)
        orders_list_page.drag_and_drop(Locators.SPICY_SAUCE_ITEM, Locators.BASKET)
        orders_list_page.click_element(Locators.PLACE_ORDER_BUTTON)
        orders_list_page.wait_until_element_invisible(Locators.ORDERS_POPUP_OVERLAY)
        orders_list_page.click_element(Locators.CLOSE_CROSS_BUTTON)
        orders_list_page = OrdersListPage(driver)
        orders_list_page.click_element(Locators.ORDERS_LIST_BUTTON)
        orders_list_page.find_element(Locators.ORDER_LIST_TITLE)
        after_order = int(orders_list_page.get_element_text(Locators.TODAY_ORDERS_COUNT))
        assert before_order < after_order


    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_order_number_appears_in_progress_section(self, driver, registered_user):
        email = registered_user['email']
        password = registered_user['password']

        orders_list_page = OrdersListPage(driver)
        orders_list_page.click_element(Locators.ORDERS_LIST_BUTTON)
        orders_list_page.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        orders_list_page.wait_until_url_matches(Urls.PERSONAL_ACCOUNT_URL)

        orders_list_page.fill_login_form(
            Locators.EMAIL_INPUT, email,
            Locators.PASSWORD_INPUT, password,
            Locators.SIGN_IN_BUTTON)

        orders_list_page.drag_and_drop(Locators.BUN_ITEM, Locators.BASKET)
        orders_list_page.drag_and_drop(Locators.SPICY_SAUCE_ITEM, Locators.BASKET)
        orders_list_page.click_element(Locators.PLACE_ORDER_BUTTON)
        orders_list_page.wait_until_element_invisible(Locators.ORDERS_POPUP_OVERLAY)
        user_order_number = '#0' + orders_list_page.get_element_text(Locators.ORDER_NUMBER)
        orders_list_page.click_element(Locators.CLOSE_CROSS_BUTTON)
        orders_list_page.click_element(Locators.ORDERS_LIST_BUTTON)
        order_number = '#' + orders_list_page.get_element_text(Locators.ORDER_IN_PROGRESS)
        assert user_order_number == order_number




