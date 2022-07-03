from .pages.main_page import MainPage



def test_guest_can_go_to_login_page(browser):
    browser, link = browser
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    