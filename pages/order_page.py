from datetime import datetime, timedelta
import allure
from data import COMMENT_TEXT
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Заполняем первую часть формы заказа")
    def fill_first_order_form(self, name, surname, address, phone):
        """Заполнение первой части формы заказа"""
        self.add_text_to_element(OrderPageLocators.NAME_FORM, name)
        self.add_text_to_element(OrderPageLocators.SURNAME_FORM, surname)
        self.add_text_to_element(OrderPageLocators.ADDRESS_FORM, address)
        self.add_text_to_element(OrderPageLocators.PHONE_FORM, phone)
        self.click_to_element(OrderPageLocators.STATION_FORM)
        self.click_to_element(OrderPageLocators.FIRST_STATION)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполняем вторую часть формы заказа")
    def fill_second_part_of_order(self):
        """Заполнение второй части формы заказа"""
        tomorrow_date = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")
        self.add_text_to_element(OrderPageLocators.DATEPICKER_INPUT, tomorrow_date)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_LIST)
        self.click_to_element(OrderPageLocators.COLOR_CHECKBOX)
        self.add_text_to_element(OrderPageLocators.COMMENT_INPUT, COMMENT_TEXT)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.ACCEPT_ORDER_BUTTON)

    def is_order_placed_successful(self):
        """Проверка, что появилось окно об успешном размещении заказа"""
        return self.find_element_with_wait(OrderPageLocators.ORDER_PLACED).is_displayed()
