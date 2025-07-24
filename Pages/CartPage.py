#! /usr/bin/env python3
import Utils.Logger as lc
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.cart_title = (By.XPATH,"//span[@class = 'title']")
        self.cart_items = (By.XPATH,"")
        self.checkout_button = (By.XPATH,"//button[@id='checkout']")