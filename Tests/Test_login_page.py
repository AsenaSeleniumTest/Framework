import pytest
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

@pytest.mark.usefixtures("driver_setup")
class Test_LoginPage:
    """Class to test home Login page."""
    @pytest.mark.smoke
    def test_login_ok(self,driver_setup):
        """Test login with valid credentials."""
        driver = driver_setup
        h_page= LoginPage(driver)
        h_page.login()
        l_page = HomePage(driver)
        page_title = l_page.get_page_tittle()
        assert page_title == "Swag Labs", "Login failed, page title does not match expected value."
        
        