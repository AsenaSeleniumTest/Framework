#! /usr/bin/env python3
import pytest
import asyncio
import Utils.Logger as lc
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

@pytest.mark.usefixtures("driver_setup")
class Test_LoginPage:
    """Class to test home Login page."""
    
    @pytest.mark.smoke
    def test_login_ok(self,driver_setup):
        """Test login with valid credentials."""
        driver = driver_setup
        l_page = HomePage(driver)
        
        l_page.d_logger.info("Starting login test with valid credentials.")
        l_page.login()
        page_title = l_page.get_page_tittle()
        l_page.d_logger.info("Verifying page title after login.")
        assert page_title == "Swag Labs", "Login failed, page title does not match expected value."
        
        