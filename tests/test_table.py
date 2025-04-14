import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from pages.tables_page import TablesPage


@pytest.fixture
def driver():
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/tables")
        yield driver
        driver.quit()

def test_table_data(driver):
        tables_page = TablesPage(driver)
        #Find all rows in the first table
        rows = driver.find_elements_by_xpath("//*[@id='table1']/thead/tr")
        expected_data = {"Last Name", "First Name", "Email", "Due", "Web Site", "Action"}