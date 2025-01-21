from selenium.webdriver.common.by import By

class TapeOrdersLocators:

    ORDERS_TAPE_TITLE = (By.XPATH, '//h1[@class="text text_type_main-large mt-10 mb-5"]')  # Надпись "Лента заказов"
    FIRST_ORDER = (By.XPATH, '//a[@class="OrderHistory_link__1iNby"]') # Первый заказ в ленте заказов
    COMPOUND_TITLE = (By.XPATH, '//p[@class="text text_type_main-medium mb-8"]')# Надпись "Состав" в модальном окне
    ORDER_ID = (By.XPATH, '//p[@class="text text_type_digits-default"]') # ID заказа
    COUNT_ALL_TIMES = [By.XPATH, '//div[@class="OrderFeed_ordersData__1L6Iv"]/div[2]/p[2]']  # Счетчик  "Выполнено за все время"
    COUNT_TODAY = [By.XPATH, '//div[@class="OrderFeed_ordersData__1L6Iv"]/div[3]/p[2]']  # Счетчик "Выполнено за сегодня"
    ORDER_IN_WORKS = [By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li']  # Заказ в разделе "В работе"