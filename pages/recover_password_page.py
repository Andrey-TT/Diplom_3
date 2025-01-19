import data
import allure
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.recover_password_locators import RecoverPasswordLocators

class RecoverPasswordPage(BasePage):

    @allure.step("Нажатие на кнопку Восстановить пароль")
    def click_recover_password_btn(self):
        self.click_by_script(RecoverPasswordLocators.RECOVER_PASS_BTN)

    @allure.step("Ввод электронной почты и нажатие на кнопку восстановить")
    def fill_email(self):
        self.write_in_field(RecoverPasswordLocators.EMAIL_INPUT, data.email)
        self.find_element(RecoverPasswordLocators.RESTORE_BNT).click()

    @allure.step("Ввод пароля")
    def fill_password(self):
        self.write_in_field(RecoverPasswordLocators.PASSWORD_INPUT, data.password)

    @allure.step("Проверка видимости пароля при нажатии кнопки показа пароля")
    def check_password_is_displayed(self):
        self.click_by_script(RecoverPasswordLocators.SHOW_PASS_BTN)
        attribute = self.find_element(RecoverPasswordLocators.SHOW_PASS_BTN_CHANGE_TYPE, condition=EC.visibility_of_element_located)
        assert attribute is not None