import allure
import data as dt

class TestRecoverPasswordPage:

    @allure.title("Тест перехода при нажатии на кнопку 'Восстановить пароль'")
    def test_transition_page_at_click_btn(self, recover_password_page):
        recover_password_page.open_page(dt.LOGIN_URL)
        recover_password_page.click_recover_password_btn()
        recover_password_page.check_redirect_forgot_password_page()

    @allure.title("Тест перехода при нажатии на кнопку ВОССТАНОВИТЬ при заполненном поле электронная почта")
    def test_fill_email_and_click_btn(self, recover_password_page):
        recover_password_page.open_page(dt.FORGOT_PASS_URL)
        recover_password_page.fill_email()
        recover_password_page.check_redirect_reset_password_page()

    @allure.title("Тест работы кнопки показать пароль")
    def test_show_password_btn(self, recover_password_page):
        recover_password_page.open_page(dt.FORGOT_PASS_URL)
        recover_password_page.fill_email()
        recover_password_page.fill_password()
        recover_password_page.check_password_is_displayed()