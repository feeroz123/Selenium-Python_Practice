from selenium import webdriver
import time

class Autocomplete:

    def get_auto_value(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("https://www.goibibo.com/")

        driver.find_element_by_xpath("//div[contains(@class, 'fltSwitchOpt')]//span[text()='One way']").click()
        driver.find_element_by_id("gosuggest_inputSrc").send_keys("Ban")
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@id='react-autosuggest-1']//span[text()='Bangui']").click()

        time.sleep(3)
        driver.quit()


dep_city = Autocomplete()
dep_city.get_auto_value()