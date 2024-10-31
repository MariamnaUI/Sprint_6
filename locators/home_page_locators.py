from selenium.webdriver.common.by import By


class HomePageLocators:
    QUESTION_BUTTON = (By.XPATH, "//div[@id='accordion__heading-{}']")
    ANSWER_TEXT = (By.XPATH, "//div[@id='accordion__panel-{}']")

    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
