from .basket_page import BasketPage
from .login_page import LoginPage
from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasketPage, LoginPage, BasePage, MainPageLocators):
    pass
            