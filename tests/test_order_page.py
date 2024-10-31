import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import ORDER_PAGE, ORDER_DATA_SETS
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


@allure.epic("Проверка формы заказа ЯндексСамокат")
class TestOrderPage:
    @pytest.mark.parametrize("data", ORDER_DATA_SETS)
    @allure.title("Заполнение формы заказа")
    @allure.description("Тест заполнения формы заказа")
    @allure.feature("Форма заказа")
    @allure.story("Заполнение данных для заказа")
    def test_input_order_form(self, driver, data):
        """Проверка ввода данных в форму заказа"""
        driver.get(ORDER_PAGE)
        order_page = OrderPage(driver)
        order_page.fill_first_order_form(data["name"], data["surname"], data["address"], data["phone"])

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(OrderPageLocators.DATEPICKER_INPUT))

        order_page.fill_second_part_of_order()
        assert order_page.is_order_placed_successful()
