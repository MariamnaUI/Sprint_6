import allure
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class RedirectPage(BasePage):
    @allure.step("Кликаем на логотип Яндекса")
    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.click_to_element(BasePageLocators.LOGO_YANDEX)

    @allure.step("Кликаем на логотип Самоката")
    def click_scooter_logo(self):
        """Клик по логотипу самоката"""
        self.click_to_element(BasePageLocators.LOGO_SCOOTER)
