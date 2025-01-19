from locators.tape_orders_locators import TapeOrdersLocators
from locators.constructor_locators import ConstructorLocators
from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage
import allure

class TapeOrdersPage(BasePage):

    id = ''
    initial_count_all_times = ''
    initial_count_today = ''

    @allure.step("Открытие первого заказа в Ленте заказов")
    def open_first_order(self):
        self.find_element(TapeOrdersLocators.FIRST_ORDER).click()

    @allure.step("Получение ID нового заказа")
    def get_order_id(self):
        self.wait_change_value_in_element_page(ConstructorLocators.ORDER_ID, '9999')
        self.id = self.get_text(ConstructorLocators.ORDER_ID)
        return self.id

    @allure.step("Получение списка заказов в работе")
    def get_order_in_work(self):
        self.wait_change_value_in_element_page(TapeOrdersLocators.ORDER_IN_WORKS, 'Все текущие заказы готовы!', 30)
        order_id = self.get_text(TapeOrdersLocators.ORDER_IN_WORKS)
        return order_id

    @allure.step("Получения количества заказов за сегодня")
    def get_current_count_today(self):
        self.initial_count_today = self.get_text(TapeOrdersLocators.COUNT_TODAY)
        return self.initial_count_today

    @allure.step("Получения количества заказов за все время")
    def get_current_count_all_time(self):
        self.initial_count_all_times = self.get_text(TapeOrdersLocators.COUNT_ALL_TIMES)
        return self.initial_count_all_times

    @allure.step("Проверка появления созданного заказа в ленте заказов")
    def check_created_order_has_in_tape(self):
        first_order_id = self.get_text(TapeOrdersLocators.ORDER_ID)
        print(first_order_id)
        print(self.id)
        assert f'#0{self.id}' == first_order_id, f'#{self.id} != {first_order_id}'

    @allure.step("Проверка появления созданного заказа в истории заказов в личном кабинете")
    def check_created_order_has_in_order_history(self):
        last_order_id = ''
        list_elem = self.find_elements(PersonalAccountLocators.ORDERS_ID_IN_HISTORY)
        if list_elem:
            last_order_id = list_elem[-1].text
            return last_order_id
        else:
           print("Список <li> пуст или не найден.")

        print(last_order_id)
        print(self.id)
        assert f'#0{self.id}' == last_order_id, f'#0{self.id} != {last_order_id}'

    @allure.step("Проверка появления созданного заказа В работе")
    def check_created_order_has_in_work(self):
        assert f'0{self.id}' == self.get_order_in_work(), f'0{self.id} != {self.get_order_in_work()}'

    @allure.step("Проверка, что модальное окно с описанием заказа открыто")
    def check_modal_window_order_displayed(self):
        assert self.get_text(TapeOrdersLocators.COMPOUND_TITLE) == 'Cостав'

    @allure.step("Проверка изменения счетчиков заказов при новом заказе")
    def check_increment_count(self):
        current_count_all_times = self.get_text(TapeOrdersLocators.COUNT_ALL_TIMES)
        current_count_today = self.get_text(TapeOrdersLocators.COUNT_TODAY)
        assert (int(self.initial_count_today) < int(current_count_today)) and (int(self.initial_count_all_times) < int(current_count_all_times)),\
        f'{self.initial_count_today} !< {current_count_today}, {self.initial_count_all_times} !< {current_count_all_times})'