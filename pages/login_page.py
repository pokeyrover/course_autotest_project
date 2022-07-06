from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):                                                     #login page verification
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):                                                      #verification page url
        assert 'login' in self.browser.current_url, \
            'Current url isn`t login page url'

    def should_be_login_form(self):                                                     #verification presence of the login form
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'Login form is miss'

    def should_be_register_form(self):                                                  #verification presence of the register form
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'Register form is miss'
            
    def registration_new_user(self, email, password):                                   #registration new user and checking success message
        self.enter_in_field(*LoginPageLocators.REGISTRATION_EMAIL, email)
        self.enter_in_field(*LoginPageLocators.REGISTRATION_PASS, password)
        self.enter_in_field(*LoginPageLocators.REGISTRATION_PASS_CONFIRM, password)
        self.press_button(*LoginPageLocators.REGISTRATION_BUTTON)
        assert self.is_element_present(*LoginPageLocators.SUCCESS_REG_MESSAGE),\
            'Success registration message not found'