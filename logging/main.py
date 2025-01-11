from log import root_logger
from foo import bar, bar_print_name

# Create a root logger


if __name__ == "__main__":
    bar.bar_print_name()
    bar_print_name()
    root_logger.info("main at {0}".format(__name__))
