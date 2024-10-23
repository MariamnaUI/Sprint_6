import allure
import pytest
from data import ANSWER_1, ANSWER_2, ANSWER_3, ANSWER_4, ANSWER_5, ANSWER_6, ANSWER_7, ANSWER_8, ORDER_PAGE
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage


@allure.epic("Проверка главной страницы ЯндексСамокат")
class TestHomePage:
    @pytest.mark.parametrize("question_index, answer", [
        (0, ANSWER_1),
        (1, ANSWER_2),
        (2, ANSWER_3),
        (3, ANSWER_4),
        (4, ANSWER_5),
        (5, ANSWER_6),
        (6, ANSWER_7),
        (7, ANSWER_8),
    ])

    @allure.title("Проверка выпадающего списка")
    @allure.description("Тест открытия вопросов и получение ответов")
    @allure.feature("Вопросы о важном")
    @allure.story("При нажатии на вопрос раскрывается ответ")
    def test_open_faq(self, driver, question_index, answer):
        """Проверка раздела «Вопросы о важном»"""
        home_page = HomePage(driver)
        home_page.open_question(question_index)
        answer_text = home_page.get_answer_text(question_index)
        assert answer_text == answer, f"Expected: {answer}, but got: {answer_text}"

    @allure.title("Клик на верхнюю кнопку «Заказать»")
    @allure.description("Тест перехода на страницу заказа при клике на верхнюю кнопку «Заказать»")
    @allure.feature("Кнопка «Заказать»")
    @allure.story("Клик на кнопку «Заказать»")
    def test_click_top_button_order(self, driver):
        """Проверка клика по кнопке заказа вверху"""
        home_page = HomePage(driver)
        home_page.click_top_button_order()
        assert driver.current_url == ORDER_PAGE

    @allure.title("Клик на нижнюю кнопку «Заказать»")
    @allure.description("Тест перехода на страницу заказа при клике на нижнюю кнопку «Заказать»")
    @allure.feature("Кнопка «Заказать»")
    @allure.story("Клик на кнопку «Заказать»")
    def test_click_bottom_button_order(self, driver):
        """Проверка клика по кнопке заказа внизу"""
        home_page = HomePage(driver)
        home_page.click_bottom_button_order(HomePageLocators.ORDER_BUTTON_BOTTOM)
        assert driver.current_url == ORDER_PAGE
