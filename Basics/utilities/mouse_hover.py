from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class Mouse_Hover:

    def mousehover(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("https://learn.letskodeit.com/p/practice")

        # Find the element on which the mouse is to be hovered
        element = driver.find_element_by_id("mousehover")
        time.sleep(2)

        # Create an object for ActionChains class
        actions = ActionChains(driver)

        # Bring the target element into view
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("window.scrollBy(0, -200)")
        time.sleep(2)
        # Perform the mouse hover action (Move to the element)
        actions.move_to_element(element).perform()
        time.sleep(2)
        # Find and click on the 'Top' value from the mouse hover list
        value1 = driver.find_element(By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Top']")
        actions.click(value1).perform()
        time.sleep(2)

        # Bring the target element into view
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("window.scrollBy(0, -200)")
        time.sleep(2)
        # Perform the mouse hover action (Move to the element)
        actions.move_to_element(element).perform()
        time.sleep(2)
        # Find and click on the 'Reload' value from the mouse hover list
        value2 = driver.find_element(By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Reload']")
        actions.click(value2).perform()
        time.sleep(2)

        driver.quit()


test = Mouse_Hover()
test.mousehover()