import logging


def get_logger(name, loglevel="INFO"):
    logger = logging.getLogger(name)
    logger.setLevel(loglevel.upper())
    if not logger.handlers:
        ch = logging.StreamHandler()
        formatter = logging.Formatter("%(message)s")
        ch.setLevel(loglevel.upper())
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
