import pytest
import driver_factory
import data as dt
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.tape_orders_page import TapeOrdersPage
from pages.recover_password_page import RecoverPasswordPage
from pages.personal_account_page import PersonalAccountPage

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    driver = driver_factory.WebDriverFactory.create_driver(browser)
    yield driver
    driver.quit()

@pytest.fixture()
def recover_password_page(driver):
    page = RecoverPasswordPage(driver, dt.LOGIN_URL)
    return page

@pytest.fixture()
def personal_acc_page(driver):
    page = PersonalAccountPage(driver, dt.BASE_URL)
    return page

@pytest.fixture()
def constructor_page(driver):
    page = ConstructorPage(driver, dt.BASE_URL)
    return page

@pytest.fixture()
def tape_orders_page(driver):
    page = TapeOrdersPage(driver, dt.BASE_URL)
    return page

@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver, dt.BASE_URL)
    return page