import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):

    @allure.step("Вход в личный кабинет пользователя")
    def authorization(self, mail, password):
        self.find_element(LoginPageLocators.LOGIN_IN_ACCOUNT).click()
        self.write_in_field(LoginPageLocators.EMAIL_INPUT, mail)
        self.write_in_field(LoginPageLocators.PASSWORD_INPUT, password)
        self.find_element(LoginPageLocators.LOGIN_BTN).click()