from selenium.webdriver.common.by import By


class BasePageLocators:                                                                 #selectors for BasePage class
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group :nth-child(1).btn')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class MainPageLocators:                                                                 #selector and url variables for main page
    PAGE_URL = 'http://selenium1py.pythonanywhere.com/'
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
        
class LoginPageLocators:                                                                #selector and url variables for login page
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    
    REGISTRATION_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASS_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[value="Register"]')
    SUCCESS_REG_MESSAGE = (By.CSS_SELECTOR, '.alert-success.fade.in')
    
class ProductPageLocators:                                                              #selector and url variables for login page
    PAGE_URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    PAGE_URL_WITHOUT_PROMO = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    
    BASKET_PRICE_ALERT = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, 'p.price_color')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success:nth-child(1) .alertinner strong')
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, '.product_main h1')
    
class BasketPageLocators:                                                               #selectors for basket page
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    ADD_VOUCHER_BUTTON = (By.CSS_SELECTOR, '#content_inner p a.btn')
    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p a')
    