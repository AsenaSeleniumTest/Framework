import Utils.Logger as lc
from selenium.webdriver.common.by import By


class BasePage():
    """Base class for all pages."""
    
    def __init__(self, driver):
        self.driver = driver
        self.d_logger = lc.get_debug_logger()
        
    
    def load_site(self, url):
        """Load the site with the given URL."""
        self.d_logger.info("Loading site: %s ",url)
        return BasePage