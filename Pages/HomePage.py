#! /usr/bin/env python3
import Utils.Logger as lc
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage



class HomePage(LoginPage):
    def __init__(self,driver):
        LoginPage.__init__(self, driver)
        self.title_main = (By.XPATH,"//div[@class='app_logo']")
        self.cart_button = (By.XPATH,"//a[@class='shopping_cart_link']")
        self.list_articles = (By.XPATH,"//div[@class='inventory_item_name ']")
        self.list_description = (By.XPATH,"//div[@class='inventory_item_desc']")
        self.list_price = (By.XPATH,"inventory_item_price")
        self.inventory_items = (By.XPATH,"//div[@class='inventory_item']")
        self.add_cart_buttons = (By.XPATH,"//div[@class='inventory_item']//button")
    
    def get_page_tittle(self):
        """Get the title of the page."""
        
        return self.driver.find_element(*self.title_main).text
    
    def add_to_cart_item(self, item_name):
        """Method to add the item to the cart."""
        self.load_site()
        self.login()
        for index,product in enumerate(self.get_article_list()):
            if product.text == item_name:
                self.get_buttons_add_to_cart_list()[index].click()
                return True
        return False
                
    def get_buttons_add_to_cart_list(self):
        """Get the add cart button list"""
        return self.driver.find_elements(*self.add_cart_buttons)
    
    def get_article_list(self):
        """Get the list of available articles."""
        
        names = self.driver.find_elements(*self.list_articles)
        return names
        