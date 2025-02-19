from page_objects.base_page import BasePage
from helpers.locators import Locators
from helpers.user_helpers import UserRegistration


class PasswordRecovery(BasePage):

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







