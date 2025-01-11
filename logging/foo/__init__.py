import logging
from foo.bar import bar_print_name

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

logging.info(f'in foo, {__name__} is imported')
