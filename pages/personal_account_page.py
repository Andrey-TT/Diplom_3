import allure
import data
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators

class PersonalAccountPage(BasePage):

    @allure.step("Нажатие на логотип Стеллар бургерс")
    def click_logo(self):
        self.click_by_script(PersonalAccountLocators.STELLAR_LOGO)

    @allure.step("Нажатие на кнопку Личный кабинет")
    def click_personal_acc_btn(self):
        self.click_by_script(PersonalAccountLocators.PERSONAL_ACCOUNT)

    @allure.step("Нажатие на кнопку История заказов")
    def click_order_history_btn(self):
        self.click_by_script(PersonalAccountLocators.ORDER_HISTORY)

    @allure.step("Получение списка заказов")
    def get_order_list(self):
        lst = self.find_elements(PersonalAccountLocators.ORDERS_LST)
        return len(lst)

    @allure.step("Скрол до последнего заказа")
    def scroll_to_last_order(self):
        scrollable_lst = self.find_element(PersonalAccountLocators.ORDER_LIST)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scrollable_lst)

    @allure.step("Проверка наполнености списка заказов")
    def check_found_lst_is_not_empty(self):
        assert self.get_order_list() != 0

    @allure.step("Нажатие на кнопку Выход")
    def click_logout_btn(self):
        self.click_by_script(PersonalAccountLocators.LOGOUT_BTN)

    @allure.step("Проверка выхода из личного кабинета")
    def check_logout_successfully(self):
        self.check_url(data.LOGIN_URL)
        assert self.find_element(PersonalAccountLocators.LOGIN_ACC).is_displayed() == True