from log import root_logger
from foo import bar_print_name, baz_print_name

if __name__ == "__main__":
    bar_print_name()
    baz_print_name()
    root_logger.info("main at {0}".format(__name__))
