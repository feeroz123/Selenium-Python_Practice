from selenium import webdriver
import time


class CalendarSelection:

    def select_date(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("https://www.goibibo.com/")

        driver.find_element_by_xpath("//div[contains(@class, 'fltSwitchOpt')]//span[text()='One way']").click()
        driver.find_element_by_xpath("//input[@placeholder='Departure']").click()
        driver.find_element_by_xpath("//div[@class='DayPicker-Day']//div[@id='fare_20190523']").click()

        time.sleep(3)
        driver.quit()

dep_date = CalendarSelection()
dep_date.select_date()