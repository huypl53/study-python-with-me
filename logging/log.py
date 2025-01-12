import logging

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture all messages

# Create a console handler
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(console_formatter)
console_handler.setLevel(logging.DEBUG)  # Set to DEBUG to capture all messages


debug_file_formatter = logging.Formatter(
    "root debug: %(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
debug_file_hanlder = logging.FileHandler("root.log")
debug_file_hanlder.setFormatter(debug_file_formatter)
debug_file_hanlder.setLevel(logging.DEBUG)

# Add the handler to the root logger
root_logger.addHandler(console_handler)
root_logger.addHandler(debug_file_hanlder)

# Debugging statements
root_logger.debug("Root logger level: %s", root_logger.level)
root_logger.debug("Console handler level: %s", console_handler.level)
