from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        if 'login' in self.browser.current_url:
            assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Register email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Register password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM), "Register password confirmation " \
                                                                                      "is not presented"
