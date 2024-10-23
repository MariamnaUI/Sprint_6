from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")

    COOKIE_TEXT = (By.XPATH, "//div[@class='App_CookieText__1sbqp']")
    COOKIE_BUTTON = (By.XPATH, "//button[@id='rcc-confirm-button']")