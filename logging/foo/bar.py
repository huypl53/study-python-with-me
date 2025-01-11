import logging

# Create a logger for this module
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set custom log level for this module

# Do not add a handler to the module logger
# The module logger will use the root logger's handler

# Debugging statements
logger.debug("Module logger level: %s", logger.level)


def bar_print_name():
    msg = "print_name: {0}".format(__name__)
    logger.info(msg)


msg = "{0} is imported".format(__name__)
logger.info(msg)
