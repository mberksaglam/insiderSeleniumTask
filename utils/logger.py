import logging


class ColoredFormatter(logging.Formatter):
    # ANSI escape codes for colors
    RESET = "\033[0m"
    DEBUG = "\033[94m"  # Blue
    INFO = "\033[92m"  # Green
    WARNING = "\033[93m"  # Yellow
    ERROR = "\033[91m"  # Red
    CRITICAL = "\033[41m"  # White text on red background

    def format(self, record):
        # Apply color based on the log level
        if record.levelname == "DEBUG":
            record.msg = self.DEBUG + str(record.msg) + self.RESET
        elif record.levelname == "INFO":
            record.msg = self.INFO + str(record.msg) + self.RESET
        elif record.levelname == "ERROR":
            record.msg = self.ERROR + str(record.msg) + self.RESET

        return super().format(record)

def setup_logger(name):
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # File handler
        fh = logging.FileHandler('test_log.log')
        fh.setLevel(logging.DEBUG)

        # Formatter
        formatter = ColoredFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # Add handlers to logger
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger
