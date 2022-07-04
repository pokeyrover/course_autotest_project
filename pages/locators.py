from distutils.util import byte_compile
from selenium.webdriver.common.by import By


class MainPageLocators:                                                                 #selector and url variables for main page
    PAGE_URL = 'http://selenium1py.pythonanywhere.com/'
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
        
class LoginPageLocators:                                                                #selector and url variables for login page
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    
class ProductPageLocators:                                                              #selector and url variables for login page
    PAGE_URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    
    BASKET_PRICE_ALERT = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, 'p.price_color')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success:nth-child(1) .alertinner strong')
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, '.product_main h1')
    