from selenium.webdriver.common.by import By

class MainPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_LINK = (By.CSS_SELECTOR, "#messages")
    TITLE_TOP_LINK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    TITLE_LOW_LINK = (By.CSS_SELECTOR, ".product_main > h1")
    TITLE_TOP_PRICE_LINK = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    TITLE_LOW_PRICE_LINK = (By.CSS_SELECTOR, ".product_main > p.price_color")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form") 
    