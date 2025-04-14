import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import logging
import time # Time module for measurin execution time

logging.basicConfig(
    filename='testsrun.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',  # Add timestamp and log level
    datefmt='%Y-%m-%d %H:%M:%S'  # Set date format

)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()

def test_valid_login(driver):
    start_time = time.time()  # Start time for performance measurement 
    login_page = LoginPage(driver)
    driver.implicitly_wait(5)  # Wait
    login_page.login("tomsmith", "SuperSecretPassword!")
    success_message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success_message
    end_time = time.time()  # End time for performance measurement
    elapsed_time = end_time - start_time  # Calculate elapsed time
    logging.info(f"Valid login test passed successfully in {elapsed_time:.2f}")

def test_invalid_login(driver):
    start_time = time.time()  # Start time for performance measurement 
    login_page = LoginPage(driver)
    login_page.login("wronguser", "wrongpass")
    driver.implicitly_wait(5)  # Wait
    error_message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in error_message
    end_time = time.time()  # End time for performance measurement
    elapsed_time = end_time - start_time  # Calculate elapsed time
    logging.info(f"Invalid login test passed in {elapsed_time:.2f}")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])