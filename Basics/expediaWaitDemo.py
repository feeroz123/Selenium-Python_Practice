from selenium import webdriver
from selenium.webdriver.common.by import By
from Selenium.Basics.utilities.waitTypes import WaitTypes


class expediaWaitDemo:

    def waitdemo(self):
        baseURL = "https://www.expedia.co.in/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(1)  # Implicit wait given just for name sake here

        driver.find_element_by_xpath("//div[@id='wizard-tabs']//button[@data-lob='flight']").click()
        driver.find_element_by_id("flight-type-one-way-label-hp-flight").click()
        driver.find_element_by_id("flight-origin-hp-flight").send_keys("London")
        driver.find_element_by_id("flight-destination-hp-flight").send_keys("Bangalore")
        driver.find_element_by_id("flight-departing-single-hp-flight").send_keys("12/05/2019")
        driver.find_element_by_xpath("//button[contains(@class,'datepicker-close-btn')]").click()
        driver.find_element_by_xpath("//form[@id='gcw-flights-form-hp-flight']//button[contains(@class,'submit')]").click()

        wait = WaitTypes()
        try:
            element_xpathlocator = "//input[@data-test-id='Direct']"
            element = wait.waitForElement(driver, element_xpathlocator)
            print("Element is clicked")
        except:
            print("Element not found - Main method")

ff = expediaWaitDemo()
ff.waitdemo()