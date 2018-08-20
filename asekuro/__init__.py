import logging

__version__ = "0.0.6"

logging.getLogger(__name__).addHandler(logging.NullHandler())

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(levelname)s - %(message)s'
)
