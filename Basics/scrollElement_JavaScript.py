from selenium import webdriver
import time

class Scroll:

    def scroll_element(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)

        # Open the URL using Java Script
        driver.execute_script("window.location = 'https://www.goibibo.com/';")
        time.sleep(5)

        # Click on an element which is not in current view, without scrolling it into view
        driver.find_element_by_xpath("//a[text()='About Us']").click()
        time.sleep(5)

        # Go back to main page
        driver.execute_script("window.location = 'https://www.goibibo.com/';")

        # Scroll the page down
        driver.execute_script("window.scrollBy(0, 1000)")
        time.sleep(3)

        # Scroll the page up
        driver.execute_script("window.scrollBy(0, -1000)")
        time.sleep(3)

        # Scroll by bringing the element into view
        element = driver.find_element_by_xpath("//a[text()='VIEW ALL PRODUCTS']")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)


sc = Scroll()
sc.scroll_element()