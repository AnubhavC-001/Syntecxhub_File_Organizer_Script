"""
Configuration settings for the File Organizer Script.
"""
import os

# Base directory (current directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Folder to scan for files to organize
SOURCE_DIR = os.path.join(BASE_DIR, "test_folder")

# Folder to move the organized files to
DESTINATION_DIR = os.path.join(BASE_DIR, "organized_files")

# Directory for logs
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# Log file path
LOG_FILE = os.path.join(LOGS_DIR, "moved_files.log")

# Extensions mapping
EXTENSION_MAPPING = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".csv", ".xlsx"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Video": [".mp4", ".mkv", ".avi", ".mov"],
    "Scripts": [".py", ".sh", ".bat", ".js", ".html", ".css"],
}
