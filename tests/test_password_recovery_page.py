from page_objects.password_recovery_page import PasswordRecovery
import allure


class TestRecoverPasswordPage():

    @allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_navigate_to_recover_password_page(self, driver):
        recover_password_page = PasswordRecovery(driver)
        assert recover_password_page.navigate_to_password_recovery_page()

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_input_email_and_click_recover_button(self, driver):
        recover_password_page = PasswordRecovery(driver)
        recover_password_page.navigate_to_password_recovery_page()
        recover_password_page.fill_email_form()
        result = recover_password_page.is_save_password_button_visible()
        assert result

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.")
    def test_show_and_hide_password(self, driver):
        recover_password_page = PasswordRecovery(driver)
        recover_password_page.navigate_to_password_recovery_page()
        recover_password_page.fill_email_form()
        recover_password_page.is_save_password_button_visible()
        assert recover_password_page.is_password_invisible()
        recover_password_page.fill_password_form()
        recover_password_page.click_show_password_button()
        assert recover_password_page.is_password_visible()








