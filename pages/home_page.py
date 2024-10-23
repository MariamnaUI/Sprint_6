import allure
from selenium.webdriver.common.by import By
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    @allure.step("Открываем вопрос")
    def open_question(self, question_index):
        """Открытие вопроса по индексу"""
        self.scroll_to_bottom()
        question_locator = HomePageLocators.QUESTION_BUTTON
        self.click_to_element((By.XPATH, question_locator[1].format(question_index)))

    @allure.step("Получаем текст ответа")
    def get_answer_text(self, answer_index):
        """Получение ответа по индексу вопроса"""
        answer_locator = HomePageLocators.ANSWER_TEXT
        return self.find_element_with_wait((By.XPATH, answer_locator[1].format(answer_index))).text

    @allure.step("Кликаем на кнопку Заказать вверху страницы")
    def click_top_button_order(self):
        """Клик по кнопке заказа вверху"""
        self.find_element_with_wait(HomePageLocators.ORDER_BUTTON_TOP).click()

    @allure.step("Кликаем на кнопку Заказать внизу страницы")
    def click_bottom_button_order(self, locator):
        """Клик по кнопке заказа внизу"""
        self.scroll_to_element(locator)
        self.click_to_element(locator)
