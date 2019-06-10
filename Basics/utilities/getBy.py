from selenium.webdriver.common.by import By


class GetBy:

    def get_by(self, locatorType):

        locator_type = locatorType.lower()

        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link_text":
            return By.LINK_TEXT
        elif locator_type == "partial_link_text":
            return By.PARTIAL_LINK_TEXT
        elif locator_type == "tag":
            return By.TAG_NAME
        elif locator_type == "css":
            return By.CSS_SELECTOR
        else:
            print("The locator type ", locatorType, " is not valid")

        return False
