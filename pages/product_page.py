from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_basket(self):                                    #add function to basket
        add_buttom = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_buttom.click()
        
    def basket_price_is_correct(self):                                  #price in alert and price in page are same
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_ALERT), \
            "Price in basket alert is miss"
        
        product_page_price = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE)
        basket_price_alert = self.get_element_text(*ProductPageLocators.BASKET_PRICE_ALERT)
        basket_price_alert = basket_price_alert.split('&')[0]
        assert product_page_price == basket_price_alert, \
            "Price in alert and price in page are different"
            
    def product_name_is_correct(self):                                  #product name in page and product name in alert are same
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_NAME), \
            "Alert with product name is miss"
        
        product_name_on_page = self.get_element_text(*ProductPageLocators.PRODUCT_NAME_ON_PAGE)
        product_name_on_alert = self.get_element_text(*ProductPageLocators.ALERT_PRODUCT_NAME)
        assert product_name_on_page == product_name_on_alert, \
            "Product name in page and product name in alert are different"
        