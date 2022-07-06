import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.locators import MainPageLocators


def test_guest_can_go_to_login_page(browser):                                                   #check possibility to go on login page from main page
    browser = browser
    page = MainPage(browser, MainPageLocators.PAGE_URL)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):                       #check possibility to go to basket page from main page when basket is empty
    browser = browser
    link = MainPageLocators.PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_should_empty()
