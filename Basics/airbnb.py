from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class AirBNB:

    def perform_search(self):
        baseURL = "https://www.airbnb.co.in/"
        driver = webdriver.Firefox()

        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseURL)

        driver.find_element_by_name("query").send_keys("Bangalore")
        driver.find_element_by_id("checkin_input").send_keys("05/10/2019")
        driver.find_element_by_id("checkout_input").send_keys("05/15/2019")
        driver.find_element_by_xpath("//button[text()='Guests']").click()
        driver.find_element_by_xpath("//div[contains(@aria-labelledby,'adults')]//div[3]//span").click()
        driver.find_element_by_xpath("//div[contains(@aria-labelledby,'children')]//div[3]//span").click()
        driver.find_element_by_xpath("//button[text()='Apply']").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)
        driver.quit()


airSearch = AirBNB()
airSearch.perform_search()






