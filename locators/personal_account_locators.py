from selenium.webdriver.common.by import By

class PersonalAccountLocators:

    STELLAR_LOGO = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a') # Логотип стеллар бургерс
    PERSONAL_ACCOUNT = (By.XPATH, '//a[@href="/account"]')  # Кнопка Личный кабинет в хедере
    LOGIN_ACC = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]') # Кнопка Сохранить
    LOGOUT_BTN = (By.XPATH, '//button[contains(text(), "Выход")]')  # Кнопка Выход
    PROFILE_PAGE_DESCRIPTION = (By.XPATH, '//p[@class="Account_text__fZAIn text text_type_main-default"]')  # Надпись "В этом разделе вы можете изменить свои персональные данные"
    ORDER_HISTORY = (By.XPATH, '//a[@href="/account/order-history"]') # Кнопка перехода к Истории заказов
    ORDER_LIST = (By.XPATH, '//ul[@class="OrderHistory_profileList__374GU OrderHistory_list__KcLDB"]') # Список истории заказов
    ORDERS_ID_IN_HISTORY = (By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"]/a/div[1]/p[1]') # ID закза в списке истории заказов
    ORDERS_LST = (By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"]') # Заказ в списке истории заказов