import logging
import sys

from app.config.settings import LOG_FORMAT, LOG_LEVEL


def setup_logger(name: str) -> logging.Logger:
    """Configure and return a logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(LOG_LEVEL)

    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


# Create default logger
logger = setup_logger(__name__)
logger.setLevel(logging.INFO)
