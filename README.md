# File Organizer Script

A complete professional Python automation project to automatically organize your files by their extension into structured categories.

## Project Overview

Are your downloads or document folders a mess? This script automatically scans a specified folder and organizes all files into categorized subfolders based on their file extensions (e.g., Images, Documents, Videos, etc.).

## Features

- **Automated Sorting:** Automatically categorizes files by extension into specific folders.
- **Duplicate Handling:** Safely handles duplicate filenames by appending a numerical counter (e.g., `file_1.txt`).
- **Dry-run Mode:** Preview what files will be moved and where, without actually moving them.
- **Logging Support:** Keeps a record of all moved files in a dedicated log file (`logs/moved_files.log`).
- **Colored Output:** Uses `colorama` to display clear, color-coded terminal messages for better readability.
- **Customizable:** Easily add new categories and file extensions to the configuration.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Syntecxhub/Syntecxhub_File_Organizer_Script.git
   cd Syntecxhub_File_Organizer_Script
   ```

2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions

1. Place the files you want to organize inside the `test_folder` directory.
2. Run the script:
   ```bash
   python organizer.py
   ```
3. To run in dry-run mode (simulate without moving files):
   ```bash
   python organizer.py --dry-run
   ```
4. Check the `organized_files` directory to see your sorted files.

## Future Improvements

- Add a graphical user interface (GUI) using Tkinter or PyQt.
- Support for recursive scanning (organizing files in subfolders).
- Configuration file (JSON/YAML) for easier customization by non-programmers.
- Setup a scheduled task (cron/Task Scheduler) for background auto-organization.
- Add an undo feature to revert the last organization run.
