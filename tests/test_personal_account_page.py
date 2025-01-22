import allure
import data as dt

class TestPersonalAccountPage:

    @allure.title("Тест входа в личный кабинет")
    def test_transition_on_click_personal_account_btn(self, personal_acc_page, login_page):
        personal_acc_page.open_page(dt.BASE_URL)
        login_page.authorization(dt.email, dt.password)
        personal_acc_page.click_personal_acc_btn()
        personal_acc_page.check_redirect_personal_acc()

    @allure.title("Тест получения истории заказов")
    def test_open_orders_history(self, personal_acc_page, login_page):
        personal_acc_page.open_page(dt.BASE_URL)
        login_page.authorization(dt.email, dt.password)
        personal_acc_page.click_personal_acc_btn()
        personal_acc_page.click_order_history_btn()
        personal_acc_page.check_found_lst_is_not_empty()

    @allure.title("Тест выхода из личного кабинета")
    def test_logout(self, personal_acc_page, login_page):
        personal_acc_page.open_page(dt.BASE_URL)
        login_page.authorization(dt.email, dt.password)
        personal_acc_page.click_personal_acc_btn()
        personal_acc_page.click_logout_btn()
        personal_acc_page.check_logout_successfully()