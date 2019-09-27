import pytest
from selenium import webdriver

@pytest.fixture
def test_chbrowser():
        print("hellwo drls")
def test_data(test_chbrowser):
    driver = webdriver.Chrome(executable_path="J://pytest-selenium//chromedriver.exe")
    driver.maximize_window()
