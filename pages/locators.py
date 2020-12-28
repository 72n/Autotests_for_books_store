from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini span a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


# class MainPageLocators:


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT_BUTTON = (By.NAME, "login_submit")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_BOOK_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    ALERT_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")
    ALERT_BASKET_TOTAL_CLOSE_BUTTON = (By.CSS_SELECTOR, ".alert-info a")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    NUM_FIELD = (By.CSS_SELECTOR, "#id_form-0-quantity")
    UPDATE_QUANTITY = (By.CSS_SELECTOR, ".checkout-quantity button")
