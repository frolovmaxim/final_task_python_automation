from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from pages.locators import BasePageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER), "Login register is not presented"
        
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PWD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PWD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT).click()
        
        