from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_BTN = (By.CSS_SELECTOR, '.basket-mini a.btn-default')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket_summary#basket_formset')
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '.content #content_inner>p')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_BTN = (By.CSS_SELECTOR, ".register_form [name='registration_submit']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    USER_EMAIL = (By.CSS_SELECTOR, ".register_form [name='registration-email']")
    USER_PASSWORD = (By.CSS_SELECTOR, ".register_form [name='registration-password1']")
    USER_PASSWORD_REPEAT = (By.CSS_SELECTOR, ".register_form [name='registration-password2']")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success div.alertinner")
    SUCCESS_MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info div.alertinner > p")
