import pytest
from  selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from data import HOME_PAGE
from pages.base_page import BasePage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(HOME_PAGE)
    WebDriverWait(driver, 5)
    cookie_banner = BasePage(driver)
    cookie_banner.click_cookie_accept()
    yield driver
    driver.quit()
