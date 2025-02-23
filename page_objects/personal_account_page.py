from page_objects.base_page import BasePage
from helpers.urls import Urls
from helpers.locators import Locators

class PersonalAccountPage(BasePage):

    def navigate_to_personal_account(self):
        self.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_until_url_matches(Urls.PERSONAL_ACCOUNT_URL)
        return self.find_element(Locators.SIGN_IN_TITLE)

    def click_on_personal_account_button(self):
        self.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)

    def click_on_order_history_button(self):
        self.click_element(Locators.ORDER_HISTORY_BUTTON)

    def order_history_page_is_open(self):
        return self.driver.current_url == Urls.ORDERS_HISTORY_URL

    def click_on_sign_out_button(self):
        self.click_element(Locators.SIGN_OUT_BUTTON)
        return self.find_element(Locators.SIGN_IN_TITLE)

    def personal_account_page_is_open(self):
        return self.driver.current_url == Urls.PERSONAL_ACCOUNT_URL