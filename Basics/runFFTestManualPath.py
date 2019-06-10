from selenium import webdriver


class RunFFTest():

    def testMethod(self):
        driverLocation = "C:\\Users\\feeroz.alam\\OneDrive - Subex Limited\PYTHON\\Selenium\\geckodriver.exe"
        driver = webdriver.Firefox(executable_path=driverLocation)
        driver.get("http://google.com")


ff = RunFFTest()
ff.testMethod()

