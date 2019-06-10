"""
Logging Levels :
    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL

Default Logging level is set to WARNING and above.
"""

import logging

#logging.basicConfig(filename="mylog.log")
#logging.basicConfig(filename="mylog.log", level= logging.INFO)
#logging.basicConfig(filename="mylog.log", level=logging.INFO, format="%(asctime)s: %(levelname)s: %(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s : %(message)s", datefmt="%d-%m-%Y %H:%M:%S")
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s : %(message)s", datefmt="%d-%m-%Y %I:%M:%S %p")

logging.critical("--------------------------------------------------")
logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")