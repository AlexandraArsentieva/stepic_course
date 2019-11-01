from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    INPUT_EMAIL = (By.ID, "id_registration-email")
    INPUT_PASSWORD = (By.ID, "id_registration-password1")
    INPUT_PASSWORD_REPEAT = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "a[href=\"/en-gb/basket/\"]:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketLocators():
    BASKET_EMPTY_LABEL = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_SUMMARY = (By.CSS_SELECTOR, ".basket_summary")
