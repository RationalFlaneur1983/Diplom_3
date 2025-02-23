from page_objects.orders_list_page import OrdersListPage
import allure

class TestOrdersListPage:

    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_popup_with_order_details(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.navigate_to_orders_list()
        orders_list_page.click_on_order_item()
        popup = orders_list_page.wait_for_order_popup()
        assert popup.is_displayed()

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_orders_displayed_in_orders_list(self, driver, registered_user):
        email = registered_user['email']
        password = registered_user['password']
        orders_list_page = OrdersListPage(driver)
        orders_list_page.authorize(email, password)
        orders_list_page.assemble_burger_and_place_order()
        user_order_number = orders_list_page.get_order_number_from_popup()
        orders_list_page.close_order_popup()
        orders_list_page.navigate_to_orders_list()
        order_number = orders_list_page.get_order_number_from_list()
        assert user_order_number == order_number

    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_all_orders_count_increases(self, driver, registered_user):
        email = registered_user['email']
        password = registered_user['password']
        orders_list_page = OrdersListPage(driver)
        before_order = orders_list_page.get_all_time_counter_data()
        orders_list_page.authorize(email, password)
        orders_list_page.assemble_burger_and_place_order()
        orders_list_page.close_order_popup()
        after_order = orders_list_page.get_all_time_counter_data()
        assert before_order < after_order

    @allure.title("при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_today_orders_count_increases(self, driver, registered_user):
        email = registered_user['email']
        password = registered_user['password']
        orders_list_page = OrdersListPage(driver)
        before_order = orders_list_page.get_today_counter_data()
        orders_list_page.authorize(email, password)
        orders_list_page.assemble_burger_and_place_order()
        orders_list_page.close_order_popup()
        after_order = orders_list_page.get_today_counter_data()
        assert before_order < after_order


    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_order_number_appears_in_progress_section(self, driver, registered_user):
        email = registered_user['email']
        password = registered_user['password']
        orders_list_page = OrdersListPage(driver)
        orders_list_page.authorize(email, password)
        orders_list_page.assemble_burger_and_place_order()
        user_order_number = orders_list_page.get_order_number_from_popup()
        orders_list_page.close_order_popup()
        orders_list_page.navigate_to_orders_list()

        order_number = orders_list_page.get_order_number_from_in_progress_section()

        assert user_order_number == order_number




