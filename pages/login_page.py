from pages.locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert current_url == LoginPageLocators.LOGIN_URL, "Login url {} is not correct".format(current_url)

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        password_input.send_keys(password)
        password_input_repeat = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_REPEAT)
        password_input_repeat.send_keys(password)
        submit = self.browser = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        submit.click()