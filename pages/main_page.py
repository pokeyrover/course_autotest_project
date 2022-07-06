from .basket_page import BasketPage
from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasketPage, BasePage, MainPageLocators):
    pass
            