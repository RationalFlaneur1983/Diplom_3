from page_objects.base_page import BasePage
from helpers.locators import Locators
from helpers.urls import Urls
from helpers.user_helpers import UserRegistration


class PasswordRecovery(BasePage):

    def navigate_to_password_recovery_page(self):
        self.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_until_url_matches(Urls.PERSONAL_ACCOUNT_URL)
        self.click_element(Locators.FORGOT_PASSWORD_LINK)
        self.wait_until_url_matches(Urls.RECOVER_PASSWORD_URL)
        result = self.find_element(Locators.FORGOT_PASSWORD_TITLE)
        return result

    def click_show_password_button(self):
        self.click_element(Locators.SHOW_PASSWORD_BUTTON)

    def fill_email_form(self):
        user_data = UserRegistration.generate_user_data(None)
        email = user_data['email']
        self.enter_text(Locators.EMAIL_INPUT, email)
        self.click_element(Locators.RESET_PASSWORD_BUTTON)

    def fill_password_form(self):
        user_data = UserRegistration.generate_user_data(None)
        password = user_data['password']
        self.enter_text(Locators.NEW_PASSWORD_INPUT, password)

    def is_password_visible(self):
        password_label = self.find_element(Locators.NEW_PASSWORD_INPUT)
        return "text" in password_label.get_attribute('type')

    def is_password_invisible(self):
        password_label = self.find_element(Locators.NEW_PASSWORD_INPUT)
        return "password" in password_label.get_attribute('type')

    def is_save_password_button_visible(self):
        return self.find_element(Locators.SAVE_PASSWORD_BUTTON)







