import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def find_element(self, locator, condition=EC.element_to_be_clickable, time=10):
        return WebDriverWait(self.driver, time).until(condition(locator))

    def find_elements(self, locator, condition=EC.visibility_of_any_elements_located, time=10):
        return WebDriverWait(self.driver, time).until(condition(locator))

    def open_page(self, url):
        self.driver.get(url)

    def wait_change_value_in_element_page(self, locator, text, time=10,):
        return WebDriverWait(self.driver, time).until_not(EC.text_to_be_present_in_element(locator, text))

    def get_text(self, locator):
        return self.find_element(locator, condition=EC.visibility_of_element_located).text

    def write_in_field(self, input=None, text=None, time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(input)).send_keys(text)

    def check_url(self, expected_url, time=20):
        try:
            WebDriverWait(self.driver, time).until(EC.url_to_be(expected_url))
        except TimeoutException:
            raise AssertionError(
                f"Проверка URL не пройдена\n"
                f"Ожидалось: {expected_url}\n"
                f"Текущий URL: {self.driver.current_url}\n"
                f"Время ожидания: 30 секунд"
            )

    def click_by_script(self, locator):
        element = self.find_element(locator)
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def check_redirect_page(self, url, locator):
        self.check_url(url)
        assert self.find_element(locator, condition=EC.visibility_of_element_located).is_displayed()

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", element)

    def move_the_element(self, locator_element, locator_target):
        element = self.find_element(locator_element)
        target = self.find_element(locator_target)
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
            """, element, target)