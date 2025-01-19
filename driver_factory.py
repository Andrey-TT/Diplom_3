from selenium import webdriver
class WebDriverFactory:
    @staticmethod
    def create_driver(browser):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('--window-size=1920,1080')
            return webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument('--window-size=1920,1080')
            return webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Браузер не подключен : {browser}")