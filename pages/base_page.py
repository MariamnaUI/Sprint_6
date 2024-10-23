import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидаем появление нужного элемента")
    def find_element_with_wait(self, locator):
        """Ожидание появления элемента на странице"""
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Скроллим страницу до нужного элемента")
    def scroll_to_element(self, locator):
        """Прокрутка страницы до указанного элемента"""
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликаем на элемент")
    def click_to_element(self, locator):
        """Клик по элементу"""
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step("Скроллим страницу в самый низ")
    def scroll_to_bottom(self):
        """Прокрутка страницы вниз"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Вводим текст")
    def add_text_to_element(self, locator, text):
        """Добавление текста"""
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Соглашаемся с куками")
    def click_cookie_accept(self):
        """Клик согласия с куками"""
        self.click_to_element(BasePageLocators.COOKIE_BUTTON)
