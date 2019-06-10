from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class Drag:

    def drag_action(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)

        # open the URL and switch to ifram that contains the element
        driver.get("https://jqueryui.com/draggable/")
        driver.switch_to.frame(0)

        # Find the target element
        element = driver.find_element_by_id("draggable")

        # Create an object of ActionChains class
        actions = ActionChains(driver)
        time.sleep(2)

        # Perform the drag action
        actions.drag_and_drop_by_offset(element,100,150).perform()

        # Perform the drag action by combo steps
        # actions.click_and_hold(element).move_by_offset(100, 150).release().perform()

        time.sleep(2)
        driver.quit()


test = Drag()
test.drag_action()