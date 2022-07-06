import pytest
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"    
])
def test_guest_can_add_product_to_basket(browser, link):                                            #will add product to basket and check success messages
    browser = browser
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.basket_price_is_correct()
    page.product_name_is_correct()
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):                                      #checking present link to login page
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):                                     #checking possibility to open login page from product page
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_product_to_basket(browser):                           #will check not present a success messages after adding product in basket
    browser = browser
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_succes_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):                                                   #will check not present a success message before add product
    browser = browser
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_succes_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):                               #will check disappearing a success message after add product
    browser = browser
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_disappear()
    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):                        #check possibility to go on basket page from product page when basket is empty
    browser = browser
    link = ProductPageLocators.PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_should_empty()
