from selenium import webdriver
import time

class SwitchTo:

    def get_page(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        driver.maximize_window()

        # driver.get("https://learn.letskodeit.com/p/practice")
        driver.execute_script("window.location='https://learn.letskodeit.com/p/practice';")  # Using Java Script method
        return driver

    def switch_to_window(self):
        driver = self.get_page()

        parent_handle = driver.current_window_handle
        time.sleep(3)
        driver.find_element_by_id("openwindow").click()

        handles = driver.window_handles

        for handle in handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element_by_id("search-courses").send_keys("Python")
                time.sleep(3)
                driver.close()
                break

        driver.switch_to.window(parent_handle)
        driver.find_element_by_id("name").send_keys("Window Test Successful")
        time.sleep(3)

        driver.quit()

    def switch_to_alerts(self):
        driver = self.get_page()

        # Finding and interacting with Alert
        driver.find_element_by_id("alertbtn").click()
        time.sleep(2)
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(2)

        # Finding and interacting with Confirm Alert
        driver.find_element_by_id("confirmbtn").click()
        time.sleep(2)
        confirm1 = driver.switch_to.alert
        confirm1.dismiss()
        time.sleep(2)

        driver.find_element_by_id("name").send_keys("Alert Test successful")
        time.sleep(2)
        driver.quit()

    def switch_to_iframe(self):
        driver = self.get_page()

        # Find the Frame and scroll it into view
        iframe = driver.find_element_by_id("courses-iframe")
        driver.execute_script("arguments[0].scrollIntoView(true);", iframe)
        driver.execute_script("window.scrollBy(0, -200)")    # To avoid the head ribbon obstructing the field brought into view


        driver.switch_to.frame("courses-iframe")    # Using ID of the frame
        #driver.switch_to.frame(("iframe-name"))     # Using NAME of the frame
        #driver.switch_to.frame(0)                   # Using the INDEX value of the frame

        driver.find_element_by_id("search-courses").send_keys("Python")
        time.sleep(3)

        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -800)")  # To avoid the head ribbon obstructing the field brought into view

        driver.find_element_by_id("name").send_keys("Frame Test successful")
        time.sleep(2)
        driver.quit()


test = SwitchTo()
test.switch_to_window()
test.switch_to_alerts()
test.switch_to_iframe()