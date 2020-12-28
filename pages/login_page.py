from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self, reg=0, log=0):
        """
        Функции передаётся параметр, который регулирует поведение взаимодействия с полями ввода на странице регистрации:
        log=1 - для входа в учётную запись, reg=1 - для регистрации нового пользователя (уже зарегистрирован),
        оставить пустым - для проверки кликабельности полей ввода
        """
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        if reg:
            self.can_register(1)
        elif log:
            self.can_login(1)
        else:
            self.can_login()
            self.can_register()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "It's not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def can_login(self, log=0):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys("Vladimir@Putin.ru")
        pass_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        pass_field.send_keys("USAsosatb")
        login_submit_button = self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON)
        if log:
            login_submit_button.click()
        time.sleep(1)
        assert email_field and pass_field and login_submit_button, "Can't login"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def can_register(self, reg=0):
        register_email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        register_email_field.send_keys("Vladimir@Putin.ru")
        register_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        register_password_field.send_keys("USAsosatb")
        register_confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_FIELD)
        register_confirm_password_field.send_keys("USAsosatb")
        register_submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        if reg:
            register_submit_button.click()
        assert register_email_field and register_password_field and register_confirm_password_field and register_submit_button, "Can't register"
        time.sleep(1)
