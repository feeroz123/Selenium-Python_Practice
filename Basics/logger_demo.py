import logging

class LoggerDemo:

    def logger_task(self):

        # Create a logger and set log level
        logger = logging.getLogger(LoggerDemo.__name__)
        logger.setLevel(logging.INFO)

        # Create a handler and set its log level
        console_handler = logging.StreamHandler()   # To print the log on console, we used Stream Handler.
        console_handler.setLevel(logging.INFO)

        # Create a formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s : %(levelname)s : %(message)s",
                                      datefmt="%d-%m-%Y %I:%M:%S %p")

        # Assign formatter to handler
        console_handler.setFormatter(formatter)

        # Assign handler to logger
        logger.addHandler(console_handler)

        # Perform logging operations
        logger.debug("This is a debug message")
        logger.info("This is a info message")
        logger.warning("This is a warning message")
        logger.error("This is an error message")
        logger.critical("This is a critical message")


do_log = LoggerDemo()
do_log.logger_task()