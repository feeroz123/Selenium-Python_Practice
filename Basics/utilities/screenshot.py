import time

class Screenshot:

    def take_screenshot(self, driver):

        try:
            filename = str(round(time.time() * 1000)) + ".png"
            destinationPath = "C:\\Users\\feeroz.alam\\Desktop\\"
            file = destinationPath + filename
            driver.save_screenshot(file)
            print("Screenshot is saved as: " + file)
        except:
            raise



