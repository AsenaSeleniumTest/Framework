#! /usr/bin/env python3
import Utils.Logger as lc
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    """Class to handle the login page actions and elements."""
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.username_field = (By.ID,"user-name")
        self.password_field = (By.ID,"password")
        self.login_button = (By.ID,"login-button")
        self.regular_user = (By.XPATH,"//div[@id='login_credentials']")
        
        
    def get_user_list(self):
        """Get the element with the text for user list."""
        user_list = self.driver.find_element(*self.regular_user).text.split("\n")
        user = user_list[1]
        return user
    
    def login(self):
        """Login steps with valid credentials.  """        
        user = self.get_user_list()
        self.driver.find_element(*self.username_field).send_keys(user)
        self.driver.find_element(*self.password_field).send_keys("secret_sauce")
        self.driver.find_element(*self.login_button).click()
        