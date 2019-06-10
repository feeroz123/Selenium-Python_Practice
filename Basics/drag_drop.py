from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class DragDrop:

    def drag_drop(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)

        # Open the URl and switch to the iframe that contains the elements
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(0)
        time.sleep(2)

        # Find the Source and Target elements
        source_element = driver.find_element_by_id("draggable")
        target_element = driver.find_element_by_id("droppable")

        # Create an object for Actions class
        actions = ActionChains(driver)

        # Perform the drag and drop operation
        actions.drag_and_drop(source_element, target_element).perform()

        # Perform the same drag and drop by combo operations
        #actions.click_and_hold(source_element).move_to_element(target_element).release().perform()

        time.sleep(2)
        driver.quit()


test = DragDrop()
test.drag_drop()


