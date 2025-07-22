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
        h_page.login()
        articles = h_page.get_article_list()
        for i,article in enumerate(articles):
            assert article.text == article_list[i], f"Article {i+1} does not match expected value. Expected: {article_list[i]}, Found: {article}"
        