import allure
import data as dt
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.recover_password_locators import RecoverPasswordLocators

class RecoverPasswordPage(BasePage):

    @allure.step("Нажатие на кнопку Восстановить пароль")
    def click_recover_password_btn(self):
        self.click_by_script(RecoverPasswordLocators.RECOVER_PASS_BTN)

    @allure.step("Ввод электронной почты и нажатие на кнопку восстановить")
    def fill_email(self):
        self.write_in_field(RecoverPasswordLocators.EMAIL_INPUT, dt.email)
        self.find_element(RecoverPasswordLocators.RESTORE_BNT).click()

    @allure.step("Ввод пароля")
    def fill_password(self):
        self.write_in_field(RecoverPasswordLocators.PASSWORD_INPUT, dt.password)

    @allure.step("Проверка видимости пароля при нажатии кнопки показа пароля")
    def check_password_is_displayed(self):
        self.click_by_script(RecoverPasswordLocators.SHOW_PASS_BTN)
        attribute = self.find_element(RecoverPasswordLocators.SHOW_PASS_BTN_CHANGE_TYPE, condition=EC.visibility_of_element_located)
        assert attribute is not None

    @allure.step("Проверка открытия страницы востановления пароля")
    def check_redirect_forgot_password_page(self):
        self.check_redirect_page(dt.FORGOT_PASS_URL, RecoverPasswordLocators.RECOVER_PASS_TITTLE)

    @allure.step("Проверка открытия страницы сброса пароля")
    def check_redirect_reset_password_page(self):
        self.check_redirect_page(dt.RESET_PASS_URL, RecoverPasswordLocators.PASSWORD_INPUT)