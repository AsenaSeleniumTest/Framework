#! /usr/bin/env python3
import pytest
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

config = ConfigParser()
config.read('config.ini')
url = "www.saucedemo.com"

@pytest.fixture(scope="class",params=["chrome"],autouse=True)
def driver_setup(request):
    """Initialize the chrome driver."""
   
    if request.param == "chrome":
        service = Service(ChromeDriverManager().install())
        c_options = webdriver.ChromeOptions()
        c_options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(service=service )
        driver.maximize_window()
        driver.get(url)
    elif request.param == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        driver.maximize_window()
        driver.get(url)
    else:
        raise ValueError("Unsupported browser: {}".format(request.param))
    
    yield driver
    driver.quit()


