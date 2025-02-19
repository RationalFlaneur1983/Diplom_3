from helpers.locators import Locators
from page_objects.personal_account_page import PersonalAccountPage
from helpers.urls import Urls
import allure


class TestPersonalAccountPage:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_navigate_to_personal_account(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_page.wait_until_url_matches(Urls.PERSONAL_ACCOUNT_URL)
        result = personal_account_page.find_element(Locators.SIGN_IN_TITLE)
        assert driver.current_url == Urls.PERSONAL_ACCOUNT_URL
        assert result

    @allure.title("Переход в раздел «История заказов»")
    def test_navigate_to_order_history(self, driver, registered_user):
        email = registered_user['email']
        password = registered_user['password']

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_page.wait_until_url_matches(Urls.PERSONAL_ACCOUNT_URL)
        personal_account_page.fill_login_form(
            Locators.EMAIL_INPUT, email,
            Locators.PASSWORD_INPUT, password,
            Locators.SIGN_IN_BUTTON)

        personal_account_page.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_page.click_element(Locators.ORDER_HISTORY_BUTTON)
        assert driver.current_url == Urls.ORDERS_HISTORY_URL

    @allure.title("Выход из аккаунта")
    def test_logout_from_personal_account(self, driver, registered_user):
        email = registered_user['email']
        password = registered_user['password']

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_element(Locators.ORDERS_LIST_BUTTON)
        personal_account_page.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_page.wait_until_url_matches(Urls.PERSONAL_ACCOUNT_URL)

        personal_account_page.fill_login_form(
            Locators.EMAIL_INPUT, email,
            Locators.PASSWORD_INPUT, password,
            Locators.SIGN_IN_BUTTON)

        personal_account_page.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_page.click_element(Locators.SIGN_OUT_BUTTON)
        result = personal_account_page.find_element(Locators.SIGN_IN_TITLE)
        assert driver.current_url == Urls.PERSONAL_ACCOUNT_URL
        assert result



