from selenium import webdriver
from Selenium.Basics.utilities.screenshot import Screenshot
import time

class Screenshot_Demo:

        def test(self):
            driver = webdriver.Firefox()
            driver.implicitly_wait(3)
            driver.maximize_window()

            driver.get("https://www.goibibo.com/")
            driver.find_element_by_id("gosuggest_inputSrc").send_keys("Bangalore (BLR)")
            driver.find_element_by_id("gosuggest_inputDest").send_keys("Seol (SEL)")
            driver.find_element_by_id("gi_search_btn").click()
            time.sleep(2)

            ss = Screenshot()
            ss.take_screenshot(driver)


ss_demo = Screenshot_Demo()
ss_demo.test()