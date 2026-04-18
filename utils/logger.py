import logging
import os
from datetime import datetime

# log folder

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# log file name with timestamp
LOG_DIR = os.path.join(BASE_DIR, "reports", "logs")
os.makedirs(LOG_DIR, exist_ok=True)
log_filename = os.path.join(LOG_DIR, f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # ── Console Handler ── shows in terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # ── File Handler ── saves to log file
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)

    # ── Format ──
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # avoid duplicate handlers
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger