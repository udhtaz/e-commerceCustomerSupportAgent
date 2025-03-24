# app/core/logging.py

import logging
import os
from logging.handlers import RotatingFileHandler

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

LOG_FILE = "logs/app.log"

# Rotating file handler
file_handler = RotatingFileHandler(
    LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
)

# Console handler
console_handler = logging.StreamHandler()

# Formatter
log_format = (
    "%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
)
formatter = logging.Formatter(log_format)

# Set formatters
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Apply handlers to root logger
logging.basicConfig(
    level=logging.INFO,
    handlers=[file_handler, console_handler]
)

# Named logger to use across app
logger = logging.getLogger("ecom_support_logger")

logger.info("✅ Logging setup complete.")
