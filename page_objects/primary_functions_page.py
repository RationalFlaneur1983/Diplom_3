from page_objects.base_page import BasePage
from helpers.locators import Locators
import allure


class PrimaryFunctionsPage(BasePage):

    @allure.step("Проверить, что попап с деталями ингредиента отображается")
    def is_ingredient_popup_visible(self):
        return self.find_element(Locators.INGREDIENT_POPUP)

    def click_on_personal_account_button(self):
        self.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)

    def click_on_constructor_button(self):
        self.click_element(Locators.CONSTRUCTOR_BUTTON)

    def is_constructor_panel_visible(self):
        return self.find_element(Locators.CONSTRUCTOR_TITLE)

    def click_on_order_list_button(self):
        self.click_element(Locators.ORDERS_LIST_BUTTON)

    def is_order_list_visible(self):
        return self.find_element(Locators.ORDER_LIST_TITLE)

    def click_on_burger_item(self):
        self.click_element(Locators.BURGER_ITEM)
        self.wait_until_element_visible(Locators.INGREDIENT_POPUP)

    def close_ingredient_popup(self):
        self.click_element(Locators.CLOSE_CROSS_BUTTON)
        self.wait_until_element_invisible(Locators.INGREDIENT_POPUP)

    def is_ingredient_popup_visible(self):
        return self.driver.find_element(*Locators.INGREDIENT_POPUP).is_displayed()

    def put_sauce_in_basket(self):
        self.drag_and_drop(Locators.SPICY_SAUCE_ITEM, Locators.BASKET)

    def get_sauce_counter_data(self):
        return self.get_element_text(Locators.SPICY_SAUCE_COUNTER)

    def assemble_burger_and_place_order(self):
        self.drag_and_drop(Locators.BUN_ITEM, Locators.BASKET)
        self.drag_and_drop(Locators.SPICY_SAUCE_ITEM, Locators.BASKET)
        self.click_element(Locators.PLACE_ORDER_BUTTON)

    def wait_for_order_overlay_to_disappear(self):
        self.wait_until_element_invisible(Locators.ORDERS_POPUP_OVERLAY)

    def is_order_subtitle_test_visible(self):
        return self.find_element(Locators.ORDER_SUBTITLE)