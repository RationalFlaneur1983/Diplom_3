from helpers.locators import Locators
from page_objects.password_recovery_page import PasswordRecovery
from helpers.urls import Urls
import allure


class TestRecoverPasswordPage:
    @allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_navigate_to_recover_password_page(self, driver):
        recover_password_page = PasswordRecovery(driver)
        recover_password_page.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        recover_password_page.wait_until_url_matches(Urls.PERSONAL_ACCOUNT_URL)
        recover_password_page.click_element(Locators.FORGOT_PASSWORD_LINK)
        recover_password_page.wait_until_url_matches(Urls.RECOVER_PASSWORD_URL)
        result = recover_password_page.find_element(Locators.FORGOT_PASSWORD_TITLE)
        assert result

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_input_email_and_click_recover_button(self, driver):
        recover_password_page = PasswordRecovery(driver)
        recover_password_page.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        recover_password_page.wait_until_url_matches(Urls.PERSONAL_ACCOUNT_URL)
        recover_password_page.click_element(Locators.FORGOT_PASSWORD_LINK)
        recover_password_page.wait_until_url_matches(Urls.RECOVER_PASSWORD_URL)
        recover_password_page.find_element(Locators.FORGOT_PASSWORD_TITLE)
        recover_password_page.fill_email_form()
        result = recover_password_page.find_element(Locators.SAVE_PASSWORD_BUTTON)
        assert result

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.")
    def test_show_and_hide_password(self, driver):
        recover_password_page = PasswordRecovery(driver)
        recover_password_page.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        recover_password_page.wait_until_url_matches(Urls.PERSONAL_ACCOUNT_URL)
        recover_password_page.click_element(Locators.FORGOT_PASSWORD_LINK)
        recover_password_page.wait_until_url_matches(Urls.RECOVER_PASSWORD_URL)
        recover_password_page.find_element(Locators.FORGOT_PASSWORD_TITLE)
        recover_password_page.fill_email_form()
        recover_password_page.find_element(Locators.SAVE_PASSWORD_BUTTON)
        assert recover_password_page.is_password_invisible()

        recover_password_page.fill_password_form()
        recover_password_page.click_element(Locators.SHOW_PASSWORD_BUTTON)
        assert recover_password_page.is_password_visible()








