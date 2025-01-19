from selenium.webdriver.common.by import By

class LoginPageLocators:

    LOGIN_IN_ACCOUNT = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]') # Кнопка войти в аккаунт
    EMAIL_INPUT = (By.XPATH, '//input[@type="text"]') # Поле ввода электронной почты
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]') # Поле ввода пароля
    LOGIN_BTN = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]') # Кнопка Войти