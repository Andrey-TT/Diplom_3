import pytest
import allure
import data as dt

class TestConstructorPage:

    @pytest.mark.parametrize('tab, url', [('Конструктор', dt.BASE_URL),
                                          ('Лента Заказов', dt.FEED_URL)])
    @allure.title("Тест перехода по кнопкам в хедере")
    def test_transition_pages(self, constructor_page, tab, url):
        constructor_page.open_page(dt.LOGIN_URL)
        constructor_page.check_redirect_nav_tab(url, tab)

    @allure.title("Тест работы модального окна с описанием ингредиентов")
    def test_ingredient_modal_window(self, constructor_page):
        constructor_page.open_page(dt.BASE_URL)
        constructor_page.check_modal_window_details_displayed()
        constructor_page.check_modal_window_closed()

    @allure.title("Тест создания заказа авторизованным пользователем")
    def test_authorization_user_can_create_order(self, constructor_page, login_page):
        constructor_page.open_page(dt.BASE_URL)
        login_page.authorization(dt.email, dt.password)
        constructor_page.click_constructor_btn()
        constructor_page.create_order()
        constructor_page.check_create_order()