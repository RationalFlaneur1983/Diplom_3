from page_objects.base_page import BasePage
from helpers.locators import Locators


class OrdersListPage(BasePage):

    def navigate_to_orders_list(self):
        self.click_element(Locators.ORDERS_LIST_BUTTON)

    def click_on_order_item(self):
        self.click_element(Locators.ORDER_ITEM)

    def wait_for_order_popup(self):
        return self.wait_until_element_visible(Locators.ORDERS_POPUP)

    def assemble_burger_and_place_order(self):
        self.drag_and_drop(Locators.BUN_ITEM, Locators.BASKET)
        self.drag_and_drop(Locators.SPICY_SAUCE_ITEM, Locators.BASKET)
        self.click_element(Locators.PLACE_ORDER_BUTTON)
        self.wait_until_element_invisible(Locators.ORDERS_POPUP_OVERLAY)

    def get_order_number_from_popup(self):
        order_number = self.get_element_text(Locators.ORDER_NUMBER)
        return f'#0{order_number}'

    def get_order_number_from_in_progress_section(self):
        self.click_element(Locators.ORDERS_LIST_BUTTON)
        order_number = self.get_element_text(Locators.ORDER_IN_PROGRESS)
        return f'#0{order_number}'

    def close_order_popup(self):
        self.click_element(Locators.CLOSE_CROSS_BUTTON)

    def get_order_number_from_list(self):
        return self.get_element_text(Locators.ORDER_NUMBER_IN_LIST)

    def get_all_time_counter_data(self):
        self.click_element(Locators.ORDERS_LIST_BUTTON)
        counter = int(self.get_element_text(Locators.ALL_ORDERS_COUNT))
        return counter

    def get_today_counter_data(self):
        self.click_element(Locators.ORDERS_LIST_BUTTON)
        counter = int(self.get_element_text(Locators.TODAY_ORDERS_COUNT))
        return counter