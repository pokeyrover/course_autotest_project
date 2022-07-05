import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):                                               #initiate page object
        self.browser = browser                          
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def open(self):                                                                             #open page function
        self.browser.get(self.url)
        
    def is_element_present(self, how, what):                                                    #element verification function
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    def is_not_element_present(self, how, what, timeout=4):                                     #element shouldn`t be on page 
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        
        return False
    
    def is_disappeared(self, how, what, timeout=4):                                             #element should disappear from page
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_all_elements_located((how, what)))
        except TimeoutException:
            return False
        
        return True
    
    def get_element_text(self, how, what):                                                      #function for getting text from element
        element = self.browser.find_element(how, what)
        return element.text

    def go_to_login_page(self):                                                                 #open sign up page and check current url
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        assert 'login' in self.browser.current_url, \
            'Current url isn`t login page url'
        
    def should_be_login_link(self):                                                             #checking present link to sign up page
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK),\
            'Login link is not presented'
        
    def solve_quiz_and_get_code(self):                                                          #function for solution for a math example in add product alert
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Your code: {alert_text}')
            alert.accept()
        except NoAlertPresentException:
            print('No secoond alert presented')
        