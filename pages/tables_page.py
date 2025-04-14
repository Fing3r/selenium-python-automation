from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TablesPage:
    def __init__(self, driver):
        self.driver = driver
        self.table_locator = (By.ID, "//*[@id='table1']")