from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage, MainPageLocators):
    def go_to_login_page(self):                                                                         #open login page function
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        
    def should_be_login_link(self):                                                                     #verification of login link
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), \
            'Login link is not present'
            