#! /usr/bin/env python3
import Utils.Logger as lc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    """Base class for all pages."""
    
    def __init__(self, driver):
        self.driver = driver
        self.cart_button_counter = (By.XPATH,"//div[contains(@id,'shopping')]//span")
        self.d_logger = lc.get_debug_logger()
        self.wait = WebDriverWait(driver, 10)
        
    
    def get_cart_counter(self):
        """Get the cart counter value."""
        try:
            self.wait.until(EC.presence_of_element_located(self.cart_button_counter))
            return self.driver.find_element(*self.cart_button_counter)
        except NoSuchElementException  as e:
            self.d_logger.error("Error getting cart counter: %s ", e)
            return False
   
    def get_element(self,locator):
        """Get an element by its locator."""
        try:
            element = EC.visibility_of_element_located(locator)
            self.wait.until(element)
            return self.driver.find_element(*locator)
        except NoSuchElementException as e:
            self.d_logger.error("Element not found: %s", e)
            return None
    
    def load_site(self):
        """Load the site with the given URL."""
        self.d_logger.info("Loading site ")
        return BasePage