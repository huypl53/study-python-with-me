import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("foo.baz.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)

# logger.setLevel(logging.WARNING)
logger.setLevel("DEBUG")

logger.info(f"in foo.baz, {__name__} is imported")
logger.propagate = False


def baz_print_name():
    msg = f"baz_print_name: {__name__}"
    logger.info(msg)
