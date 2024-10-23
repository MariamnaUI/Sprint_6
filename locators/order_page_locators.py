from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FORM = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FORM = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FORM = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION_FORM = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FORM = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")
    FIRST_STATION = (By.XPATH, "//button[@value='1']")
    ORDER_HEADER = (By.XPATH, "//div[@class='Order_Header__BZXOb']")
    DATEPICKER_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATEPICKER_CALENDAR = (By.XPATH, "//div[@class='react-datepicker__current-month']")
    RENTAL_PERIOD = (By.XPATH, "//span[@class='Dropdown-arrow']")
    RENTAL_PERIOD_LIST = (By.XPATH, "//div[@class='Dropdown-option']")
    COLOR_CHECKBOX = (By.XPATH, "//label[contains(text(),'чёрный жемчуг')]")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    ACCEPT_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")
    ORDER_PLACED = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
