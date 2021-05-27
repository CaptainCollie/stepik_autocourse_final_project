from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".btn-items")
    BASKET_EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "#register_form button")
    OK_SIGN = (By.CSS_SELECTOR, ".icon-ok-sign")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success strong")
    BASKET_SUM = (By.CSS_SELECTOR, ".alert-info strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")