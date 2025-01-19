import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.constructor_locators import ConstructorLocators
from locators.tape_orders_locators import TapeOrdersLocators
from pages.base_page import BasePage

class ConstructorPage(BasePage):

    @allure.step("Нажатие на кнопку Конструктор")
    def click_constructor_btn(self):
        self.click_by_script(ConstructorLocators.CONSTRUCTOR_BTN)

    @allure.step("Нажатие на кнопку Лента заказов")
    def click_tape_orders_btn(self):
        self.click_by_script(ConstructorLocators.ORDERS_TAPE_BTN)

    @allure.step("Нажатие на булку в конструкторе")
    def click_to_bun(self):
        self.find_element(ConstructorLocators.BUNS).click()

    @allure.step("Проверка открытия модального окна булки")
    def check_modal_window_details_displayed(self):
        self.click_to_bun()
        assert self.get_text(ConstructorLocators.DESCRIPTION_TITLE) == 'Детали ингредиента'

    @allure.step("Проверка закрытия модального окна булки")
    def check_modal_window_closed(self):
        self.close_modal_window()
        assert self.find_element(ConstructorLocators.DESCRIPTION_TITLE, condition=EC.invisibility_of_element)

    @allure.step("Нажатие на кнопку Оформить заказ")
    def click_create_order_btn(self):
        self.click_by_script(ConstructorLocators.CREATE_ORDER_BTN)
        assert self.get_text(ConstructorLocators.ORDER_STATUS) == 'Ваш заказ начали готовить'

    @allure.step("Закрытие модального окна")
    def close_modal_window(self):
        self.click_by_script(ConstructorLocators.CLOSE_MODAL_BTN)

    @allure.step("Добавление булки в заказ")
    def add_buns(self):
        ingredient = self.find_element(ConstructorLocators.BUNS)
        basket_lst = self.find_element(ConstructorLocators.BASKET)
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();
            const dragStartEvent = new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragStartEvent);

            const dragOverEvent = new DragEvent('dragover', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dragOverEvent);

            const dropEvent = new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dropEvent);

            const dragEndEvent = new DragEvent('dragend', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragEndEvent);
            """,
            ingredient,
            basket_lst
        )
        assert self.get_text(ConstructorLocators.BUNS_COUNTER) == '2', f'Фактический результат {self.get_text(ConstructorLocators.BUNS_COUNTER)}'

    @allure.step("Формирование заказа")
    def create_order(self):
        self.add_buns()
        self.click_create_order_btn()

    @allure.step("Проверка перехода по кнопкам Конструктор или Лента заказов")
    def check_redirect_nav_tab(self, url, elem):
        if elem == 'Конструктор':
            self.click_constructor_btn()
            self.check_redirect_page(url, ConstructorLocators.CONSTRUCTOR_TITLE)
        if elem == 'Лента Заказов':
            self.click_tape_orders_btn()
            self.check_redirect_page(url, TapeOrdersLocators.ORDERS_TAPE_TITLE)