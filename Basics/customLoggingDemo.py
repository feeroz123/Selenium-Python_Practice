import logging
import Selenium.Basics.utilities.custom_logger as cl


class CustomLoggingDemo:

    log = cl.custom_logging(logging.DEBUG)

    def method1(self):
        self.log.debug("This is a DEBUG message")
        self.log.info("This is a INFO message")
        self.log.warning("This is a WARNING message")
        self.log.error("This is a ERROR message")
        self.log.critical("This is a CRITICAL message")

    def method2(self):
        m2Log = cl.custom_logging(logging.INFO)
        m2Log.debug("This is a DEBUG message")
        m2Log.info("This is a INFO message")
        m2Log.warning("This is a WARNING message")
        m2Log.error("This is a ERROR message")
        m2Log.critical("This is a CRITICAL message")

    def method3(self):
        m3Log = cl.custom_logging(logging.ERROR)
        m3Log.debug("This is a DEBUG message")
        m3Log.info("This is a INFO message")
        m3Log.warning("This is a WARNING message")
        m3Log.error("This is a ERROR message")
        m3Log.critical("This is a CRITICAL message")


logTest = CustomLoggingDemo()
logTest.method1()
logTest.method2()
logTest.method3()
