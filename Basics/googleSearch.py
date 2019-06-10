from selenium import webdriver
from selenium.webdriver.common.by import By
from Selenium.Basics.utilities.getBy import GetBy
from Selenium.Basics.utilities.waitTypes import WaitTypes


class GoogleSearch:

    def gsearch(self, locatorType, locator):

        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://www.google.com/")

        wt = WaitTypes(driver)
        g_element = wt.waitForElement(locatorType, locator)
        g_element.send_keys("This is a test")


newtest = GoogleSearch()
newtest.gsearch("name","q")
