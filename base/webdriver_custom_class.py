import os
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Utilities import Utility_page


class WebDriverCustomClass:

    def __init__(self, driver):
        self.time = None
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()

        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'class':
            return By.CLASS_NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        elif locator_type == 'partial link':
            return By.PARTIAL_LINK_TEXT
        elif locator_type == 'tag':
            return By.TAG_NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        else:
            raise Exception("Not supported locator!")

    def get_element(self, locator, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(lambda driver: self.driver.find_element(by_type, locator))
            return element
        except:
            raise Exception("Element {0} not found".format(locator))

    def get_elements(self, locator, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.driver, 10)
            elements = wait.until(lambda driver: self.driver.find_elements(by_type, locator))
            return elements
        except:
            raise Exception("Elements weren't found")

    def click_on_element(self, locator, locator_type="id"):
        element = self.get_element(locator, locator_type)
        element.click()

    def send_keys_to(self, locator, data="", locator_type="id"):
        element = self.get_element(locator, locator_type)
        element.send_keys(data)

    def hover_over_an_element_and_click_on(self, locator, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator, locator_type)
            hover = ActionChains(self.driver)
            hover.move_to_element(element).perform()
        except:
            raise Exception("Element {0} is not visible".format(locator))

    def hover_over_an_element(self, element, locator, locator_type="id"):
        try:
            hover = ActionChains(self.driver)
            hover.move_to_element(element).perform()
            self.is_element_visible(locator, locator_type).click()
        except:
            raise Exception("Element {0} is not visible".format(element))

    def hover_over_first_element_click_on_second(self, *args):
        locator_1, locator_type_1, locator_2, locator_type_2, locator_3, locator_type_3 = args
        locator_type_1.lower()
        locator_type_2.lower()
        locator_type_3.lower()
        main_button = self.get_element(locator_1, locator_type_1)
        second_button = self.get_element(locator_2, locator_type_2)
        third_element = self.get_element(locator_3, locator_type_3)
        hover = ActionChains(self.driver)
        hover.move_to_element(main_button).pause(1).move_to_element(second_button).pause(1).perform()
        third_element.click()

    def scroll_into_view(self, locator, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator, locator_type)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except:
            raise Exception("Element {0} is not visible".format(locator))

    def is_element_visible(self, locator, locator_type="id"):
        try:
            by_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
            return element
        except:
            raise Exception("Element {0} is not visible".format(locator))

    def click_on_returned_element(self, element):
        element.click()

    def wait_and_click(self, locator, number, locator_type):
        element = self.is_element_visible(locator.format(number), locator_type)
        self.click_on_returned_element(element)

    def get_title(self):
        try:
            self.driver.title()
        except:
            print("Couldn't retrieve title from document object model")

    def verify_title(self):
        if self.get_title() == Utility_page.Title:
            print("Test Passed")
        else:
            print("Test Failed")

    def forward(self):
        try:
            self.driver.forward()
        except:
            print("unable to navigate forward")

    def back(self):
        try:
            self.driver.back()
        except:
            print("unable to navigate back")

    def drop_down_handle(self, element_and_click, dropdown_locator_type, scroll_locator, scroll_locator_type):
        self.click_on_element(element_and_click, dropdown_locator_type)
        self.time.sleep(4)
        self.click_on_element(scroll_locator, scroll_locator_type)

    def enter_search_data(self, data_locator, data, data_locator_type):
        self.send_keys_to(data_locator, data, data_locator_type)

    def get_text_by_xpath(self, locator):
        """
        This method is get the text present within given web element.
        param locator: XPATH of given element
        param_type: string
        """

        return self.driver.find_element_by_xpath(locator).text

    def wait_for_element_invisible(self, locator, timeout=20):
        """
        This method is to wait for visibility of given element for given time(default timeout = 20 secs.)
        If element does not present in given max time, this will throw timeout exception.
        param locator: XPATH of given element
        param_type: string
        param timeout: maximum wait timeout
        param_type: number
        """

        print("# Wait for element to appear... %s" % locator)
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((By.XPATH, locator)))

    def assert_element_is_not_present(self, locator):
        """
        This method is to assert element is present or not.
        param locator: XPATH of given element
        param_type: string
        """
        print("# Verifying Element is not present.")
        assert not self.is_element_visible(locator), "Element '%s' should not be present." % locator

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            print("Wait :: " + str(sec) + " seconds for " + info)
            try:
                time.sleep(sec)
            except:
                traceback.print_stack()

    def navigate_to(self, url):
        print("Navigate to '%s'" % url)
        self.driver.get(url)

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, frame_reference):
        self.driver.switch_to.frame(frame_reference)

    def switch_to_window(self, window_name):
        self.driver.switch_to.window(window_name)

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            print("Screenshot save to directory: " + destinationFile)
        except:
            print("### Exception Occurred when taking screenshot")
            traceback.print_stack()

