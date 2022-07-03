from distutils.util import byte_compile
from selenium.webdriver.common.by import By


class MainPageLocators:                                         #selector variables for main page
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    
class LoginPageLocators:                                        #selector variables for login page
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    