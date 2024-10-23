import allure
from selenium.webdriver.support import expected_conditions as EC
import data
from pages.redirect_page import RedirectPage
from selenium.webdriver.support.wait import WebDriverWait


@allure.epic("Проверка переходов по страницам")
class TestRedirectPage:
    @allure.title("Клик на лого Яндекса и переход на Дзен")
    @allure.description("Тест перехода на Дзен в новом окне при клике на лого Яндекса")
    @allure.feature("Логотип Яндекс")
    @allure.story("Переход по логотипу Яндекса")
    def test_click_logo_yandex_open_dzen(self, driver):
        """Проверка, что клик на логотип Яндекса редиректит на страницу Дзен в отдельной вкладке"""
        redirect_page = RedirectPage(driver)
        redirect_page.click_yandex_logo()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(EC.url_contains(data.DZEN))
        assert driver.current_url == data.DZEN

    @allure.title("Клик на лого Самоката и переход на главную страницу")
    @allure.description("Тест перехода на главную страницу Самоката при клике на лого Самоката")
    @allure.feature("Логотип Самокат")
    @allure.story("Переход по логотипу Самоката")
    def test_click_logo_scooter_open_home_page(self, driver):
        """Проверка, что клик на логотип Самоката редиректит на главную страницу"""
        driver.get(data.ORDER_PAGE)
        home_page = RedirectPage(driver)
        home_page.click_scooter_logo()
        WebDriverWait(driver, 10).until(EC.url_to_be(data.HOME_PAGE))
        assert driver.current_url == data.HOME_PAGE
