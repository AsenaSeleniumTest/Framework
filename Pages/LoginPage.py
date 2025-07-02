from selenium.webdriver.common.by import By


class LoginPage:
    """Class to handle the login page actions and elements."""
    def __init__(self, driver):
        self.driver = driver
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
        return self.driver