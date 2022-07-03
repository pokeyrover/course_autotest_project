from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10):       #initiate page object
        self.browser = browser                          
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def open(self):                                     #open page function
        self.browser.get(self.url)
        
    def is_element_present(self, how, what):            #element verification function
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
        