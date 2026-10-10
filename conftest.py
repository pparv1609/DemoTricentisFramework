from selenium import webdriver
import pytest

@pytest.fixture(autouse=True)
def setup_and_teardown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://demowebshop.tricentis.com/')
    yield driver
    driver.quit()

from urllib import request

## Cross Browser Testing
'''
import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome","edge","firefox"])
def setup_and_teardown(request):

    browser = request.param   ## Get Current value
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()

    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.quit()'''