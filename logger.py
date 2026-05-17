"""
Logging configuration for the File Organizer Script.
"""
import logging
import os
from config import LOG_FILE, LOGS_DIR

def setup_logger():
    """Sets up the logger to write to both console and file."""
    
    # Ensure logs directory exists
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)
        
    logger = logging.getLogger("FileOrganizer")
    logger.setLevel(logging.INFO)
    
    # Formatter for log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # File handler
    file_handler = logging.FileHandler(LOG_FILE, mode='a')
    file_handler.setFormatter(formatter)
    
    # Avoid adding handlers multiple times if imported multiple times
    if not logger.handlers:
        logger.addHandler(file_handler)
        
    return logger

logger = setup_logger()
