from selenium.webdriver.common.by import By

class ConstructorLocators:

    CONSTRUCTOR_TITLE = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]') # Надпись "Соберите бургер"
    CONSTRUCTOR_BTN = (By.XPATH, '//p[contains(text(), "Конструктор")]') # Кнопка конструктор
    ORDERS_TAPE_BTN = (By.XPATH, '//p[contains(text(), "Лента Заказов")]') # Кнопка Лента заказов
    ORDER_ID = (By.XPATH, '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]') # Идентификатор заказа в модальном окне
    BUNS = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]') # Краторная булка в конструкторе
    BUNS_COUNTER = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]/div[1]/p') # Счетчик количества ингредиента
    STUFFING_TAB = (By.XPATH, '//span[contains(text(), "Начинки"]') # Кнопка Начинки
    MEAT = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]') # Начинка Мясо бессмертных моллюсков в конструкторе
    BASKET = (By.XPATH, '//div[@class="constructor-element constructor-element_pos_top"]') # Верхняя составляющая бургера
    DESCRIPTION_TITLE = (By.XPATH, '//h2[@class="Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10"]') # Надпись "Детали ингредиента" в модальном окне
    CLOSE_MODAL_BTN = (By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]/div/button') # Кнопка закрытия модального окна
    CREATE_ORDER_BTN = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]') # Кнопка оформить заказ
    ORDER_STATUS = (By.XPATH, '//p[@class="undefined text text_type_main-small mb-2"]') # Надпись "Ваш заказ начали готовить" в модальном окне