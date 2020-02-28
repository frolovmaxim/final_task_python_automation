from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def go_to_modal_screen(self):
        login_link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        login_link.click()
        
    def should_be_message(self):
        assert self.is_element_present(*MainPageLocators.MESSAGE_LINK), "Login link is not presented"
        
    def should_be_title_price_matching(self):
        assert self.is_text_matching(*MainPageLocators.TITLE_TOP_LINK,*MainPageLocators.TITLE_LOW_LINK) and self.is_text_matching(*MainPageLocators.TITLE_TOP_PRICE_LINK,*MainPageLocators.TITLE_LOW_PRICE_LINK)
    
