from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from Selenium.Basics.utilities.getBy import GetBy


class WaitTypes:

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorType, locator, timeoutSecs=10, poll_freq=1):
        element = None

        print("Waiting for the Element for max", timeoutSecs, "secs with polling frequency of", poll_freq, "secs..")
        wait = WebDriverWait(self.driver, timeout=timeoutSecs, poll_frequency=poll_freq,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        try:
            gb = GetBy()
            getBy = gb.get_by(locatorType)
            element = wait.until(EC.element_to_be_clickable((getBy, locator)))
            print("Element was found")
        except:
            print("Element was not found")
        return element

