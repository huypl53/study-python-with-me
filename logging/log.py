import logging

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture all messages

# Create a console handler
console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)  # Set to DEBUG to capture all messages

# Add the handler to the root logger
root_logger.addHandler(console_handler)

# Debugging statements
root_logger.debug("Root logger level: %s", root_logger.level)
root_logger.debug("Console handler level: %s", console_handler.level)
