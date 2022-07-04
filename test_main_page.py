from .pages.main_page import MainPage
from .pages.locators import MainPageLocators


def test_guest_can_go_to_login_page(browser):
    browser = browser
    page = MainPage(browser, MainPageLocators.PAGE_URL)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    