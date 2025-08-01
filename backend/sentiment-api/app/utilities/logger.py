import logging
from logging.handlers import RotatingFileHandler
import os

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file_path = os.path.join(log_dir, "sentiment.log")
logger = logging.getLogger("sentiment-logger")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(log_file_path, maxBytes=5_000_000, backupCount=5)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
