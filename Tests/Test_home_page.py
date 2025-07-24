#! /usr/bin/env python3
import pytest
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage


@pytest.mark.usefixtures("driver_setup")
class Test_Home_Page:
    """class to test home page for items in sale"""
    
    @pytest.mark.smoke
    def test_list_articles(self,driver_setup):
        """Test the list of available articles"""
        article_list = ["Sauce Labs Backpack","Sauce Labs Bike Light","Sauce Labs Bolt T-Shirt","Sauce Labs Fleece Jacket","Sauce Labs Onesie","Test.allTheThings() T-Shirt (Red)"]
        driver = driver_setup
        h_page = HomePage(driver)
        h_page.d_logger.info("Starting test for list of articles Login user.")
        h_page.login()
        h_page.d_logger.info("Verifying the list of articles on the home page.")
        articles = h_page.get_article_list()
        for i,article in enumerate(articles):
            assert article.text == article_list[i], f"Article {i+1} does not match expected value. Expected: {article_list[i]}, Found: {article}"
        
    def test_add_items_to_cart(self,driver_setup):
        """Test adding items to the cart."""
        driver = driver_setup
        h_page = HomePage(driver)
        h_page.d_logger.info("Starting test for adding items to the cart.")
        h_page.login()
        
        # Add first item to cart
        assert h_page.add_to_cart_item("Sauce Labs Backpack"), "Failed to add Sauce Labs Backpack to cart."
        
        # Add second item to cart
        assert h_page.add_to_cart_item("Sauce Labs Bike Light"), "Failed to add Sauce Labs Bike Light to cart."
        
        # Verify items in cart
        cart_item = h_page.get_cart_counter()
        assert cart_item.text() == '2', "Cart does not contain the expected number of items."