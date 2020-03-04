from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.common.by import By
from pages.locators import BasketPageLocators


class ProductPage(BasePage):
    def go_to_modal_screen(self):
        login_link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        login_link.click()
        
    def add_to_basket(self):
        login_link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        login_link.click()
        
    def should_be_message(self):
        assert self.is_element_present(*MainPageLocators.MESSAGE_LINK), "Login link is not presented"
        
    def should_be_title_price_matching(self):
        assert self.is_text_matching(*MainPageLocators.TITLE_TOP_LINK,*MainPageLocators.TITLE_LOW_LINK) and self.is_text_matching(*MainPageLocators.TITLE_TOP_PRICE_LINK,*MainPageLocators.TITLE_LOW_PRICE_LINK)
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*MainPageLocators.MESSAGE_LINK), "Success message is presented, but should not be"
            
    def should_not_disappeared_success_message(self):
        assert self.is_disappeared(*MainPageLocators.MESSAGE_LINK), "Success message is disappeared, but should not be"
    
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_LINK), "Success message is presented, but should not be"
    
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Products in busket is not presented"    