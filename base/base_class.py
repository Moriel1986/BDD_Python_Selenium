from selenium import webdriver
from base.webdriver_custom_class import WebDriverCustomClass
from Utilities import Utility_page


class Base_class(WebDriverCustomClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver = webdriver.Chrome(Utility_page.Chrome_Path)

    def set_up(self):
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.set_page_load_timeout(10)
        self.driver.get(Utility_page.URL)

    def tear_down(self):
        self.driver.quit()

