from page_objects.personal_account_page import PersonalAccountPage
import allure


class TestPersonalAccountPage:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_navigate_to_personal_account(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        result = personal_account_page.navigate_to_personal_account()
        assert result

    @allure.title("Переход в раздел «История заказов»")
    def test_navigate_to_order_history(self, driver, registered_user):
        email = registered_user['email']
        password = registered_user['password']
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.authorize(email, password)
        personal_account_page.click_on_personal_account_button()
        personal_account_page.click_on_order_history_button()
        assert personal_account_page.order_history_page_is_open()

    @allure.title("Выход из аккаунта")
    def test_logout_from_personal_account(self, driver, registered_user):
        email = registered_user['email']
        password = registered_user['password']
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.authorize(email, password)
        personal_account_page.click_on_personal_account_button()
        personal_account_page.click_on_sign_out_button()
        assert personal_account_page.personal_account_page_is_open()




