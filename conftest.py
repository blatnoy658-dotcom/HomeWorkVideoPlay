import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver

@pytest.fixture
def driver_chrome():
    driver: WebDriver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def driver_edge():
    driver: WebDriver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# @pytest.fixture
# def driver_fire_fox():
#     driver: WebDriver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
