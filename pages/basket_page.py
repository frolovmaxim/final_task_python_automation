from pages.base_page import BasePage
from pages.locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)
    