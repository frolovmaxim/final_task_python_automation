from selenium.webdriver.common.by import By

class MainPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_LINK = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    TITLE_TOP_LINK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    TITLE_LOW_LINK = (By.CSS_SELECTOR, ".product_main > h1")
    TITLE_TOP_PRICE_LINK = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    TITLE_LOW_PRICE_LINK = (By.CSS_SELECTOR, ".product_main > p.price_color")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PWD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PWD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT = (By.NAME, "registration_submit")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_IS_EMPTY = (By.XPATH, "//*[@id='content_inner']/p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_PRODUCT_LINK = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_IS_EMPTY = (By.XPATH, "//*[@id='content_inner']/p")