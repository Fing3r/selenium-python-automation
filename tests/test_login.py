import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import logging

logging.basicConfig(filename='test_log.log', level=logging.INFO)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("tomsmith", "SuperSecretPassword!")
    success_message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success_message
    logging.info("Valid login test passed")

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("wronguser", "wrongpass")
    driver.implicitly_wait(5)  # Wait
    error_message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in error_message
    logging.info("Invalid login test passed")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])