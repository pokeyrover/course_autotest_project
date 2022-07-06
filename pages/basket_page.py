from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_empty(self):                                                                      #check basket`s empty
        self.should_not_be_any_products()
        self.should_not_be_add_voucher_button()
        self.should_be_message_about_empty_basket()

    def should_not_be_any_products(self):                                                               #basket hasn`t any product
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS),\
            'Basket has any item, but should nothing'
            
    def should_not_be_add_voucher_button(self):                                                         #basket hasn`t add voucher button
        assert self.is_not_element_present(*BasketPageLocators.ADD_VOUCHER_BUTTON),\
            'Add voucher button is present, but should not'
        
    def should_be_message_about_empty_basket(self):                                                     #basket has message about empty basket
        assert self.get_element_text(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET),\
            'Message about empty basket not found'
