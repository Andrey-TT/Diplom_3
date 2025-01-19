from selenium.webdriver.common.by import By

class RecoverPasswordLocators:

    RECOVER_PASS_BTN = (By.LINK_TEXT, 'Восстановить пароль') # Кнопка восстановить пароль
    EMAIL_INPUT = (By.XPATH, '//input[@class="text input__textfield text_type_main-default"]') # Поле ввода электронной почты
    RESTORE_BNT = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]') # Кнопка Восстановить
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]') # Поле ввода нового пароля
    CODE_MSG_INPUT = (By.XPATH, '//input[@type="text"]') # Поле ввода кода из письма
    SHOW_PASS_BTN = (By.XPATH, '//div[@class="input__icon input__icon-action"]') # Кнопка показать пароль
    SHOW_PASS_BTN_CHANGE_TYPE = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default input_status_active"]') # Поле пароля в состояние видимости пароля
    RECOVER_PASS_TITTLE = (By.XPATH, '//h2[contains(text(), "Восстановление пароля")]') # Надпись "Восстановление пароля"
